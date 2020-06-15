import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 32  # データ数
n = np.arange(N)
freq = 3  # 周期 = 時間的に繰り返す振動の1周期 3つの周期
amp = 4  # 振幅 = 波の大きさ 縦の長さ
# np.sin(freq * 2 * np.pi * (n/N)) sinの波の定義
f = amp * np.sin(freq * 2 * np.pi * (n/N))  # freq=3周期分
print(f)
# 2πが3つある波を32個のplotで表現

# グラフ表示
# plt.figure(figsize=(8, 4))
# plt.xlabel('n')
# plt.ylabel('Signal')
# plt.plot(f)
# plt.show()

F = np.fft.fft(f)  # 高速フーリエ変換(FFT)
print(type(F), F.dtype)
print(F)  # FFT結果
F_abs = np.abs(F)

# Y軸の値が意味のない数値になっているため、振幅に合うように値を変換
F_abs_amp = F_abs / N * 2  # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2  # 直流成分は2倍不要

# plt.plot(F_abs) # 後半の鏡像が要らないから
# 周期を確認できるのは、データ数の半分まで
plt.plot(F_abs_amp[:int(N/2)+1])

plt.show()  # 周期3のsin波だから、3のところが
