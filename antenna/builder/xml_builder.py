from logging import getLogger
from xml.etree import ElementTree as ET

logger = getLogger(__name__)


class XMLBuilder:
    def __init__(self, root: ET.Element) -> None:
        self.tree: ET.ElementTree | None = None
        self.root = root

    def add(
        self,
        parent: ET.Element,
        sub_element_name: str,
        attr: dict[str, str] | None = None,
        value: str | None = None,
    ) -> ET.Element:
        sub_element = ET.SubElement(parent, sub_element_name)
        if attr:
            for key, value in attr.items():
                sub_element.set(key, value)
        sub_element.text = value
        return sub_element

    def build(
        self,
        output: str,
        encoding: str = 'utf-8',
        xml_declaration: bool = True,
    ) -> None:
        # pretty print
        ET.indent(self.root, space='  ')
        self.tree = ET.ElementTree(self.root)
        if not self.tree:
            logger.error(
                f'failed to write {output}, becuase xml.element.ElementTree object is None'
            )
            return
        self.tree.write(output, encoding, xml_declaration)
        logger.info(
            f'success to serialize xml.element.ElementTree object into {output}'
        )
