import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 128
dt = 0.01  # サンプリング周期（sec）: 10ms => サンプリング周波数100Hz
freq = 10  # 周波数（10hz） => 正弦波の周期0.1sec
amp = 1  # 振幅

t = np.arange(0, N*dt, dt)  # 時間軸 1.28秒 0.01刻みが128個

# 周波数軸のデータ作成
# 100Hzで
fq = np.linspace(0, 1.0/dt, N)  # 周波数軸　linspace(開始,終了,分割数)


f = amp * np.sin(2 * np.pi * freq * t)  # 波の関数

# グラフ表示
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)
plt.plot(t, f)
plt.show()

F = np.fft.fft(f)  # 高速フーリエ変換(FFT)

# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
# 振幅をもとの信号に揃える
F_abs_amp = F_abs / N * 2  # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要
# グラフ表示
# 周波数軸に変更してグラフを再表示
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)
# plt.plot(F_abs_amp)  # ->NG、周波数軸に変更する必要あり
plt.plot(fq, F_abs_amp)  # ->NG、周波数軸に変更する必要あり
plt.show()
