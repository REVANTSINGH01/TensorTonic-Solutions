import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    dict = {}
    x_vec = np.asarray(x)
    p_vec = np.asarray(p)
    pmf = np.asarray([])
    for i in range(len(x)):
        if x[i] == 0:
            pmf = np.append(pmf, 1-p)
        else:
            pmf = np.append(pmf, p)

    dict["pmf"] = pmf
    dict["mean"] = float(p)
    dict["variance"] = float(p*(1.0-p))

    return dict
    pass