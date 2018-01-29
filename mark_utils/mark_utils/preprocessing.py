
def torch(x):
    import torch
    """
        Preprocessing the x data with zero meand and unitary variance
        Arguments:
                    x -- numpy ndarray
        Returns:
                    standardize -- data standardize (torch Tensor)
    """
    x = torch.from_numpy(x)
    standardize = (torch.div(x - torch.mean(x, 0), torch.std(x, 0)))
    return standardize


def numpy(x, besse_correction=True):
    import numpy as np
    """
        Preprocessing the x data with zero meand and unitary variance
        Arguments:
                    x -- numpy ndarray
        Returns:
                    standardize -- data standardize (numpy ndarray)
    """
    if besse_correction:
        standardize = (x - np.mean(x, 0)) / np.std(x, 0, ddof=1)
    else:
        standardize = (x - np.mean(x, 0)) / np.std(x, 0)

    return standardize
