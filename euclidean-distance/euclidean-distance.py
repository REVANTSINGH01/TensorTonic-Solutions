import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    dist=0
    n=len(x)
    for i in range(n):
        dist+=(x[i]-y[i])**2
    return math.sqrt(dist)
    pass