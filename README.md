# Mutant lambda

It is a project developed in Python that is responsible for creating a matrix which determines whether the entered dan is a human or a mutant. It also stores the information using dynamo db, consults the stored data and performs the calculations of the stored data.


## Table of Contents

- [Installation](#installation)
- [Test](#test)

### Installation

* `git clone git clone github.com:wendymantilla/bass-mutant.git` this repository


You will need to run:

```bash
pip install
```

## Test

```bash
$ pytest
```
### Unit Test Coverage

```bash
$ pytest
```

### Run with jobs

```bash
python main.py --job=dummy
```

## Code Style & Quality Checker

```bash
$ flake8 .

$ black .

$ pylint $module_folder
```

## Api Rest

The consumption of the lambda is done through a Rest api, these are its url:
- [Metodo post https://odflfss7yb.execute-api.us-east-2.amazonaws.com/dev/isMutant ]
- [Metodo get  https://odflfss7yb.execute-api.us-east-2.amazonaws.com/dev/report]




