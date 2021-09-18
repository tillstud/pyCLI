[![GitHub license](https://img.shields.io/github/license/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/graphs/contributors)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/pulls)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/pulls)
[![GitHub issues](https://img.shields.io/github/issues/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/tillstud/python-sample-project-cli)](https://github.com/tillstud/python-sample-project-cli/issues?q=is%3Aissue+is%3Aclosed)

# tool-name
{{long desc.}}

## Background
{{short desc.}}

# Installation
1. clone the repo
`git clone https://github.com/tillstud/python-sample-project-cli.git`
2. install the dependencies
`pip install -r requirements.txt`

## Development
1. create a virtual environment
`python -m venv .venv`
2. activate the virtual environment
- Linux: `source ./.venv/bin/activate`
- Windows: `.venv\Scripts\activate`
> To deactivate the venv type `deactivate`
3. update pip
`python -m pip install --upgrade pip`
4. install the dev dependencies
`pip install -r requirements-dev.txt`
5. add the env variables to your venv
`export $(xargs < .env)`
6. update the versions in `.pre-commit-config.yml` and install them with `pre-commit install`

### Optional
1. Use [pyenv](https://github.com/pyenv/pyenv) to manage your python versions
