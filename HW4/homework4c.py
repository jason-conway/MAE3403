import math
import matplotlib.pyplot as plt
import numpy as np

#Methodology and extra information pulled from https://en.wikipedia.org/wiki/Determinant#Laplace's_formula_and_the_adjugate_matrix
def Cramer(A, b):
    solution = np.zeros((len(b), 1))
    aMod = np.zeros((len(A), len(A[0]), len(b))) #Create 3d matrix to hold the modified A matrixes
    for i in range(len(A[0])): #Loop through the columns in matrix A
        aMod[i] = np.copy(A) #Put a fresh copy of matrix A into the current element of aMod
        aMod[i][:,i] = b #Replace the current column of A with B
        solution[i] =  Determinant(aMod[i]) / Determinant(A) #Calculate the solution using Cramer's Rule
    return solution

def Determinant(A):
    if A.shape[0] == 2: return A[0][0] * A[1][1] - A[0][1] * A[1][0] #If A is a 2x2 matrix, take the easy determinant
    det = 0 #Create placeholder variable to hold the determinant as we calculate it
    for k in range(A.shape[0]): det += (-1)**(k + 1) * A[1][k] * Determinant(Submatrix(A, 1, k)) #Use Laplace's formula to recursively find the determinant of A
    return det #Return the determinant 
    
def Submatrix(A, j, k):
    return np.delete(np.delete(np.copy(A), j, axis = 0), k, axis = 1) ##Create a copy of A and remove row j then remove column k and return the new matrix

def main():
    A = np.array([[1, -2, 3, 4], [5, 6, 7, 8], [-9, 10, -11, 6], [5, 4, -3, 2]]) 
    b = np.array([1, 2, 3, 4])
    print(Submatrix(A, 1, 2))
    print("\n", Determinant(A))
    print("\n", Cramer(A, b))
    
    A = np.array([[-5, 1, -5, 0, 1, -4], [5, 0, 3, 5, 3, 5], [-2, -2, 1, 4, 3, -5], [4, 5, 0, 3, 4, -1], [-5, -2, -5, 5, -2, -2], [4, 5, 5, 0, 0, -2]])
    b = np.array([-95, -45, 49, -50, 90, 30]) 
    print("\n", Submatrix(A, 1, 2)) 
    print("\n", Determinant(A))
    print("\n", Cramer(A, b))

if __name__ == "__main__": 
    main()