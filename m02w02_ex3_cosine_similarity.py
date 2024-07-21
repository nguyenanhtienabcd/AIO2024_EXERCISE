import numpy as np


def compute_cosin_simlarity(matrix_a, matrix_b):
    if isinstance(matrix_a, np.ndarray) == False:
        matrix_a = np.array(matrix_a)
    if isinstance(matrix_b, np.ndarray) == False:
        matrix_b = np.array(matrix_b)
    matrix_a = matrix_a.flatten()
    matrix_b = matrix_b.flatten()
    numerator = np.dot(matrix_a, matrix_b)
    denominator = np.linalg.norm(matrix_a) * np.linalg.norm(matrix_b)
    return numerator/denominator


if __name__ == '__main__':
    a = [[2, 3, 4], [2, 4, 3], [10, 20, 30]]
    b = [[1, 2, 3], [4, 5, 6], [9, 8, 7]]
    print('cosine similarity:', compute_cosin_simlarity(a, b))
