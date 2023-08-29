import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from glob import glob
import pandas as pd 
from numpy.fft import fft, ifft
from matplotlib.animation import  PillowWriter
import matplotlib.animation as anim
from matplotlib import colors

# Importing necessary libraries

# Set the path to the folder containing the FITS files
file_paths = glob("folder")

# Define grid parameters
grid_size = 100
lim_2 = 900
lim_1 = 1450

# Creating data cubes to store the FITS data
data_cube = np.zeros((80, grid_size, grid_size), float)

# Load data from FITS files and populate the data cube
for i, file_path in enumerate(file_paths):
    with fits.open(file_path) as hdulist:
        data = hdulist[0].data
        data_cube[i] = data[lim_1:lim_1+grid_size, lim_2:lim_2+grid_size]

# Create a figure for animation
fig = plt.figure()

# Initialize the first frame of the animation with the initial data
im = plt.imshow(data_cube[0,:,:], interpolation="none", cmap="gray", origin="lower")
title = plt.title("")

# Define the update function for the animation
def update(t):
    im.set_array(data_cube[t,:,:])
    #title.set_text(str(t))

# Create an animation using FuncAnimation
ani = anim.FuncAnimation(fig, func=update, frames=80, repeat=False, interval=100)

# Save the animation as an MP4 video
ani.save("SUNs_GOT_MOVES_OG.mp4", dpi=100)

# Display the animation
plt.show()
