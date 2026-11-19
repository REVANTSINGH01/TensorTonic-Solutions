import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    n=len(x)
    weight_sum=0
    for i in range(n):
        weight_sum+=float(x[i]*p[i])
    return weight_sum
    pass