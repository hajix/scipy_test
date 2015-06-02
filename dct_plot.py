# -*- coding: utf-8 -*-

from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
import numpy as np

N = 100
t = np.linspace(0, 20, N)
x = np.exp(-t / 3) * np.cos(2 * t)
y = dct(x, norm='ortho')
window20 = np.zeros(N)
window20[0:20] = 1
# print (window)
yr20 = idct(y * window20, norm='ortho')
print ('absolute error with 20 coefficient:')
#print((sum(abs(x - yr20) ** 2) / sum(abs(x) ** 2)))
print((sum(abs(x - yr20) ** 2)))
plt.plot(t, x, '-bx')
plt.plot(t, yr20, '+r-')
window15 = np.zeros(N)
window15[0:15] = 1
yr15 = idct(y * window15, norm='ortho')
print ('absolute error with 15 coefficient:')
#print((sum(abs(x - yr15) ** 2) / sum(abs(x) ** 2)))
print((sum(abs(x - yr15) ** 2)))
plt.plot(t, yr15, 'g+')
plt.legend(['x', '$x_{20}$', '$x_{15}$'])
plt.grid()
plt.show()
