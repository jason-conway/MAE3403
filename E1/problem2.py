def combineOnDiagonal(matrix1, matrix2):
      columns, rows = len(matrix1[0]) + len(matrix2[0]), len(matrix1) + len(matrix2)
      newArray = [[0] * columns for i in range(rows)]
      for i in range(len(matrix1)):
            for j in range(len(matrix1[0])): newArray[i][j] = matrix1[i][j]
      for i in range(len(matrix2)):
            for j in range(len(matrix2[0])): newArray[i + len(matrix1)][j + len(matrix1[0])] = matrix2[i][j]
      return newArray

def main():
      m1 = [[1, 2, 3],
            [4, 5, 6]]

      m2 = [[5, 4, 3, 2, 1],
            [3, 4, 5, 6, 7],
            [9, 8, 7, 6, 5]]

      m3 = [[1, 2],
            [3, 4],
            [5, 6]]

      answer = combineOnDiagonal(m1, m2)
      print(answer)
      answer = combineOnDiagonal(m2, m3)
      print(answer)

main()