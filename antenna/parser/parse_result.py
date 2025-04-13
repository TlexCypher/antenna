class ParseResult:
    def __init__(self, src_kind: list[str]) -> None:
        self.__src_kind = src_kind

    def src_kind(self) -> list[str]:
        return self.__src_kind
