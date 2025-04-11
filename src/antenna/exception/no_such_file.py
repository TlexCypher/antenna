class NoSuchFileException(Exception):
    def __init__(self, message: str, path: str) -> None:
        super().__init__(message)
        self.path = path
