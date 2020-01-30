from copy import *

def GaussElim(Aaug):
    ans = [0 for i in range(len(Aaug))] #Create an empty array to hold the solutions to the set of linear equations
    for i in range(1,len(Aaug)): #Loop for all rows after row 1 to begin reducing and eliminating elements in column 1
        tmp = Aaug[i][0] / Aaug[0][0] #Calculate the multiplier used to eliminate the other elements. This equation only works for eliminating the first column
        for j in range(len(Aaug[0])): Aaug[i][j] -= Aaug[0][j] * tmp #Run through all the columns in Aaug on row i and begin elimination by multiplying the element by the multiplier and subtracting the result from the original element
    for i in range(2, len(Aaug)): #Loop for all rows after row 2 to begin reducing and elimination elements between column 2 and the length of the matrix
        tmp = Aaug[i][i-(i-1)] / Aaug[i-(i-1)][i-(i-1)] #Calculate the multiplier used to eliminate the other elements. Unlike the above equation, this one works for any column from 2
        for j in range(1, len(Aaug[0])): Aaug[i][j] -= Aaug[i-(i-1)][j] * tmp  #Loop through all the columns in i after column 2 (column one should be all zeros besides row 1) and begin elimination by multiplying the element by the multiplier and subtracting the result from the original element
            
    for i in range(len(Aaug) - 1, -1, -1): #Loop backwards from the last row in Aaug to the first row to perform back substitution and solve for our independant variables
        tmpSum = 0 #Set / reset the temporary sum variable to 0 between rows
        for j in range(len(Aaug)): tmpSum += Aaug[i][j] * ans[j] #Loop through the columns in row i and calculate the sum to be subtracted from the "b" column in the matrix
        ans[i] = (Aaug[i][len(Aaug)] - tmpSum) / Aaug[i][i] #Subtract the previously calculated sum and solve for the unknown variable 

    return ans #Return the array of solutions


def main():
    MyA = [[4, -1, -1, 3],
           [-2, -3, 1, 9],
           [-1, 1, 7, -6]]
    
    anotherA = [[4, 3, 1, -1, 2],
                [2, -5, 0, -2, -3],
                [-3, 3, -6, 1, 5],
                [0, 1, 4, 8, -2]]

    #Pretty-print the solutions
    solution = GaussElim(deepcopy(MyA)) #Pass a copy of the desired matrix when we call GaussElim
    print('c) The solution to the set of linear equations in the augmented matrix:')  
    for i in MyA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    print(solution)

    solution = GaussElim(deepcopy(anotherA)) #Pass a copy of the desired matrix when we call GaussElim
    print('\n\n\nThe solution to the set of linear equations in the augmented matrix:') 
    for i in anotherA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    print(solution)
    
main()
