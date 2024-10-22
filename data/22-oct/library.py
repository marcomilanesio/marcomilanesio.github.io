import math
import numpy as np

def is_perfect_square(a):
    """
    True if a is a perfect square.
    @param a: int
    @return bool
    """
    return math.sqrt(a) ** 2 == a

def gcd(a,b):
    """
    Compute the Greatest Common Divisor between
    two integers.
    @param a, b: int
    @return int
    """
    while b:
        a, b = b, a % b
    return a

def are_arrays_equal(a, b, threshold=None):
    """
    Checks if two numpy array are equal to a certain threshold
    @param a, b: numpy array
    @param threshold: float
    @return bool
    """
    if not threshold:
        return np.array_equal(a,b)
    else:
        return np.allclose(a,b,threshold)
