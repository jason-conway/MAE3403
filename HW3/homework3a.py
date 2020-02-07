def MatrixTermProducts(Amatrix, Bmatrix):
    returnArray = [[0] * len(Amatrix[0]) for i in range(len(Amatrix))]
    for i in range(len(Amatrix)):
        for j in range(len(Amatrix[0])):
            returnArray[i][j] = Amatrix[i][j] * Bmatrix[i][j]
    return returnArray
    
def main():
    matrix1 = [[1, -5, 3, -7],
               [2, 5, 11, -2],
               [13, -1, 0, 4]]
    matrix2 = [[5, 0, 1, 4],
               [4, 3, 2, 1],
               [1, 2, 3, 4]]

    answer = MatrixTermProducts(matrix1, matrix2)
    print(answer)

main()