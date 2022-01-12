[![GitHub license](https://img.shields.io/github/license/tillstud/pyCLI)](https://github.com/tillstud/pyCLI/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/tillstud/pyCLI)](https://github.com/tillstud/pyCLI/graphs/contributors)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/tillstud/pyCLI)](https://github.com/tillstud/pyCLI/pulls)
[![GitHub issues](https://img.shields.io/github/issues/tillstud/pyCLI)](https://github.com/tillstud/pyCLI/issues)

# pyCLI

`pyCLI` is a template project to structure your next CLI!

## Usage

`pyCLI` is a command line tool, which can be used like this:

```plaintext
Usage: pyCLI [OPTIONS]

  INSERT SHORT DESCRIPTION WHAT THE CLI DOES HERE

Options:
  --version             Show the version and exit.
  -v, --verbose         Increase log verbosity
  --ca-bundle TEXT      The default certificate bundle.  [default:
                        /etc/ssl/certs/ca-certificates.crt]
  --pycli-message TEXT  The message which will be printed to the shell.
                        [default: Ciao]
  -h, --help            Show this message and exit.
```

## Configuration

`pyCLI` can read all of its command line parameters from environment variables (but **not** from a `.env` file).

The format of the environment variable names can be directly derived from the parameter's name, e.g.:

`--pycli-message` -> `PYCLI_MESSAGE`

In case one doesn't want to export the environment variables one by one, it can be convenient to put all the variables in a `.env` file and export them like this:

`export $(xargs < .env)`

This will grab all the environment variables from the `.env` file and export them in the current shell.
> In case you modify anything in your `.env` file don't forget to re-export the values, as they won't be picked up automatically.

`pyCLI` will prioritize command line options. If none are given it will first check for environment variables and if those aren't given either the default value is used.

## Installation

```bash
pip install pyCLI
```

## Contribute

Please do contribute! Issues and pull requests are very welcome!

Thank you already in advance for your help improving this CLI template!

### Development

1. Clone the repository

```bash
git clone https://github.com/tillstud/pyCLI
```

2. Create and activate a virtual environment

```bash
python3 -m venv venv
source ./venv/bin/activate
```

> To deactivate the venv type `deactivate` in your shell

3. Install the package in editable mode with the dev requirements

```bash
pip install -e .["dev"]
```

> This will also install the related build and publish packages, not just the packages for development.

4. Update the versions in `.pre-commit-config.yml` and install the pre-commit script

```bash
pre-commit autoupdate
pre-commit install
```

5. Set your shell variables

```bash
export $(xargs < .env)
```

#### Optional

I can recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your local python versions.
