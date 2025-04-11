class UnsupportedExrtensionException(Exception):
    def __init__(self, message: str, ext: str):
        super().__init__(message)
        self.ext = ext
