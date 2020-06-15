import numpy as np
import matplotlib.pyplot as plt

# 簡単な信号の作成
N = 128  # サンプル数
dt = 0.01  # サンプリング周期(sec):100ms =>サンプリング周波数100Hz
freq1 = 10  # 周波数(10Hz) =>正弦波の周期0.1sec
amp1 = 1  # 振幅
freq2 = 15  # 周波数(15 Hz) =>正弦波の周期0.sec
amp2 = 1  # 振幅

t = np.arange(0, N*dt, dt)  # 時間軸
f = amp1 * np.sin(2*np.pi*freq1*t) + amp2 * np.sin(2*np.pi*freq2*t)  # 信号
# グラフ表示
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('signal', fontsize=14)
plt.plot(t, f)
plt.show()


# 高速フーリエ変換(FFT)
F = np.fft.fft(f)

# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
# 振幅をもとの信号に揃える
F_abs_amp = F_abs / N * 2  # 交流成分はデータ数で割って2倍
F_abs_amp[0] = F_abs_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# 周波数軸のデータ作成
fq = np.linspace(0, 1.0/dt, N)  # 周波数軸　linspace(開始,終了,分割数)

# グラフ表示（FFT解析結果）
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq, F_abs_amp)

plt.show()

F_ifft = np.fft.ifft(F)  # 逆フーリエ変換(IFFT)
F_ifft_real = F_ifft.real  # 実数部
F_ifft_real[:10]
plt.plot(t, F_ifft_real, c="g")  # IFFT（逆変換）
plt.show()
