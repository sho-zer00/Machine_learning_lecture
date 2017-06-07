import numpy as np

def AND(x1,x2):
    w1, w2, ikiti = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= ikiti:
        return 0
    elif tmp > ikiti:
        return 1

def AND02(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1,x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y
