import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 32
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ]
n = np.arange(32)
# n / N = [0.      0.03125 0.0625  0.09375 0.125   0.15625 0.1875  0.21875 0.25 0.28125 0.3125  0.34375 0.375   0.40625 0.4375  0.46875 0.5 0.53125 0.5625  0.59375 0.625   0.65625 0.6875  0.71875 0.75    0.78125 0.8125 0.84375 0.875   0.90625 0.9375  0.96875]
# 32個のデータで2πを離散で表現
freq = 3  # 周期
signal = np.sin(2 * np.pi * n / N)
plt.figure(figsize=(8, 4))
plt.xlabel('n')
plt.ylabel('Signal')
plt.plot(signal)
plt.show()
