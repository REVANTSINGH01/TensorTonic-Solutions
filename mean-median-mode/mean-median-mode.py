from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode = float(Counter(x).most_common(1)[0][0])
    dic = {
        "mean" : mean,
        "median" : median,
        "mode" : mode,
    }
    return dic
    # Write code here
    pass