from math import cos

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    for i in range(maxiter): #Iterate the entered number of times or default to 10
        x = x1 - (fcn(x1) * (x1 - x0)) / (fcn(x1) - fcn(x0)) #Perform Secant method
        x0, x1 = x1, x #Update x0 and x1 with new values calculated with Secant method
        if abs(x - x1) < xtol: return x #If we converge within the entered (or default) value during the loop, go ahead and return back the value we converged to
    return x #Return the final calculated value

def main():
    def funcA(x): #First function to pass to Secant()
        return x - 3 * cos(x)

    def funcB(x): #Second and third function to pass to Secant()
        return cos(2 * x) * x**3
        
    ans = Secant(funcA, 1, 2, 5, 1e-4) #Call Secant() with our desired args
    print('Estimation of "x - 3 * cos(x)" is: {:.3f}'.format(ans))

    ans = Secant(funcB, 1, 2, 15, 1e-8) #Call Secant() with our desired args
    print('Estimation of "cos(2x) * x^3" is: {:.3f}'.format(ans))

    ans = Secant(funcB, 1, 2, 3, 1e-8) #Call Secant() with our desired args
    print('Estimation of "cos(2x) * x^3" is: {:.3f}'.format(ans))

main()