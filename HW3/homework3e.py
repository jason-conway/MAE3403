def ColumnWithLargestSum(matrix):
    colsum, colnumber = -9999, -1 #Initialize colsum with a really small value and colnumber with an impossible value to compare against
    for i in range(len(matrix[0])): #Loop through the columns in the matrix
        tempSum = 0 #Reset a temporary variable to sum the column elemnts with
        for j in range(len(matrix)): #Loop through the rows of the matrix
            tempSum += matrix[j][i] #Add the current column element to the temporary sum
            if tempSum > colsum: colsum, colnumber = tempSum, i #Update what the biggest sum is and the largest column if tempSum was greater than the previous large value
    return colnumber, colsum

def main():
    Amatrix = [[3, 2, 5, 2, 3],
               [2, -1, 4, 5, 1],
               [1, 8, 3, 1.3, 2]]
    Bmatrix = [[2, 1, 4],
               [3, 2, 5],
               [4, 2, 1],
               [1, 5, 2],
               [3, 1, 1]]

    colnumber, colsum = ColumnWithLargestSum(Amatrix)
    print('The largest sum is located in column {:d} and equals {:.2f}'.format(colnumber, colsum))
    
    colnumber, colsum = ColumnWithLargestSum(Bmatrix)
    print('The largest sum is located in column {:d} and equals {:.2f}'.format(colnumber, colsum))

main()