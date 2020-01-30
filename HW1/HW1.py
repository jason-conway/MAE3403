import math #I use this for math.floor() in interp1D

def SequenceSumClosestTo(vals,thisSum):
    smallestDiff, closestSum = 2**64, 2**64 #Starting values to compare against. Should be big enough for *almost* all cases
    for i in range(len(vals)): 
        for j in range(i, len(vals)): #Lower bound for range needs to be the current value of i
            tempSum = sum(vals[i:j + 1:1]) #Splice input array between correct indexes and sum the members
            tempDiff = abs(tempSum - thisSum) #Scaler amount of deviance between current value and wanted value
            if tempDiff < smallestDiff: #New value is closer to desired value than the previous, update new values and corresponding indice markers
                smallestDiff, closestSum = tempDiff, tempSum #Update temp markers and new values and corresponding indice markers
                tempIndexI, tempIndexJ = i, j - i + 1 #Update indice markers corrosponding to our temp markers. Also correct length value to account for starting position and offset by one for clarity
    return tempIndexI, tempIndexJ, closestSum
    
def MatrixSumLarge(vals, large):
    largeSum = 0 #Variable used for adding "large values"
    for i in range(len(vals)):
        for j in range(len(vals) + 1): #Create loops for passing through all elements in matrix
            largeSum += vals[i][j] if abs(vals[i][j]) >= large else 0 #Add the currently indexed value in the matrix to largeSum if its absolute value is greater than "large"
    return largeSum

def Horner(x, coeffs):
    poly = coeffs[len(coeffs) - 1] #Initially define poly as the last element in the array
    for i in range(len(coeffs) - 2, -1, -1): #Loop backwards from the 2nd to last array element to the first
        poly = poly * x + coeffs[i] #Calculate the value of the polynomial using Horner's Rule
    return poly

def interp1D(x,xyvals, yvals): 
    i = 0 
    while xyvals[i] < math.floor(x): i += 1 #Find the index of the largest integer in xvals smaller than x 
    return (yvals[i] * (xyvals[i+1] - x)) + (yvals[i+1] * (x - xyvals[i])) / (xyvals[i+1] - xyvals[i]) #Return back the interpolated value using linear interpolation

def main():
    myvals = [1, 5, -2, 3, 5, 5, 3, 5, 2, -5, 3, 3, 1, 5] 
    mymatrix = [[1, 3.7, -7, 4], 
                [-8, -8, 2, -1.8],
                [-12, 7.9, 3.2, 12]
                ]
    a = [3, 2, -2, -4]
    xvals = [1, 2, 4, 5, 7]
    yvals = [2, 4, -2, 4, 5]
    x1 = 1.7
    x2 = 4.8
    mylarge = 5.2

    start, length, sum = SequenceSumClosestTo(myvals, 31)
    print('a) The {:d} term sequence starting at location {:d} sums to {:f}'.format(length, start, sum))

    mysum2 = MatrixSumLarge(mymatrix, mylarge)
    print('b) Sum of small values = {:.1f}'.format(mysum2))

    poly = Horner(x1, a)
    print('c) Polynomial value for (x1 = {:.2f}) = {:.1f}'.format(x1, poly))

    y = interp1D(x2, xvals, yvals)
    print('d) Interpolated value for (x2 = {:.2f}) = {:.3f}'.format(x2, y))

main()