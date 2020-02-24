import math
import matplotlib.pyplot as plt
import numpy as np

def Horner(x, coeffs): #Bring in Horner's Rule from homework 1
    poly = coeffs[len(coeffs) - 1] #Initially define poly as the last element in the array
    for i in range(len(coeffs) - 2, -1, -1): poly = poly * x + coeffs[i]#Loop backwards from the 2nd to last array element to the first and the value of the polynomial using Horner's Rule
    return poly

def LeastSquares(x, y, power):
    matA, matB = np.zeros((len(x), power + 1)), np.zeros((len(x), 1)) #Create matrixes of the appropriate size
    for i in range(len(x)): #Loop through the values of the x array
        matB[i][0] = y[i] #Fill in matrix B with data from the y array
        for j in range(power + 1): matA[i][j] = x[i] ** j #Loop through "matrix" A and set the current element as the corresponding value in the x array to the power of j
    aTransxA = np.matmul(np.transpose(matA), matA) #Multiply transposed A by A
    aTransxB = np.matmul(np.transpose(matA), matB) #Multiply transposed A by B
    return np.linalg.solve(aTransxA, aTransxB) #Calculate the coefficients by solving the matrixes and return them back

def PlotLeastSquares(x, y, power, showpoints = True, npoints = 500):
    coefficients = LeastSquares(x,y,power) #Get the needed coefficients using the LeastSquares function
    valuesX, valuesY = np.linspace(min(x), max(x), npoints), np.linspace(min(x), max(x), npoints) #Create npoints evenly divided x points to calculate y for, and a placeholder array for the y values
    for i in range(len(valuesX)): valuesY[i] = Horner(valuesX[i], coefficients) #Use Horner's to solve for the y values respective to x
    
    '''
    It's plotting time
    '''
    
    plt.title('Least Squares Curve Fitting of Degree {:d}'.format(power)) #Add a title and lable the axis for the plot
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')
    if showpoints: plt.plot(x,y,'ro', label='Original Data') #Plot original data if indicated
    plt.plot(valuesX, valuesY, 'b', linewidth = 2, label = 'Power: ' + str(power)) #Add our x and y values with a lable indicating the power
    plt.legend()
    plt.show()
    return valuesX, valuesY #Return the x and y values we calculated to be displayed later in combination with the other plot

def main():
    x = np.array([.05, .11, .15, .31, .46, .52, .7, .74, .82, .98, 1.17])
    y = np.array([.956, 1.09, 1.332, .717, .771, .539, .378, .370, .306, .242, .104])

    '''
        Change the values of powerOne and powerTwo below in order to easily change the degree to solve for
    '''
    powerOne = 1 
    powerTwo = 3

    linCoeff = LeastSquares(x, y, powerOne) #Call LeastSquares with the x and y array and the power, return back the coefficient array
    print('The coefficients for a linear fit is: ', end = '')
    print(np.transpose(linCoeff)) #Since the array is returned with 1 column and several rows, transpose it so it prints nicer
    xValuesOne, yValuesOne = PlotLeastSquares(x, y, powerOne) #Pass the x and y array and the power to be plotted, return back the calculated x and y values for plotting again later

    cubCoeff = LeastSquares(x, y, powerTwo) #Call LeastSquares with the x and y array and the power, return back the coefficient array
    print('The coefficients for a cubic fit is: ', end = '')
    print(np.transpose(cubCoeff)) #Since the array is returned with 1 column and several rows, transpose it so it prints nicer
    xValuesTwo, yValuesTwo = PlotLeastSquares(x, y, powerTwo) #Pass the x and y array and the power to be plotted, return back the calculated x and y values for plotting again later
    
    plt.title('Combined Graphs') #Create a title and label the plot axis
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')    
    plt.plot(x, y, 'ro', label = 'Original Data') #Add the original data to the plot
    plt.plot(xValuesOne, yValuesOne, 'b', linewidth = 2, label='Power: ' + str(powerOne)) #Add the first set of data to the plot with a respective label
    plt.plot(xValuesTwo, yValuesTwo, 'g', linewidth = 2, label='Power: ' + str(powerTwo)) #Add the second set of data to the plot with a respective label
    plt.legend()
    plt.show()

if __name__ == "__main__": #I've been hesitant to correctly call main this semester but figured it's time
    main()
