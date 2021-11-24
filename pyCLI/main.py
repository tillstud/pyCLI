from pyCLI.config import Config
from pyCLI.logging import logger


def main(config: Config):
    print(config.pycli_message)
    logger.debug("If you enter 'pyCLI -v', you will see this message!")
