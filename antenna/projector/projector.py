from abc import ABC, abstractmethod

from antenna.parser.parse_result import ParseResult


class Projector(ABC):
    @abstractmethod
    def project(self, parsed: ParseResult) -> None:
        pass
