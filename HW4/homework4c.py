import math
import matplotlib.pyplot as plt
import numpy as np

def Cramer(A, b):

def Determinant(A):

def Submatrix(A, j, k):


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

main()