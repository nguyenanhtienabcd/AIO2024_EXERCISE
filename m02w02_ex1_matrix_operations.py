import numpy as np

# 1. Matrix operations


def compute_vector_length(vector):
    if isinstance(vector, np.ndarray) == False:
        vector = np.array(vector)
    length = np.sqrt(sum(vector**2))
    return length


def compute_dot_product(vector_a, vector_b):
    if isinstance(vector_a, np.ndarray) == False:
        vector_a = np.array(vector_a)
    if isinstance(vector_b, np.ndarray) == False:
        vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b)


def mtrx_multi_vector(matrix, vector):
    if isinstance(matrix, np.ndarray) == False:
        matrix = np.array(matrix)
    if isinstance(vector, np.ndarray) == False:
        vector = np.array(vector)

    return np.dot(matrix, vector)


def mtrx_multi_mtrx(matrix_a, matrix_b):
    if isinstance(matrix_a, np.ndarray) == False:
        matrix_a = np.array(matrix_a)
    if isinstance(matrix_b, np.ndarray) == False:
        matrix_b = np.array(matrix_b)

    return np.dot(matrix_a, matrix_b)


def compute_inverse_mtrx(matrix):
    if isinstance(matrix, np.ndarray) == False:
        matrix = np.array(matrix)
    det = np.linalg.det(matrix)
    if det == 0:
        print(" determinant = 0, need to check the matrix ")
        return None
    else:
        return np.linalg.inv(matrix)


if __name__ == '__main__':
    vector_a = [3, 4]
    vector_b = [1, 2]
    matrix_a = [[5, 6], [7, 8]]
    matrix_b = [[9, 10], [11, 12]]

    print('length_a:', compute_vector_length(vector_a))
    print('vector and vector:', compute_dot_product(vector_a, vector_b))
    print('matrix and vector:', mtrx_multi_vector(matrix_a, vector_a))
    print('matrix and matrix:', mtrx_multi_mtrx(matrix_a, matrix_b))
    print('inverse matrix:', compute_inverse_mtrx(matrix_a))
