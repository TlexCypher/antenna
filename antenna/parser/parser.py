import xml.etree.ElementTree as ET
from collections import defaultdict

from antenna.config.build_xml import BuildXML
from antenna.parser.parse_result import ParseResult


class Parser:
    def __init__(self, build_xml: BuildXML):
        self.build_xml = build_xml
        self.tree = ET.parse(self.build_xml.get_path())
        self.root = self.tree.getroot()

    def parse(self) -> ParseResult:
        return ParseResult(self.__parse_src_kind())

    def __parse_src_kind(self) -> list[str]:
        src_dirs: set[str] = set()
        if self.root is None:
            return list(src_dirs)

        # gather properties
        props: dict[str, str] = defaultdict(str)
        for prop in self.root.iter('property'):
            name, value = prop.attrib.get('name'), prop.attrib.get('value')
            if name and value:
                props[name] = value

        # gather path elements
        path_elements: dict[str, list[str]] = defaultdict(list[str])
        for path in self.root.iter('path'):
            path_id = path.attrib.get('id')
            if not path_id:
                continue
            for path_element in path.findall('pathelement'):
                location = path_element.attrib.get('location')
                if not location:
                    continue
                path_elements[path_id].append(location)

        for javac in self.root.iter('javac'):
            src_dir = javac.attrib.get('srcdir')
            if not src_dir:
                continue
            if src_dir.startswith('${') and src_dir.endswith('}'):
                part = src_dir[2 : len(src_dir) - 1]
                # find <javac srcdir="src_dir"/> and <javac srcdir="${scr.dir}"
                if part in props:
                    src_dirs.add(props[part])
                # <path id="source.path">
                #   <pathelement location="src"/>
                #   <pathelement location="src2"/>
                # </path>
                # <javac destdir="bin" srcdir="${source.path}" />
                if part not in path_elements:
                    continue
                for elem in path_elements[part]:
                    src_dirs.add(elem)
            else:
                src_dirs.add(src_dir)

            # <javac destdir="bin">
            #   <src path="src/main/java:src/common/java" />
            # </javac>
            for src in javac.iter('src'):
                path = src.attrib.get('path')
                if not path:
                    continue
                for element in path.split(':'):
                    src_dirs.add(element)
        return list(src_dirs)
