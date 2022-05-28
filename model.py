import pandas as pd
import os
import numpy as np
from scipy.stats import  norm
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import math
import seaborn as sns
sns.set_style("darkgrid",{"font.sans-serif":['KaiTi', 'Arial']})

def func(p, endT):
    beta, l = p
    I=[0 for _ in range(endT)]
    J=[0 for _ in range(endT)]
    deltaJ = [0 for _ in range(endT)]
    G=[0 for _ in range(endT)]
    I_0=[0 for _ in range(endT)]
    C = [0 for _ in range(endT)]
    I[0] = 400000
    G[0] = 20000
    J[0] = 300000
    for t in range(endT-1):
        I_0[t] = I[t] - J[t] - G[t]
        prob=0
        for s in range(t):
            prob=prob+(5**(t-s))*math.exp(-5)/math.factorial(t-s)
            C[t] = C[t] + I_0[s] *(5**(t-s))*math.exp(-5)/math.factorial(t-s)
        C[t] = C[t] + I_0[0]*(1-prob)*1.4
        I[t+1]=I[t]+beta*I_0[t]
        J[t+1]=J[t]+beta*C[t]
        G[t+1]=G[t]+l*I_0[t]-l*C[t]
        deltaJ[t+1]=J[t+1]-J[t]
    return np.array(deltaJ[1:])

def error(p, x, y):
    return func(p, x) - y
Yi = np.array([24820,22248,20416,18901,18495,17629,23370,21058,19455,16980,13562,10622,15032,10181,7872,7333,5669,4982,4651,4269,4214,3975,3947,3014,1487,1449,2096,1681,1367,938])
p0=[0.3,0.5]
Para = leastsq(error, p0, args=(1+30, Yi))
# 读取结果
beta, l = Para[0]
actual, l = Para[0]
predict = func(Para[0],35+1)

plt.plot([i for i in range(len(Yi))], Yi, color='black', alpha=1, label='实际感染人数')
plt.plot([i for i in range(len(predict))], predict, color='red', alpha=1, label='预测感染人数')
plt.title('实际感染人数与预测感染人数对比')
plt.legend()
plt.xlabel('天数')
plt.ylabel('感染数')
plt.show()


