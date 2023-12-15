import pandas as pd
import numpy as np

class simplePerson:
    def __init__(self):
        for j in range(21):
            setattr(self, f"random{j}", np.random.uniform(size=20).tolist())

def meanOfList(x):
    return x["random"].apply(np.mean)

def meanOfListNTimes(x):
    for i in range(100):
        a = x["random"].apply(np.mean)
    return a

def meanOfListOb(x):
    setattr(x, "randomMean", np.mean(x.random))
    return x

def meanOfListObP(x):
    list(map(lambda y: setattr(y, "randomMean", np.mean(y.random)), x)) 
    return x

def meanOfListObPNTimes(x):
    for i in range(100):
        list(map(lambda y: setattr(y, "randomMean", np.mean(y.random)), x))
    return x     

def doNothingReturnArg(x):
    return x

def doNothingReturn0(x):
    return 0

def meanOfColumns(x):
    return pd.DataFrame.apply(x[[f"random{j}" for j in range(0,20)]],np.mean, axis=1)

def meanOfColumnsOb(x):
    setattr(x, "randomMean", np.mean([getattr(x, f"random{j}") for j in range(0,20)] ))         
    return x

def meanOfColumnsUsingPandas(x):
    return x[[f"random{j}" for j in range(0,20)]].mean(axis=1)

