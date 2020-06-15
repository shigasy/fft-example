import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 64
n = np.arange(N)
f1 = 2  # 周期1
f2 = 6  # 周期2
a1 = 1.5  # 振幅1
a2 = 3  # 振幅2
f = a1 * np.sin(f1 * 2 * np.pi * (n/N)) + a2 * np.sin(f2 * 2 * np.pi * (n/N))
# グラフ表示
# plt.figure(figsize=(8, 4))
# plt.xlabel('n')
# plt.ylabel('Signal')
# plt.plot(f)
# plt.show()

# FFT
F = np.fft.fft(f)

# FFT結果の複素数を絶対値に変換
F_abs = np.abs(F)

# 振幅を元の信号に揃える
F_abs_amp = F_abs / N * 2
F_abs_amp[0] = F_abs_amp[0] / 2

plt.plot(F_abs_amp[:int(N/2 + 1)])
plt.show()
