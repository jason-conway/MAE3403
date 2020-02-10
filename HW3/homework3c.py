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

def STO(thrust):
    #The following calculates the needed values to find STO
    Vstall = sqrt(56000 / (.5 * .002377 * 1000 *2.4))
    Vto = Vstall * 1.2
    A = 32.2 * (thrust / 56000)
    B = (32.2 / 56000) * (.5 * .002377 * 1000 * .0279)

    def S_TO(v): #Make a function to be passed to Simpson
        return v / (A - (B * v**2))
    return Simpson(S_TO, 0, Vto) #Pass the function to Simpsons to estimate the integral between 0 and Vto and return the value

def ThrustNeededForTakeoff(distance):
    def solveThrust(x): #Make a function to be passed to Secant
        return STO(x) - distance
    return Secant(solveThrust, 1000, 2000) #Pass the function and intial guesses of 1000 and 2000 feet to Secant in order to solve for the needed thrust and return the value
    
def main():
    distance = STO(13000)
    print('The take-off distance for an engine with 13,000 pounds of thrust is: {:.1f} feet.'.format(distance))

    thrustNeeded = ThrustNeededForTakeoff(1500)
    print('The thrust needed to take-off in a distance of 1,500 feet is {:.2f} pounds.'.format(thrustNeeded))

    thrustNeeded = ThrustNeededForTakeoff(1000)
    print('The thrust needed to take-off in a distance of 1,000 feet is {:.2f} pounds.'.format(thrustNeeded))

main()