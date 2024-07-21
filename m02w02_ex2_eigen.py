import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    if isinstance(matrix, np.ndarray) == False:
        matrix = np.array(matrix)
    eigenvalue, eigenvector = np.linalg.eig(matrix)
    return eigenvalue, eigenvector


def norm_eigenvctor(eigenvector):
    length = np.linalg.norm(eigenvector)
    return eigenvector/length


if __name__ == '__main__':
    matrix = [[5,3,2],[3,2,5],[9,6,2]]
    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix )
    print('eigenvalues:',eigenvalues)
    print()
    print('eigenvectors:',eigenvectors)
    print()
    print('normalise vector:',norm_eigenvctor(eigenvectors))
