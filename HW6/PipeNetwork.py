from scipy.optimize import fsolve
import numpy as np

from HW6.PipeClass import Pipe
from HW6.PumpClass import Pump

# Solve the pipe network when the supply is a pressure source
def p1errors(pvals, pipelist, rho, mu, supplyp): # using a pressure source
    pressureB, pressureC, pressureD = pvals #Expand pressures
    ab, bc, cd, bd, de = pipelist #Expand pipes

    Qab = ab.flow(pressureB - supplyp, rho, mu)
    Qbc = bc.flow(pressureC - pressureB, rho, mu)
    Qcd = cd.flow(pressureD - pressureC, rho, mu)
    Qde = de.flow(0 - pressureD, rho, mu)
    Qbd = bd.flow(pressureD - pressureB, rho, mu)

    flowErrors = [Qab - Qbc - Qbd, #Sum of the flows at node B
                 Qbc - Qcd, #Sum of the flows at node C
                 Qcd + Qbd - Qde] #Sum of the flows at Node D

    return flowErrors

# Solve the pipe network when the supply is a flow source
def p2errors(pvals, pipelist,rho,mu,supplyQ): # using a pressure source
    pressureA, pressureB, pressureC, pressureD = pvals #Expand pressures
    ab, bc, cd, bd, de = pipelist #Expand pipes

    Qab = ab.flow(pressureB - pressureA, rho, mu)
    Qbc = bc.flow(pressureC - pressureB, rho, mu)
    Qcd = cd.flow(pressureD - pressureC, rho, mu)
    Qde = de.flow(0 - pressureD, rho, mu)
    Qbd = bd.flow(pressureD - pressureB, rho, mu)

    flowErrors = [supplyQ - Qab,
                  Qab - Qbc - Qbd, #Sum of the flows at node B
                  Qbc - Qcd, #Sum of the flows at node C
                  Qcd + Qbd - Qde] #Sum of the flows at Node D

    return flowErrors

# Solve the pipe network when the supply is a pump
def p3errors(pvals, pipelist, rho, mu, pump):  # using a pump
    pressureA, pressureB, pressureC, pressureD = pvals #Expand pressures
    ab, bc, cd, bd, de = pipelist #Expand pipes

    Qab = ab.flow(pressureB - pressureA, rho, mu)
    Qbc = bc.flow(pressureC - pressureB, rho, mu)
    Qcd = cd.flow(pressureD - pressureC, rho, mu)
    Qde = de.flow(0 - pressureD, rho, mu)
    Qbd = bd.flow(pressureD - pressureB, rho, mu)

    flowErrors = [pump.flow(pressureA) - Qab,
                  Qab - Qbc - Qbd, #Sum of the flows at node B
                  Qbc - Qcd, #Sum of the flows at node C
                  Qcd + Qbd - Qde] #Sum of the flows at Node D
    pump.dp = pump.dp[0]
    return flowErrors

def main():
    rho = 1.94
    mu = 0.0000186
    eps = 0.00082

    ab = Pipe(4/12, 2500, eps, 'ab')
    bc = Pipe(5/12, 3500, eps, 'bc')
    cd = Pipe(6/12, 6000, eps, 'cd')
    bd = Pipe(8/12, 2000, eps, 'bd')
    de = Pipe(8/12, 1500, eps, 'de')

    pipelist = [ab,bc,cd,bd,de]

    #Pressure Source
    guess = [1000,1100,1200]
    supplyp = 7596.4 #psf or 100 psi
    Pvals = fsolve(p1errors, guess, args = (pipelist, rho, mu, supplyp))

    Pvals = fsolve(p1errors, Pvals, args = (pipelist, rho, mu, supplyp))
    pb, pc, pd = Pvals

    print('\nPressures at b, c and d are {:.1f}, {:.1f} and {:.1f}'.format(pb, pc, pd))

    for pipe in pipelist: pipe.print()

    print('Fsolve Errors: ', p1errors(Pvals, pipelist, rho, mu, supplyp))

    #Flow Source
    guess = [10000, 1000, 1100, 1200]
    supplyQ = 0.54932 #cfm
    Pvals = fsolve(p2errors, guess, args=(pipelist, rho, mu, supplyQ))
    pa, pb, pc, pd = Pvals

    print('\nPressures at a, b, c and d are {:.1f}, {:.1f}, {:.1f} and {:.1f}'.format(pa, pb, pc, pd))
    for pipe in pipelist: pipe.print()
    print('Fsolve Errors: ', p2errors(Pvals, pipelist, rho, mu, supplyQ))

    #Pump Source
    pump = Pump([15000, -1820, -12900, -15150]) #create the pump object

    guess = [130, 120, 110, 100]
    Pvals = fsolve(p3errors, guess, args=(pipelist, rho, mu, pump))
    pa, pb, pc, pd = Pvals

    print('\nPressures at a, b, c and d are {:.1f}, {:.1f}, {:.1f} and {:.1f}'.format(pa, pb, pc, pd))
    for pipe in pipelist: pipe.print()
    print('Pump flow and pressure are: {:.3f} and {:.3f}'.format(pump.Q, pump.dp))
    print('Fsolve Errors: ', p3errors(Pvals, pipelist, rho, mu, pump))

main()
