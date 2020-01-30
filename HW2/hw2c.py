def GaussSeidel(Aaug, x, Niter):
    for i in range(Niter): #Loop for however many iterations are specified
        for j in range(len(Aaug)): #Loop for each row in the augmented matrix to solve for x[1] x[2] and x[3]
            rightSide = Aaug[j][len(Aaug)] #Set rightSide to the corresponding "b" (answer) element in the augmented matrix
            for k in range(len(Aaug)): #Loop for every column in the augmented matrix
                rightSide -= Aaug[j][k] * x[k] if j != k else 0 #Subtract every element from the "left side" except for the element we are solving for
            x[j] = rightSide / Aaug[j][j] #Finally solve for the specific element by dividing by the coefficient at the corresponding index
    return x #Return an array with the solutions

def main():
    MyA = [[4, -1, -1, 3],
           [-2, -3, 1, 9],
           [-1, 1, 7, -6]]
    initialGuessA = [0, 0, 0]
    
    anotherA = [[4, 3, 1, -1, 2],
                [2, -5, 0, -2, -3],
                [-3, 3, -6, 1, 5],
                [0, 1, 4, 8, -2]]
    initialGuessB = [0, 0, 0, 0]

    solution = GaussSeidel(MyA, initialGuessA, 22) #Call GaussSeidel with args for our augmented matrix, initial guess, and number of iterations

    '''
        I wanted to nicely display the matrix and corresponding solutions, which is a messy task without numpy...
        Sure, I could just print(solution) but if this were somehow running on an embedded system and I started writing floats 
        to stdout with 20 points of precision, I'd likely overflow a buffer or cause other issues-
        So here is a quick and dirty method of displaying our inital augmented array and subsequent solution:
    '''

    print('c) The solution to the set of linear equations:\n') 
    for i in MyA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    for i in range(len(solution)): print('{:.3f}'.format(solution[i]), end =" ") #Print out the solutions with only 3 points of precision
    
    #And once more:
    solution = GaussSeidel(anotherA, initialGuessB, 3) #Call GaussSeidel with args for our augmented matrix, initial guess, and number of iterations

    print('\n\n\nThe solution to the set of linear equations:\n')
    for i in anotherA: print(*i) #Loop through the rows in the augmented matrix and print them nicely
    print('\nis: ', end = " ")
    for i in range(len(solution)): print('{:.3f}'.format(solution[i]), end =" ") #Print out the solutions with only 3 points of precision

main()