# IDS 706 Data Engineering Mini Project 2 [![CI](https://github.com/nogibjj/Gavin_Li_mini_project_2/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Gavin_Li_mini_project_2/actions/workflows/ci.yml)


This repo is for Duke MIDS IDS706 Data Engineering course. The environment was based on the first mini project. 

## Purpose of the template

The work in this repo includes descriptive statistical analysis on dataset [TITANIC from kaggle](https://www.kaggle.com/competitions/titanic/overview)

## The build process

### Install python packages

`make install`

calls the following commands

`pip install --upgrade pip && pip install -r requirements.txt`

### Test the code

`make test`

calls the following command

`python -m pytest -vv --cov=main test_*.py`

![TestResult](./resources/make_test.png)

### Lint the code

`make lint`

calls the following command

`pylint --disable=R,C --ignore-patterns=test_.*?py *.py`

![LintResult](./resources/make_lint.png)

## References

[Professor Noah's template](https://github.com/nogibjj/python-template)