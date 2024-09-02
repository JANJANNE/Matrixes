def multiplying_matrices(matrixA, matrixB):
    row_A = len(matrixA)
    column_A = len(matrixA[0])
    row_B = len(matrixB)
    column_B = len(matrixB[0])

    if column_A != row_B:
        raise ValueError("The number of columns in matrix_A must equal the number of rows in matrix_B.")
    result = [[0 for _ in range(column_B)] for _ in range(row_A)]

    for i in range(row_A):
        for j in range(column_B):
            for k in range(column_A):
                result[i][j] += int(matrixA[i][k]) * int(matrixB[k][j])

    return result