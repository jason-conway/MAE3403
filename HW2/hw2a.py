from math import *

def Simpson(fcn, a, b, npoints = 21):
    npoints += 1 if npoints % 2 == 0 else 0 #If npoints is even, add 1 to make it odd. This will also slightly increase accuracy. Nice
    h = (b - a) / npoints #Calculate the step-size to use
    est = fcn(a) + fcn(b) #There aren't coefficients of 2 or 4 for f(a) and f(b), let's go ahead and account for those
    for i in range(1, npoints, 2): est += 4 * fcn(a + (h * i)) #Add coefficient of 4 for every other term between f(a) and f(b)
    for i in range(2, npoints - 1, 2): est += 2 * fcn(a + (h * i)) #Add coefficient of 2 for every other term between f(a) and f(b)  
    return est * h / 3 #Finish Simpson's rule by multiplying by h / 3 and return the result

def main():
    def funcA(x): #First function to pass to Simpson()
        return x - 3 * cos(x)
    
    def funcB(x): #Second function to pass to Simpson()
       return cos(2 * x) * x**3

    ans = Simpson(funcA, 1, 3, 10) #Call Simpson() with our desired args
    print('Estimation of "x - 3 * cos(x)" is: {:.3f}'.format(ans))

    ans = Simpson(funcB, 2, 3, 23) #Call Simpson() with our desired args
    print('Estimation of "cos(2x) * x^3" is: {:.3f}'.format(ans))

main()



