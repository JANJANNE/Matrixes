def transpose_matrices(matrixA, matrixB):
    try:
        row_A = len(matrixA)
        column_A = len(matrixA[0])
        row_B = len(matrixB)
        column_B = len(matrixB[0])
        transposed_A = [[0 for _ in range(row_A)] for _ in range(column_A)]
        for i in range(row_A):
            for j in range(column_A):
                transposed_A[j][i] = matrixA[i][j]

        transposed_B = [[0 for _ in range(row_B)] for _ in range(column_B)]
        for i in range(row_B):
            for j in range(column_B):
                transposed_B[j][i] = matrixB[i][j]

        return transposed_A, transposed_B
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None