# Mutant lambda

It is a project developed in Python that is responsible for creating a matrix which determines whether the entered dan is a human or a mutant. It also stores the information using dynamo db, consults the stored data and performs the calculations of the stored data.


## Table of Contents

- [Installation](#installation)
- [Test](#test)

### Installation

* `git clone git clone github.com:wendymantilla/bass-mutant.git` this repository


## Test

$ pytest
If you have python version 3.10, this comonado runs
$ python3.10 -m pytest

## Api Rest

The consumption of the lambda is done through a Rest api, these are its url:
- Metodo post https://odflfss7yb.execute-api.us-east-2.amazonaws.com/dev/isMutant 
- Metodo get  https://odflfss7yb.execute-api.us-east-2.amazonaws.com/dev/report




