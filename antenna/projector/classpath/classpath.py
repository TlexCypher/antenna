from antenna.parser.parse_result import ParseResult
from antenna.projector.projector import Projector


class ClassPathProjector(Projector):
    def __init__(self) -> None:
        pass

    def project(self, parsed: ParseResult) -> str:
        raise NotImplementedError()
