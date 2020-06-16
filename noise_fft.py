import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)  # 乱数seed固定

N = 128
dt = 0.01  # サンプリング周期(sec) 100Hz
freq = 4  # 周波数 Hz 1秒あたりに繰り返される回数のこと 周期は1波長の数 周波数は1秒あたりに繰り返される回数のこと？ 4Hz
amp = 1  # 振幅

t = np.arange(0, N * dt, dt)
f = amp * np.sin(2 * np.pi * freq * t) + np.random.randn(N) * 0.3  # 信号

plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('signal', fontsize=14)
plt.plot(t, f)
plt.show()

F = np.fft.fft(f)
F_abs = np.abs(F)

F_abs_amp = F_abs / N * 2  # 交流成分はデータ数で割って2倍
F_abs_amp[0] = F_abs_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# 周波数軸　linspace(開始,終了,分割数) 等差数列。サンプリング周波数にX軸を揃える
fq = np.linspace(0, 1.0/dt, N)
print(fq)
print(F_abs_amp)

# グラフ表示（FFT解析結果）
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
# Xの要素とYの要素でグラフ化
plt.plot(fq, F_abs_amp)
plt.show()

# そのまま普通にIFFTで逆変換した場合
F_ifft = np.fft.ifft(F)  # IFFT
F_ifft_real = F_ifft.real  # 実数部
plt.plot(t, F_ifft_real, c="g")  # グラフ
plt.show()

F2 = np.copy(F)  # FFT結果コピー

# --------------
# 周波数でフィルタリング処理
fc = 10  # カットオフ（周波数）
F2[(fq > fc)] = 0  # カットオフを超える周波数のデータをゼロにする（ノイズ除去）

# フィルタリング処理したFFT結果の確認
# FFTの複素数結果を絶対値に変換
F2_abs = np.abs(F2)
# 振幅をもとの信号に揃える
F2_abs_amp = F2_abs / N * 2  # 交流成分はデータ数で割って2倍
F2_abs_amp[0] = F2_abs_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# グラフ表示（FFT解析結果）
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq, F2_abs_amp, c='r')
plt.show()

# 周波数でフィルタリング（ノイズ除去）-> IFFT
F2_ifft = np.fft.ifft(F2)  # IFFT
F2_ifft_real = F2_ifft.real * 2  # 実数部の取得、振幅を元スケールに戻す
# グラフ表示：オリジナルとフィルタリング（ノイズ除去）
plt.plot(t, f, label='original')
plt.plot(t, F2_ifft_real, c="r", linewidth=4, alpha=0.7, label='filtered')
plt.legend(loc='best')
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('singnal', fontsize=14)
plt.show()

# --------------

# グラフ再表示（FFT結果・フィルタリングなし)
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.hlines(y=[0.2], xmin=0, xmax=100, colors='r', linestyles='dashed')
plt.plot(fq, F_abs_amp)
plt.show()
F3 = np.copy(F)  # FFT結果コピー
# 振幅強度でフィルタリング処理
F3 = np.copy(F)  # FFT結果コピー
ac = 0.2  # 振幅強度の閾値
F3[(F_abs_amp < ac)] = 0  # 振幅が閾値未満はゼロにする（ノイズ除去）

# 振幅でフィルタリング処理した結果の確認
# FFTの複素数結果を絶対値に変換
F3_abs = np.abs(F3)
# 振幅をもとの信号に揃える
F3_abs_amp = F3_abs / N * 2  # 交流成分はデータ数で割って2倍
F3_abs_amp[0] = F3_abs_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# グラフ表示（FFT解析結果）
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq, F3_abs_amp, c='orange')
plt.show()

# 振幅強度でフィルタリング（ノイズ除去）-> IFFT
F3_ifft = np.fft.ifft(F3)  # IFFT
F3_ifft_real = F3_ifft.real  # 実数部の取得
# グラフ（オリジナルとフィルタリングを比較）
plt.plot(t, f, label='original')
plt.plot(t, F3_ifft_real, c="orange", linewidth=4, alpha=0.7, label='filtered')
plt.legend(loc='best')
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('singnal', fontsize=14)
plt.show()
