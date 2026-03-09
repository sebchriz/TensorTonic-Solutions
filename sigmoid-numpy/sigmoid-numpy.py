import numpy as np
def sigmoid(x):
    sigma = 1/(1+(1/np.exp(x)))
    return sigma
    