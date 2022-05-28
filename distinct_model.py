import pandas as pd
import os
import numpy as np
from scipy.stats import norm
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import math


def func(p, endT, J0):
    beta = 0.22163846
    l, useless = p
    I = [0 for _ in range(endT)]
    J = [0 for _ in range(endT)]
    deltaJ = [0 for _ in range(endT)]
    G = [0 for _ in range(endT)]
    I_0 = [0 for _ in range(endT)]
    C = [0 for _ in range(endT)]
    I[0] = J0 * 4 / 3
    G[0] = J0 * 2 / 30
    J[0] = J0
    for t in range(endT - 1):
        I_0[t] = I[t] - J[t] - G[t]
        prob = 0
        for s in range(t):
            prob = prob + (5 ** (t - s)) * math.exp(-5) / math.factorial(t - s)
            C[t] = C[t] + I_0[s] * (5 ** (t - s)) * math.exp(-5) / math.factorial(t - s)
        C[t] = C[t] + I_0[0] * (1 - prob) * 1.4
        I[t + 1] = I[t] + beta * I_0[t]
        J[t + 1] = J[t] + beta * C[t]
        G[t + 1] = G[t] + l * I_0[t] - l * C[t]
        deltaJ[t + 1] = J[t + 1] - J[t]
    return np.array(deltaJ[1:])


def error(p, x, y0, y):
    return func(p, x, y0) - y


# Yi = np.array([24820,22248,20416,18901,18495,17629,23370,21058,19455,16980,13562,10622,15032,10181,7872,7333,5669,4982,4651,4269,4214,3975,3947,3014,1487,1449,2096,1681,1367,938])
p0 = [0.07, 0]

Y0 = [126475, 19722, 7164, 22354, 7737, 10996, 10171, 11640, 13971, 41052, 12305, 1147, 11568, 5964, 2314, 2361]
distinct_data = pd.read_excel("distinct_data.xlsx")
result = []
for i in range(16):
    i = i + 1
    print(distinct_data.columns[i])
    Yi = np.array(distinct_data.iloc[-30:, i])
    # 真实值
    y0 = Y0[i - 1]
    Para = leastsq(error, p0, args=(1 + 30, y0, Yi))
    print(Para[0])
    result.append(Para[0][0])
    Yfit = func(Para[0], 30 + 1, y0)
    # 拟合值
pd.DataFrame(result, index=distinct_data.columns[1:17]).to_excel("distinct_result.xlsx")
