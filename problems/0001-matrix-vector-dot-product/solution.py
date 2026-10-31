import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

    a = np.asarray(a)
    b = np.asarray(b)

    if a.ndim != 2 or b.ndim != 1:
        return -1

    if a.shape[1] != b.shape[0]:
        return -1

    return np.dot(a, b).tolist()