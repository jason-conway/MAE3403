from math import *

def Simpson(fcn, a, b, npoints = 21):
    npoints += 1 if npoints % 2 == 0 else 0 #If npoints is even, add 1 to make it odd. This will also slightly increase accuracy. Nice
    h = (b - a) / npoints #Calculate the step-size to use
    est = fcn(a) + fcn(b) #There aren't coefficients of 2 or 4 for f(a) and f(b), let's go ahead and account for those
    for i in range(1, npoints, 2): est += 4 * fcn(a + (h * i)) #Add coefficient of 4 for every other term between f(a) and f(b)
    for i in range(2, npoints - 1, 2): est += 2 * fcn(a + (h * i)) #Add coefficient of 2 for every other term between f(a) and f(b)  
    return est * h / 3 #Finish Simpson's rule by multiplying by h / 3 and return the result

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    for i in range(maxiter): #Iterate the entered number of times or default to 10
        x = x1 - (fcn(x1) * (x1 - x0)) / (fcn(x1) - fcn(x0)) #Perform Secant method
        if abs(x - x1) < xtol: return x #If we converge within the entered (or default) value during the loop, go ahead and return back the value we converged to
        x0, x1 = x1, x #Update x0 and x1 with new values calculated with Secant method
    return x #Return the final calculated value

def SigmaMax(z):
    def x_lift(x): #Make function to be passed to Simpson. Equation comes from the problem statement
        return x * (1.5 * cos(x / 320)) 
    return (Simpson(x_lift, 0, 320) / z) #Estimate the integral of x_lift between 0 and 320 to solve for Mroot. Then divide by 320 to get the max bending stress and return the value

def DesignTheSpar(DesignStress):
    def solveModulus(z): #Make function to be passed to Secant
        return SigmaMax(z) - DesignStress
    return Secant(solveModulus, 1, 2) #Pass the function to Secant with initial guesses of 1 and 2 to estimate the value of z needed for the specified stress. Then return the value

def main():
    z = 3.5
    print('The stress value for a section modulus of {:.1f} is {:.1f}'.format(z, SigmaMax(z)))

    z = 1.5
    print('The stress value for a section modulus of {:.1f} is {:.1f}'.format(z, SigmaMax(z)))
    
    designStress = 25000
    print('The section modulus required for a design stress of {:.2f} is {:.2f}'.format(designStress, DesignTheSpar(designStress)))

main()