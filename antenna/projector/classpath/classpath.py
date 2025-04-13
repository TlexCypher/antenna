from xml.etree import ElementTree as ET

from antenna.builder.xml_builder import XMLBuilder
from antenna.parser.parse_result import ParseResult
from antenna.projector.projector import Projector


class ClassPathProjector(Projector):
    def __init__(self) -> None:
        self.projected_path = '.classpath'

    def project(self, parsed: ParseResult) -> None:
        root = ET.Element('classpath')
        xml_builder = XMLBuilder(root)

        for src_kind in parsed.src_kind():
            xml_builder.add(
                root, 'classpathentry', {'kind': 'src', 'path': src_kind}
            )
        return xml_builder.build(self.projected_path)
