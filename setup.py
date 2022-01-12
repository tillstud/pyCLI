try:  # for pip >= 20.0.2
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 20.0.2
    from pip._internal.download import PipSession  # type: ignore
    from pip._internal.req import parse_requirements

import os

from setuptools import find_packages, setup

from pyCLI import __version__

REQUIREMENTS = [
    req.requirement if hasattr(req, "requirement") else str(req.req)  # type: ignore
    for req in parse_requirements(
        os.path.join(os.path.dirname(__file__), "requirements.txt"),
        session=PipSession(),
    )
]

EXTRAS_REQUIRE = {
    "build": ["wheel", "twine"],
    "lint": ["flake8", "black", "mypy", "isort", "rope"],
    "sec": ["bandit", "safety", "pre-commit"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["build"] + EXTRAS_REQUIRE["lint"] + EXTRAS_REQUIRE["sec"]
)

URL = "https://github.com/tillstud/pyCLI"


def read(fname):
    """Read the content of the file `fname`."""
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="pyCLI",
    version=__version__,
    description="A template to structure your next CLI",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Till Studer",
    author_email="tillstud@gmail.com",
    url=URL,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    keywords="cli, template",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10.0",
    entry_points={"console_scripts": ["pyCLI=pyCLI.cli:cli"]},
)
