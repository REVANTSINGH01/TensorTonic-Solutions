import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n=len(x)
    mean=float(np.mean(x))
    sum=0
    for i in range(n):
        sum+=(x[i]-mean)**2

    variance=sum/(n-1)
    sd=math.sqrt(variance)
    dict={
        "variance":variance,
        "standard_deviation":sd
    }
    return dict
    # Write code here
    pass