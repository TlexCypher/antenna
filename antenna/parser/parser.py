from antenna.config.build_xml import BuildXML
from antenna.parser.parse_result import ParseResult


class Parser:
    def __init__(self, build_xml: BuildXML): 
        self.build_xml = build_xml

    def parse(self) -> ParseResult:
        return ParseResult()
