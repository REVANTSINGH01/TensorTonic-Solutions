import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    n=len(a)
    A=0
    for i in range(0,n):
        A+=a[i]**2
    A=math.sqrt(A)
    B=0
    for i in range(0,n):
        B+=b[i]**2
    B=math.sqrt(B)
    product=0
    for i in range(0,n):
        product+=a[i]*b[i]
    if A == 0 or B == 0:
        return 0.0
    return product/(A*B)
