# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp

a = np.array([5, 2, -3], float)
b = np.array([0, 9, 8], float)
c = np.array([4, 5, 6], float)
d = np.array([a, b, c], float)
#########
z = np.zeros((3, 3))
lin = np.array([1, 1, 0, 0, 0, 1, 0, 0, 1])
fft_lin = sp.fft(lin)
fft_lin = np.fft.fftpack.fft(lin, 16)
fft_lin = np.fft.fft(lin, 16)
fft_lin = sp.fft(lin, 16)

print ((d.shape))
print ((d.transpose()[0, :]))
print (z)
print ((fft_lin))
print ((np.roots(a)))
