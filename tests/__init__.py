"""PyCausal Dai - Causal Inference Toolkit"""

__version__ = "0.1.0"

# Import key functions for easy access
from pycausal_dai.rct import calculate_ate_ci, calculate_ate_pvalue
from pycausal_dai.propensity import ipw, doubly_robust
from pycausal_dai.meta_learners import (
    s_learner_discrete,
    t_learner_discrete,
    x_learner_discrete,
    double_ml_cate
)

__all__ = [
    "calculate_ate_ci",
    "calculate_ate_pvalue",
    "ipw",
    "doubly_robust",
    "s_learner_discrete",
    "t_learner_discrete",
    "x_learner_discrete",
    "double_ml_cate",
]