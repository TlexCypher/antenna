import os
import traceback
from logging import getLogger
from pathlib import Path

from antenna.config.build_xml import BuildXML
from antenna.exception.no_such_file import NoSuchFileException
from antenna.exception.unsupported_extension import (
    UnsupportedExrtensionException,
)
from antenna.parser.parser import Parser
from antenna.projector.classpath.classpath import ClassPathProjector
from antenna.projector.project.project import ProjectProjector

logger = getLogger(__name__)


class Antenna:
    def __init__(self) -> None:
        self.build_xml: BuildXML | None = None
        self.parser: Parser | None = None
        self.classpath_file: str | None = None
        self.project_file: str | None = None

    def is_xml(self, path: str) -> bool:
        return Path(path).suffix.lower() == '.xml'

    def up(self, path: str) -> None:
        try:
            if not os.path.exists(path) or not os.path.isfile(path):
                raise NoSuchFileException(f'No such file: {path}', path)
            if not self.is_xml(path):
                raise UnsupportedExrtensionException(
                    f'Unsupported Extension: {Path(path).suffix}',
                    Path(path).suffix,
                )

            self.build_xml = BuildXML(path)
            self.parser = Parser(self.build_xml)

            parsed = self.parser.parse()
            classpath_projector, _ = (
                ClassPathProjector(),
                ProjectProjector(),
            )
            logger.info(f'success to parse {self.build_xml}')

            classpath_projector.project(parsed)
            # project_projector.project(parsed)

            logger.info('success to create .classpath, and .project')

        except Exception:
            logger.error('failed to up antenna')
            traceback.print_exc()
            return None
