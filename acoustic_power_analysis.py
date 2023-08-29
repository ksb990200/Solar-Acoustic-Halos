import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from array import *
from skimage import color
from skimage import io
import glob as glob
import cv2 
from numpy.fft import fft, fft2, ifft, ifft2
from matplotlib.colors import Normalize, LogNorm
from scipy.io import readsav as rsav
import matplotlib.colors as colors
import matplotlib.animation as anim
from astropy.io import fits
from matplotlib import cm
import astropy.io
from sunpy.map import Map

# The folders with .sav files
folder = glob.glob("folder")

# Selecting the data
no = 11
file = folder[int(no)]

# Selecting data to normalize, i.e., the data is being normalized with quiet sun
norm_qsun = folder[7]

# Reading .sav files
sav = rsav(file)
qsav = rsav(norm_qsun)
keys = list(sav.keys())
qkeys = list(qsav.keys())

# Print available keys in the loaded .sav files
print(keys)
print(qkeys)

# Extracting data from the loaded .sav files
qf = qsav[qkeys[1]]
qt = qf[:, 10:(qf.shape[1]-10), 10:(qf.shape[2]-10)]
qd = qt[:, 1, 1]

f = sav[keys[1]]
t = f[:, 10:(f.shape[1]-10), 10:(f.shape[2]-10)]
q = t[:, 1, 1]

# Print shapes of extracted data
print(t.shape)
print(f.shape)

# Print xcen and ycen values from the loaded .sav files
print(sav["xcen"])
print(sav["ycen"])

# Calculate the frequency of the Fourier transformed data
# This section seems to be related to determining the frequency bins based on the length of data

# ... (frequency calculation code) ...

# Creating an array to hold the Fourier transformed data for quiet sun
qfarr = np.zeros((qt.shape[1:]), float)

# Calculate the Fourier transform and store it in qfarr
# This loop seems to calculate the amplitude of the Fourier transform for each pixel in the quiet sun data
# and stores it in qfarr
for i in range(qfarr.shape[0]):
    for j in range(qfarr.shape[1]):
        q_evo = qf[:, i, j]
        q_dfft = np.fft.fft(q_evo)
        qfarr[i, j] = np.sum(np.abs(q_dfft[num])**2)

# Calculate the average value of Fourier transformed data for quiet sun
qsun_av = np.average(qfarr)

# Creating an array to hold the Fourier transformed data for the main data
farr = np.zeros((t.shape[1:]), float)

# Calculate the Fourier transform and store it in farr
# This loop calculates the amplitude of the Fourier transform for each pixel in the main data
# and stores it in farr
for k in range(farr.shape[0]):
    for h in range(farr.shape[1]):
        evo = f[:, k, h]
        dfft = np.fft.fft(evo)
        farr[k, h] = np.sum(np.abs(dfft[num])**2)

# Plotting the data
fig = plt.figure(frameon="False")
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.imshow(farr/qsun_av, cmap="viridis", origin="lower", norm=Normalize(vmin=0.85, vmax=2.4))
plt.xticks([])
plt.yticks([])
plt.savefig("Sunspot Dop.png", dpi=500, transparent="True")
