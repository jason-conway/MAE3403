from math import *

def MagVectorDiff(vector1, vector2):
    elementSum = 0 #Initialize variable to hold the squared difference of the elements in the vectors
    for i in range(len(vector1)): elementSum += (vector1[i] - vector2[i]) ** 2 #Find the difference of each element in the vectors and square it, then add the value to element sum
    return sqrt(elementSum) #Return the square root of elementSum, which is the magnitiude of the difference of the vectors

def main():
    A = [2, 1, 5, 9]
    B = [1, 2, 7, 5]
    C = [1.5, 3, 4, 7, 3]
    D = [2, 4.2, 4, 6, 3]

    ans = MagVectorDiff(A, B)
    print('Magnitude of the vector difference is: {:.2f}'.format(ans))

    ans = MagVectorDiff(C, D)
    print('Magnitude of the vector difference is: {:.2f}'.format(ans))
main()