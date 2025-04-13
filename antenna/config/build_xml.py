class BuildXML:
    def __init__(self, path: str) -> None:
        self.path = path

    def ext(self) -> str:
        return 'xml'

    def get_path(self) -> str:
        return self.path
