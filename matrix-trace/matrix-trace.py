import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    sum=0
    n=len(A)
    for i in range(n):
        sum+=A[i][i]
    return sum
    pass