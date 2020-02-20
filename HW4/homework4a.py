import math
import matplotlib.pyplot as plt
import numpy as np

def Horner(x, coeffs):
    poly = coeffs[len(coeffs) - 1] #Initially define poly as the last element in the array
    for i in range(len(coeffs) - 2, -1, -1): poly = poly * x + coeffs[i]#Loop backwards from the 2nd to last array element to the first and the value of the polynomial using Horner's Rule
    return poly

def LeastSquares(x, y, power):
    matA = np.zeros((len(x), power + 1))
    matB = np.zeros((len(x), 1))
    for i in range(len(x)):
        matB[i][0] = y[i]
        for j in range(power + 1):
            matA[i][j] = (x[i]) ** j
    transMatA = np.transpose(matA)
    aTransDotA = np.dot(transMatA, matA)
    aTransDotB = np.dot(transMatA, matB)
    return np.linalg.solve(aTransDotA, aTransDotB)

def PlotLeastSquares(x, y, power, showpoints = True, npoints = 500):
    plt.title('Least Squares Curve Fitting of Degree {:d}'.format(power))
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')
    coefficients = LeastSquares(x,y,power)
    valuesX = np.linspace(min(x), max(x), npoints)
    valuesY = np.linspace(min(x), max(x), npoints)
    for i in range(len(valuesX)):
        valuesY[i] = Horner(valuesX[i], coefficients)
    if showpoints: plt.plot(x,y,'ro', label='Original Data')
    plt.plot(valuesX, valuesY, 'b', linewidth = 2, label = 'Power: ' + str(power))
    plt.legend()
    plt.show()
    return valuesX, valuesY

def main():
    x = np.array([.05, .11, .15, .31, .46, .52, .7, .74, .82, .98, 1.17])
    y = np.array([.956, 1.09, 1.332, .717, .771, .539, .378, .370, .306, .242, .104])

    powerOne = 1
    powerTwo = 3

    linCoeff = LeastSquares(x, y, powerOne)
    print('The coefficients for a linear fit is: ', end = '')
    print(np.transpose(linCoeff))
    xValuesOne, yValuesOne = PlotLeastSquares(x, y, powerOne)

    cubCoeff = LeastSquares(x, y, powerTwo)
    print('The coefficients for a cubic fit is: ', end = '')
    print(np.transpose(cubCoeff))
    xValuesTwo, yValuesTwo = PlotLeastSquares(x, y, powerTwo)
    
    plt.title('Combined Graphs')
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')    
    plt.plot(x, y, 'ro', label = 'Original Data')
    plt.plot(xValuesOne, yValuesOne, 'b', linewidth = 2, label='Power: ' + str(powerOne))
    plt.plot(xValuesTwo, yValuesTwo, 'g', linewidth = 2, label='Power: ' + str(powerTwo))
    plt.legend()
    plt.show()

main()
