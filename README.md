# pycausal_dai
[![Tests](https://github.com/daihuanlin/pycausal_dai/workflows/Tests/badge.svg)](https://github.com/daihuanlin/pycausal_dai/actions)
[![PyPI version](https://badge.fury.io/py/pycausal_dai.svg)](https://pypi.org/project/pycausal_dai/)

A Python package for causal inference methods including ATE estimation, propensity scores, and meta-learners.

## Features

- Estimation of Average Treatment Effect (ATE)  
- Propensity score calculation and balancing  
- Support for meta-learner methods  
- Easy-to-use Python API  

## Installation

```bash
pip install pycausal-dai
```
or, to directly install from source,
```bash
git clone https://github.com/HuanlinDai/pycausal_dai.git
cd pycausal_dai
pip install .
```

## Getting Started

from pycausal_dai import ...  # import the module(s) you need
# Example usage:
#   - load your data (features, treatment, outcome)
#   - compute propensity scores or apply meta-learner
#   - estimate ATE or other causal quantities


## License

This project is licensed under the MIT License.