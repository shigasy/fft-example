import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 2πを0.1刻みで表現する
x = np.arange(0, 2*np.pi, 0.1)

print(x)
print(np.sin(x))
