import logging
import traceback

import click

from pyCLI import __version__
from pyCLI.config import Config
from pyCLI.errors import pyCLIError
from pyCLI.logging import logger
from pyCLI.main import main


@click.command(
    context_settings={
        "help_option_names": ["-h", "--help"],
    }
)
@click.version_option(message="%(prog)s v%(version)s", version=__version__)
@click.option(
    "-v",
    "--verbose",
    default=False,
    help="Increase log verbosity",
    is_flag=True,
)
@click.option(
    "--ca-bundle",
    default="/etc/ssl/certs/ca-certificates.crt",
    help="The default certificate bundle.",
    envvar="REQUESTS_CA_BUNDLE",
    show_default=True,
)
@click.option(
    "--pycli-message",
    type=str,
    default="Ciao",
    help="The message which will be printed to the shell.",
    envvar="PYCLI_MESSAGE",
    show_default=True,
)

def cli(
    verbose: bool,
    ca_bundle: str,
    pycli_message: str,
):
    """INSERT SHORT DESCRIPTION WHAT THE CLI DOES HERE"""

    if verbose:
        logger.setLevel(logging.DEBUG)

    try:
        config = Config(
            ca_bundle=ca_bundle,
            pycli_message=pycli_message,
        )
        main(config)
    except pyCLIError as err:
        logger.error(str(err))
    except Exception as err:
        logger.error(str(err))
