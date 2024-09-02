def adding_matrices(matrixA, matrixB):
    matrixAdd = []
    for i in range(len(matrixA)):
        rowadd = []
        for j in range(len(matrixA[0])):
            element_add = int(matrixA[i][j]) + int(matrixB[i][j])
            rowadd.append(element_add)
        matrixAdd.append(rowadd)
    return matrixAdd
