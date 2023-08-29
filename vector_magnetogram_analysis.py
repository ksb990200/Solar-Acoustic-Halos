import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import astropy.io
from sunpy.map import Map
from scipy.io import readsav as rsav

# Importing necessary libraries

# Set the paths to the folders containing .sav files
#c_fold contains files in fits format
#this is to calculate the line of sight angle of the central pixel from the disk data
#s_fold contains other sav files of different wavelengths
ms_fold = glob('Vector Magnetogram/*')
s_fold = glob("sav folder/*")
c_fold = glob("Continuum/*")

# Extracting information regarding the inclination angle of the central pixel of the image

# Opening the fits files
c_fits = Map(c_fold[0])
c_dat = c_fits.data
c_met = c_fits.meta

# Initialize arrays to store central pixel coordinates and angles
x_cent = np.zeros((3,1), float)
y_cent = np.zeros((3,1), float)
arc_dist = np.zeros((3,1), float)
cen_ang = np.zeros((3,1), float)
i=0

# Loop through to calculate central pixel coordinates and angles
for m in range(3):
    sav = rsav(s_fold[i])
    xcen = sav['xcen']
    ycen = sav['ycen']

    x_cent[m] = xcen
    y_cent[m] = ycen
    
    arc_dist[m] = np.sqrt(xcen**2 + ycen**2)
    cen_ang[m] = np.rad2deg(np.arcsin((arc_dist[m])/c_met["RSUN_OBS"]))
    
    i += 4

# Create subplots for visualizing inclination angles
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
lst_mag = []
h=0
while h <=2:
    s_mag = rsav(ms_fold[h])
    s_keys = list(s_mag.keys())
    incl = s_mag[s_keys[2]] - cen_ang[h]
    lst_mag.append(incl)
    figure = ax[h].imshow(lst_mag[h], cmap="twilight", origin="lower")
    ax[h].set_aspect("auto")
    clb = fig.colorbar(figure, ax=ax[h])

    h = h+1
plt.show()

# Extracting the inclination and strength information from the magnetogram and making an array out of it

inc_mag = []
str_mag = []
for h in range(3):
    s_mag = rsav(ms_fold[h])
    s_keys = list(s_mag.keys())
    incl = s_mag[s_keys[2]] - cen_ang[h]
    strnt = s_mag[s_keys[0]]
    inc_mag.append(incl)
    str_mag.append(strnt)
