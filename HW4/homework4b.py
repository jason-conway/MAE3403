import math
import matplotlib.pyplot as plt
import numpy as np

def CubicSpline(x, y, slope1 = 0, slope2 = 0):
    matA, matB, coefficients = np.zeros((len(x), len(x))), np.zeros((len(x))), np.zeros((len(x) - 1, 4)) #Create empty matrixes
    matA[0][0], matA[len(x) - 1][len(x) - 1] = 1, 1 #Put 1s at the top left and bottom right of matA
    stepSize = x[1] - x[0] #Assume a uniform step size throughout the provided array
    matB[0], matB[len(x) - 1] = slope1, slope2 #Put slope 1 and slope 2 at the beginning and end of matB
    for i in range(1, len(x) - 1):
        matA[i][i], matA[i][i + 1], matA[i][i-1] = 4, 1, 1 #Create a diagonal of 4 and 1 in matA
        matB[i] = (3 / stepSize) * (y[i + 1] - y[i - 1]) #Calculate needed values in matB for finding the k values
    kValues = np.linalg.solve(matA, matB) #Solve for the k values
    for i in range(len(x) - 1): #Loop through and use cubic spline equations to calculate the coefficients
        coefficients[i][0] = y[i]
        coefficients[i][1] = kValues[i]
        coefficients[i][2] = (3 / stepSize ** 2) * (y[i + 1] - y[i]) - (1 / stepSize) * (kValues[i + 1] + 2 * kValues[i])
        coefficients[i][3] = (2 / stepSize ** 3) * (y[i] - y[i + 1]) + (1 / stepSize ** 2) * (kValues[i + 1] + kValues[i])
    return coefficients

def PlotCubicSpline(x, y, slope1 = 0, slope2 = 0 , showpoints = True, npoints = 500):
    coefficients = CubicSpline(x, y, slope1, slope2) #Pass the x and y arrays to CubicSpline to calculate the coefficients of the spline
    for i in range(len(x) - 1): #Loop through the values in the main x array
        valuesX = np.linspace(x[i], x[i+1], npoints)
        valuesY = np.zeros(len(valuesX))#Create 500 points between the current points in the x array and a placeholder of the same size for storing the values of y
        for j in range(len(valuesX)): #Loop through the values in this valuesX array
            valuesY[j] = coefficients[i][0] + coefficients[i][1] * (valuesX[j] - x[i]) + coefficients[i][2] * (valuesX[j] - x[i]) ** 2 + coefficients[i][3] * (valuesX[j] - x[i]) ** 3 #Solve for the current value of y with the coefficients and add it to the valuesY array
        plt.plot(valuesX, valuesY, label = "Spline " + str(i + 1))

    plt.title('Cubic Spine') #Add a title and lable the axis for the plot
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')
    if showpoints: plt.plot(x,y,'ro', label='Original Data') #Plot original data if indicated
    plt.legend()
    plt.show()

def main():
    x = np.array([1.5, 3, 4.5, 6, 7.5, 9])
    y = np.array([3.5, 1.5, -2, 6.9, 8.2 ,1.5]) 
    slope1 = 2
    slope2 = -4

    coefficients = CubicSpline(x,y,slope1, slope2) #Pass the x and y arrays, along with the boundary slopes to CubicSpline to calculate the coefficients of the spline
    print('The coefficients of the spline are: ')
    print(coefficients)
    PlotCubicSpline(x, y, slope1, slope2) #Call PlotCubicSpline to calculate the needed values and display the plot

if __name__ == "__main__":
    main()