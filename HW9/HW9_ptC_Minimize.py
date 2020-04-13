from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

def func(t, vals):
    A, B, C = vals
    return A + B * np.exp(C * t)

def plotfunc(f, vals):
    t=np.linspace(0,2,1000)
    y=np.zeros_like(t)
    for i in range(1000):
        y[i]=f(t[i], vals)
    plt.plot(t,y)
    plt.show()

def NonlinearCurve(vals, t, data):
    A, B, C = vals
    error = 0
    penalty = 0
    for i in range(len(t)):
        func = A + B * np.exp(C * t[i])
        error += (func - data[i])**2
    if np.abs(error) > 0:
        penalty += error * 1e100
    return penalty

def main():

    pts = 6
    t = np.zeros(pts)
    data1 = np.zeros(pts)
    data2 = np.zeros(pts)

    for i in range(pts):
        t[i] = i/3
        data1[i] = 2 + -2*np.exp(-0.6*t[i])
        data2[i] = -3 + 2*np.exp(-0.7*t[i])


    # data1 = [0, 0.363, 0.659, 0.902, 1.101, 1.264]

    # 2D optimization - constrained
    guess = [1, 1, -1]
    answer = minimize(NonlinearCurve, guess, args=(t, data1), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data1), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data1), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data1), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data1), method='Nelder-Mead')

    print(answer.x, answer.fun)

    x = np.linspace(0,2,1000)
    y = np.zeros_like(x)
    for i in range(1000):
        y[i] = func(x[i], answer.x)
    plt.plot(x, y)
    plt.plot(t, data1, 'o')
    plt.show()

    answer = minimize(NonlinearCurve, guess, args=(t, data2), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data2), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data2), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data2), method='Nelder-Mead')
    answer = minimize(NonlinearCurve, answer.x, args=(t, data2), method='Nelder-Mead')

    print(answer.x, answer.fun)

    x = np.linspace(0, 2, 1000)
    y = np.zeros_like(x)
    for i in range(1000):
        y[i] = func(x[i], answer.x)
    plt.plot(x, y)
    plt.plot(t, data2, 'o')
    plt.show()

main()