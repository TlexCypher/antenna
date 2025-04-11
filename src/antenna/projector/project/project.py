from antenna.parser.parse_result import ParseResult
from antenna.projector.projector import Projector


class ProjectProjector(Projector):
    def __init__(self) -> None:
        pass

    def project(self, parsed: ParseResult) -> str:
        return super().project(parsed)
