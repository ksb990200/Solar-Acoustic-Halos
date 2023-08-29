# Import necessary libraries
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from array import *
from skimage import color
from skimage import io
import cv2 
from numpy.fft import fft, fft2, ifft, ifft2
from matplotlib.colors import Normalize, LogNorm
from scipy.io import readsav as rsav
import matplotlib.colors as colors
import matplotlib.animation as anim
from astropy.io import fits
from sunpy.map import Map
import os
from matplotlib.patches import Rectangle

# Define folder paths for different types of data
fold = glob("folder0")        # Fits data
mvec_fold = glob("folder1")   # Magnetogram data
pwr_fold = glob('folder2')    # Power data

# Load sunspot data from continuum
sp_sav = rsav(fold[6])
sp_keys = list(sp_sav.keys())
sp_dat = sp_sav[sp_keys[1]]

# Load sunspot magnetogram data
sp_msav = rsav(mvec_fold[2])
sp_mkeys = list(sp_msav.keys())
sp_mstr = sp_msav[sp_mkeys[0]]
sp_minc = sp_msav[sp_mkeys[2]]

# Load solar pore data from continuum
p_sav = rsav(fold[2])
p_keys = list(p_sav.keys())
p_dat = p_sav[p_keys[1]]

# Load solar pore magnetogram data
p_msav = rsav(mvec_fold[0])
p_mkeys = list(p_msav.keys())
p_mstr = p_msav[p_mkeys[0]]
p_minc = p_msav[p_mkeys[2]]

# Initialize arrays to store power data for solar pore and sunspot
p_lf_pwr = []
sp_lf_pwr = []
p_hf_pwr = []
sp_hf_pwr = []
pwr = [p_lf_pwr, sp_lf_pwr, p_hf_pwr, sp_hf_pwr]

# Load power data into respective arrays
for i in range(len(pwr)):
    for l in range(4):
        pwr_mps = np.load(pwr_fold[l+(i*4)])
        pwr[i].append(pwr_mps)

# Visualize the region of interest with contours
plt.figure(figsize=(8,8))
p_im = p_dat[0]
plt.gca().add_patch(Rectangle((260,100), 50,50, facecolor="none", edgecolor="g", lw=2,label="Solar Pore 1"))
plt.gca().add_patch(Rectangle((250,350), 50,50, facecolor="none", edgecolor="k", lw=2,label="Solar Pore 2"))
plt.contour(p_mstr, [200,1500], linewidths=0.8, colors=['purple', 'r'])
# Customize labels and title
plt.ylabel("arcsec")
plt.xlabel("arcsec")
plt.title('Solar Pore region of interest')
plt.savefig('Solar Pore 200G, 1500G OC.png', dpi=500)

# Visualize the region of interest with contours for sunspot
sp_im = sp_dat[0]
plt.gca().add_patch(Rectangle((450,50),110, 100, facecolor="none", lw=2, edgecolor='g'))
plt.contour(sp_mstr, [700,1500], colors=['purple', 'r'], linewidths=0.8)
yini_labels = np.linspace(0,sp_im.shape[0], 7)
xini_labels = np.linspace(0,sp_im.shape[1], 7)
xlabels = np.linspace(-((sp_im.shape[0]//2)*0.6), ((sp_im.shape[0]//2)*0.6), xini_labels.shape[0])
ylabels = np.linspace(-((sp_im.shape[1]//2)*0.6), ((sp_im.shape[1]//2)*0.6), yini_labels.shape[0])
plt.xticks(xini_labels, ylabels)
plt.yticks(yini_labels, xlabels)
plt.ylabel("arcsec")
plt.xlabel("arcsec")
plt.title('Sun Spot region of interest')
plt.savefig('Sun Spot 700G, 1500G OC.png', dpi=500)

# Scatter plots for field strength and normalized power, and field inclination and normalized power
# Create subplots
fig, ax = plt.subplots(2, 4, figsize=(16, 9))
# Set the threshold to filter data
threshold = 20

for i, p_lf_data in enumerate(p_lf_pwr):
    if i < 4:
        x_str = p_mstr[100:150, 260:310]
        p_lf_pwr_data = p_lf_data[100:150, 260:310]

        ind = x_str > threshold
        ind1 = (x_str > 200) & (x_str<1500)
        x_str, y_ppwr = x_str[ind], p_lf_pwr_data[ind]

        ax[0][i].scatter(x_str, y_ppwr, s=0.2)

        unique_x, indices = np.unique(x_str, return_inverse=True)
        mean_range = 50
        mask = np.abs(x_str[:, None] - unique_x) <= mean_range
        y1 = np.sum(np.where(mask, y_ppwr[:, None], 0), axis=0) / np.sum(mask, axis=0)
        x1 = unique_x

        ax[0][i].plot(x1, y1, linewidth=1, c='r', label=r"Averaging in $|\vec{B}|$ bins")
        ax[0][i].set_xlabel("Magnetic Field strength (in Gauss)")
        ax[1][i].set_xlabel("Inclination of the Magnetic field (in $^o$)")
        
        if i <2:
            ax[0][i].set_ylim(0,1)
            ax[0][i].axvline(x=200, c='g', label="200G line")
            ax[1][i].set_ylim(0,1)
        else:
            pass
        
        ax[0][i].legend()
        
        x_inc = p_minc[100:150, 260:310]
        x_inc, y_ppwr1 = x_inc[ind1], p_lf_pwr_data[ind1]
        
        ax[1][i].scatter(x_inc+23, y_ppwr1, c='r', s=0.2)
        
        unique_x1, indices1 = np.unique((x_inc+23), return_inverse=True)
        mean_range1 = 10
        mask1 = np.abs((x_inc+23)[:, None] - unique_x1) <= mean_range1
        y2 = np.sum(np.where(mask1, y_ppwr1[:, None], 0), axis=0) / np.sum(mask1, axis=0)
        x2 = unique_x1

        ax[1][i].plot(x2, y2, linewidth=1, c='b')

ax[0][i].set_title(ttl[i]+" in 4mHz")
ax[0][0].set_ylabel("Power normalized to Quite Sun")
ax[1][0].set_ylabel("Power normalized to Quite Sun")
fig.suptitle("Solar Pore Power distribution", fontsize=18)
plt.savefig("Inclination and field strength of Solar Pore 4mHz.png", dpi=500)
plt.show()

# Similar scatter plots for sunspot
# (Continuing from previous code snippet)
fig, ax = plt.subplots(2, 4, figsize=(16, 9))
threshold = 20

for i, sp_lf_data in enumerate(sp_lf_pwr):
    if i < 4:
        x_str = sp_mstr[150:280, 110:210]
        sp_lf_pwr_data = sp_lf_data[150:280, 110:210]

        ind = x_str > threshold
        ind1 = (x_str > 200) & (x_str<1500)
        x_str, y_ppwr = x_str[ind], sp_lf_pwr_data[ind]

        ax[0][i].scatter(x_str, y_ppwr, s=0.2)

        unique_x, indices = np.unique(x_str, return_inverse=True)
        mean_range = 50
        mask = np.abs(x_str[:, None] - unique_x) <= mean_range
        y1 = np.sum(np.where(mask, y_ppwr[:, None], 0), axis=0) / np.sum(mask, axis=0)
        x1 = unique_x

        ax[0][i].plot(x1, y1, linewidth=1.2, c='r', label=r"Averaging in $|\vec{B}|$ bins")
        ax[0][i].set_xlabel("Magnetic Field strength (in Gauss)")
        ax[1][i].set_xlabel("Inclination of the Magnetic field (in $^o$)")        
 
        if i <2:
            ax[0][i].set_ylim(0,1.5)
            ax[0][i].axvline(x=200, c='g', label="200G line")
        else:
            pass
        
        ax[0][i].legend()
        
        x_inc = sp_minc[150:280, 110:210]
        x_inc, y_ppwr1 = x_inc[ind1], sp_lf_pwr_data[ind1]
        
        ax[1][i].scatter(90-np.abs((x_inc+19)), y_ppwr1, c='r', s=0.2)
        
        unique_x1, indices1 = np.unique((x_inc+19-90), return_inverse=True)
        mean_range1 = 10
        mask1 = np.abs((x_inc+19-90)[:, None] - unique_x1) <= mean_range1
        y2 = np.sum(np.where(mask1, y_ppwr1[:, None], 0), axis=0) / np.sum(mask1, axis=0)
        x2 = unique_x1

#         ax[1][i].pl/ot(x2, y2, linewidth=1, c='b')

ax[0][i].set_title(ttl[i]+" in 4mHz")
ax[0][0].set_ylabel("Power normalized to Quiet Sun")
ax[1][0].set_ylabel("Power normalized to Quiet Sun")
fig.suptitle("Sun Spot 2 Power distribution", fontsize=18)
# plt.savefig("Inclination and field strength of Sun Spot 4mHz.png", dpi=500)
plt.show()
