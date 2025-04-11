from logging import getLogger
from pathlib import Path
import os

from antenna.config.build_xml import BuildXML
from antenna.exception.no_such_file import NoSuchFileException
from antenna.exception.unsupported_extension import UnsupportedExrtensionException
from antenna.parser.parser import Parser
from antenna.projector.classpath.classpath import ClassPathProjector
from antenna.projector.project.project import ProjectProjector


logger = getLogger(__name__)


class Antenna:
    def __init__(self) -> None:
        self.build_xml = None
        self.parser = None
        self.classpath_file = None
        self.project_file = None

    def is_xml(self, path: str) -> bool:
        return Path(path).suffix.lower() == "xml"

    def up(self, path) -> tuple[str, str] | None:
        try:
            if not os.path.exists(path) or not os.path.isfile(path):
                raise NoSuchFileException(f"No such file: {path}", path)
            if not self.is_xml(path):
                raise UnsupportedExrtensionException(
                    f"Unsupported Extension: {Path(path).suffix}",
                    Path(path).suffix,
                )

            self.build_xml = BuildXML(path)
            self.parser = Parser(self.build_xml)

            parsed = self.parser.parse()
            classpath_projector, project_projector = (
                ClassPathProjector(),
                ProjectProjector(),
            )
            logger.info(f"success to parse {self.build_xml}")
            self.classpath_file = classpath_projector.project(parsed)
            self.project_file = project_projector.project(parsed)

            logger.info(
                f"success to create {self.classpath_file}, and {self.project_file}"
            )
            return self.classpath_file, self.project_file

        except Exception:
            logger.error("failed to up antenna")
