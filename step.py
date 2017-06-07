import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)  # -5.0~5.0までの範囲を0.1刻みでnumpy配列を生成
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1) # y軸の範囲を指定
plt.show()