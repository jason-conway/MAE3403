from copy import *

def GaussElim(Aaug):
    ans = [0 for i in range(len(Aaug))] #Create an empty array to hold the solutions to the set of linear equations
    for i in range(len(Aaug)): #I use this index to keep track of the offset when calculating multipliers and eliminating elements
        for j in range(i + 1, len(Aaug)): #Loop through all rows beginning with row 2 in order to begin reducing and elimination elements
            tmp = Aaug[j][j - (j - i)] / Aaug[j - (j - i)][j - (j - i)] #Calculate the multiplier needed to eliminate the next non-zero element. Offsets from the primary for loop are used to keep track of how far right we've travelled
            for k in range(i, len(Aaug[0])): Aaug[j][k] -= Aaug[j - (j - i)][k] * tmp  #Loop though all the columns starting with the left-most un-eliminated column and begin eliminate or reduce it by multiplying the element by the multiplier and subtracting the result from the original element
    for i in range(len(Aaug) - 1, -1, -1): #Loop backwards from the last row in Aaug to the first row to perform back substitution and solve for our independant variables
        tmpSum = 0 #Set / reset the temporary sum variable to 0 between rows
        for j in range(len(Aaug)): tmpSum += Aaug[i][j] * ans[j] #Loop through the columns in row i and calculate the sum to be subtracted from the "b" column in the matrix
        ans[i] = (Aaug[i][len(Aaug)] - tmpSum) / Aaug[i][i] #Subtract the previously calculated sum and solve for the unknown variable and save it in an array to be returned after all completing back substitution
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
    solution = GaussElim(deepcopy(MyA)) #Pass a copy of the desired matrix when we call GaussElim to keep it intact
    print('c) The solution to the set of linear equations in the augmented matrix:')  
    for i in MyA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    for i in range(len(solution)): print('{:.4f}'.format(solution[i]), end =" ") #Print out the solutions with only 4 points of precision

    solution = GaussElim(deepcopy(anotherA)) #Pass a copy of the desired matrix when we call GaussElim
    print('\n\n\nThe solution to the set of linear equations in the augmented matrix:') 
    for i in anotherA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    for i in range(len(solution)): print('{:.4f}'.format(solution[i]), end =" ") #Print out the solutions with only 4 points of precision
    
main()
