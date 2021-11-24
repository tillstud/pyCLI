import logging
from time import gmtime


class LogFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(
            fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.converter = gmtime


default_handler = logging.StreamHandler()
default_handler.setFormatter(LogFormatter())

logging.basicConfig(handlers=[default_handler])

logger = logging.getLogger("pyCLI")
logger.setLevel(logging.INFO)
