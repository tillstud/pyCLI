[![GitHub license](https://img.shields.io/github/license/tillstud/spotirss)](https://github.com/tillstud/spotirss/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/tillstud/spotirss)](https://github.com/tillstud/spotirss/graphs/contributors)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/tillstud/spotirss)](https://github.com/tillstud/spotirss/pulls)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/tillstud/spotirss)](https://github.com/tillstud/spotirss/pulls)
[![GitHub issues](https://img.shields.io/github/issues/tillstud/spotirss)](https://github.com/tillstud/spotirss/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/tillstud/spotirss)](https://github.com/tillstud/spotirss/issues?q=is%3Aissue+is%3Aclosed)

# spotirss
{{long desc.}}

## Background
{{short desc.}}

# Installation
1. clone the repo
`git clone https://github.com/tillstud/spotirss.git`
2. install the dependencies
`pip install -r requirements.txt`

## For development
1. create a virtual environment
`python -m venv .venv`
2. activate the virtual environment
- Windows: `.venv\Scripts\activate`
- Linux: `source ./.venv/bin/activate`
> To deactivate the venv type `deactivate`
3. update pip
`python -m pip install --upgrade pip`
4. install the dev dependencies
`pip install -r requirements-dev.txt`
5. add the env variables to your venv
`export $(xargs < .env)`

### Optional
1. Use [pyenv](https://github.com/pyenv/pyenv) to manage your python versions
