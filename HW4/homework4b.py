import math
import matplotlib.pyplot as plt
import numpy as np

#Methodology pulled from https://en.wikipedia.org/wiki/Spline_interpolation
def CubicSpline(x, y, slope1 = 0, slope2 = 0):
    xDiff, yDiff = np.diff(x), np.diff(y)  #Create array holding the difference between adjacent values in the x and y array
    divSpacing = yDiff / xDiff #Create array holding the ratio between the x and y array differences
    neighboringDiagMatA = xDiff[1 : (len(x) - 1) - 1] ** -1 #Calculate the values to be occupied above and below the diagonal in matrix A. We are creating the diagonal linear equation system piece by piece
    diagMatA = 2 * (1 / xDiff[: (len(x) - 1) - 1] + 1 / xDiff[1 :]) #Calculate the values to occupy the diagonal in matrix A
    matA = np.diag(neighboringDiagMatA, -1) + np.diag(diagMatA, 0) + np.diag(neighboringDiagMatA, +1) #Create matrix A with the appropriate offsets and values we calculated
    matB = 3 * (divSpacing[1 :] / xDiff[1 :] + divSpacing[: (len(x) - 1) - 1] / xDiff[: (len(x) - 1) - 1]) #Create matrix B containing "solutions" to the set of equations
    return np.hstack([slope1, np.linalg.solve(matA, matB), slope2]) #Return the coefficients, which are the solutions to the set of equations bounded by the argument-provided slopes
    
def PlotCubicSpline(x, y, slope1 = 0, slope2 = 0 , showpoints = True, npoints = 500):
    xDiff, yDiff = np.diff(x), np.diff(y)  #Create array holding the difference between adjacent values in the x and y array
    divSpacing = yDiff / xDiff #Create array holding the ratio between the x and y array differences
    coefficients = CubicSpline(x,y) #Pass the x and y arrays to CubicSpline to calculate the coefficients of the spline
    alpha = (3 * divSpacing - coefficients[1 :] - 2 * coefficients[: (len(x) - 1)]) / xDiff #Create the last two arrays of values needed to solve for the y values
    beta = (coefficients[: (len(x) - 1)] + coefficients[1 :] - 2 * divSpacing) / (xDiff ** 2)
    valuesX, valuesY = np.linspace(min(x), max(x), npoints), [] #Create npoints evenly divided x points to calculate y for, and a placeholder array for the y values
    for i in valuesX: #Loop through all the values in the x array
        for j in range(len(x) - 1): #Loop through the values in the x array
            if ((i >= x[j]) & (i <= x[j + 1])):
                tempY = y[j] + coefficients[j] * (i - x[j]) + alpha[j] * ((i - x[j]) ** 2) + beta[j] * ((i - x[j]) ** 3) #Solve for the current value of y with the coefficients
                valuesY.append(tempY) #Add the calculated value of y in the valuesY array
    '''
    It's plotting time
    '''

    plt.title('Cubic Spine') #Add a title and lable the axis for the plot
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')
    if showpoints: plt.plot(x,y,'ro', label='Original Data') #Plot original data if indicated
    plt.plot(valuesX, valuesY, 'b', linewidth = 2, label = 'Splines') #Add the x values and calculated y values
    plt.legend()
    plt.show()

def main():
    x = np.array([1.5, 3, 4.5, 6, 7.5, 9])
    y = np.array([3.5, 1.5, -2, 6.9, 8.2 ,1.5]) 
    slope1 = 2
    slope2 = -4
    coefficients = CubicSpline(x,y,slope1, slope2) #Pass the x and y arrays, along with the boundary slopes to CubicSpline to calculate the coefficients of the spline
    print('The coefficients of the spline are: ', end = '')
    print(coefficients)
    PlotCubicSpline(x, y, slope1, slope2) #Call PlotCubicSpline to calculate the needed values and display the plot

if __name__ == "__main__":
    main()