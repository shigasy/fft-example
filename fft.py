###############################################################################
# 高速フーリエ変換（ FFT ）を計算するプログラム
###############################################################################
# インポート
import matplotlib.pyplot as plt
import numpy as np

# 簡単な入力波の作成
N = 2**6  # サンプル数
dt = 0.025  # サンプリング周期（ sec ）
freq1 = 10  # 周波数（ Hz ）
ampl1 = 1  # 振幅
freq2 = 15  # 周波数（ Hz ）
ampl2 = 1  # 振幅
print("■■■　入力条件　■■■")
print("サンプル数 : " + str(N))
print("サンプリング周期 : " + str(dt) + ' sec')
print("サンプリング周波数 : " + str(1/dt) + ' Hz')
print("入力波１")
print("　　周波数 : " + str(freq1) + ' Hz')
print("　　振　幅 : " + str(ampl1))
print("入力波２")
print("　　周波数 : " + str(freq2) + ' Hz')
print("　　振　幅 : " + str(ampl2))

# 時間軸
t = np.arange(0, N*dt, dt)
print("サンプリング時間 : " + str(N*dt-dt) + ' sec')
print("サンプリング時刻 : " + str(t))

# ｛周波数　freq1, 振幅　amp1　の正弦入力波｝ + ｛周波数　freq2, 振幅　amp2　の正弦入力波｝
f = ampl1*np.sin(2*np.pi*freq1*t) + ampl2*np.sin(2*np.pi*freq2*t)
# 周波数　freq1, 振幅　amp1　の正弦入力波
#f = amp1 * np.sin(2*np.pi*freq1*t)

# 高速フーリエ変換（ FFT ）
F = np.fft.fft(f)

# FFT の複素数結果を絶対に変換
absf = np.abs(F)

# 振幅をもとの信号に揃える
absf_amp = absf / N * 2
absf_amp[0] = absf_amp[0] / 2

# 周波数軸のデータ作成
fq = np.linspace(0, 1.0/dt, N)

idx = np.argmax(f)
print("\n■■■　入力信号特性　■■■")
print("入力信号の最大idx : " + str(idx))
print("入力信号の最大振幅 : " + str(f[idx]))
print("入力信号の最大時刻 : " + str(t[idx]))

idx = np.array(absf_amp[:int(N/2)+1])  # コピー
idx = idx.argsort()[::-1]  # 降順に並べ替えた時のインデックスを取得する
print("\n■■■　フーリエ変換信号特性　■■■")
print("フーリエ変換信号の最大idx : " + str(idx[0]))
print("フーリエ変換信号の最大振幅 : " + str(absf_amp[idx[0]]))
print("フーリエ変換信号の最大周波数 : " + str(fq[idx[0]]))

print("\nフーリエ変換信号の次点idx : " + str(idx[1]))
print("フーリエ変換信号の次点振幅 : " + str(absf_amp[idx[1]]))
print("フーリエ変換信号の次点周波数 : " + str(fq[idx[1]]))

# グラフ表示
fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10, 4))

# 信号のグラフ（時間軸）
axL.plot(t, f)
axL.set_title('Input Wave')
axL.set_xlabel('time[sec]')
axL.set_ylabel('amplitude')
axL.grid(True)

# FFTのグラフ（周波数軸）
axR.plot(fq[:int(N/2)+1], absf_amp[:int(N/2)+1])
axR.set_title('Fast ')
axR.set_xlabel('freqency[Hz]')
axR.set_ylabel('amplitude')
axR.grid(True)

# グラフの出力
file_name = 'fft'
fig.savefig(file_name + '0.0.jpg', bbox_unches="tight")
