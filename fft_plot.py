# -*- coding: utf-8 -*-

import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


# Number of samplepoints
N = 1000
# sample spacing
T = 1.0 / 8000.0
x = np.linspace(0.0, N * T, N)
y1 = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
y2 = np.sin(100.0 * 2.0 * np.pi * x) + (1. / 3) * np.sin(300.0 * 2.0 * np.pi * x)
yf1 = np.absolute(fft(y1, 512))
yf2 = np.absolute(fft(y2, 512))
#xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)
xf = np.array(list(range(512)))
xf = xf[0:512]
#print (xf.size)
#print (yf1.size)
#print (yf2.size)

# plots
plt.figure(1)
#plt.plot(x, y1, 'b')
#plt.plot(x, y2, 'r')
plt.plot(x, y1, 'b', x, y2, 'r')
plt.legend(['50, 80', '100, 300'])
plt.grid()


plt.figure(2)
plt.plot(xf[0:128], yf1[0:128], 'b', xf[0:128], yf2[0:128], 'r')
plt.legend(['50, 80', '100, 300'])
plt.grid()

plt.show()
