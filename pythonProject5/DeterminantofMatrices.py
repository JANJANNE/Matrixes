import numpy as np
def determinant_matrices(matrixA, matrixB):
    np_matrixA = np.array(matrixA, dtype=float)
    np_matrixB = np.array(matrixB, dtype=float)

    det_matrixA = np.linalg.det(np_matrixA)
    det_matrixB = np.linalg.det(np_matrixB)
    return det_matrixA, det_matrixB