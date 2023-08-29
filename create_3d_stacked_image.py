import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# List of image filenames to be stacked
image_files = ['image1.png', 'image2.png', 'image3.png']

# Initialize an empty list to store the images
images = []
for filename in image_files:
    img = plt.imread(filename)
    images.append(img)

# Create a figure with adjusted DPI
fig = plt.figure(dpi=300)

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Determine dimensions of the images
x_dim = images[0].shape[1]
y_dim = images[0].shape[0]
z_dim = len(images)

# Create meshgrid for x and y dimensions
x = np.arange(0, x_dim)
y = np.arange(0, y_dim)
X, Y = np.meshgrid(x, y)

# Iterate through the images and stack them in 3D

for i in range(z_dim):
    Z = np.ones_like(X) * i
    img = images[i]
    ax.plot_surface(X, Y, Z, facecolors=img, rstride=1, cstride=1
                    , linewidth=0, antialiased=False) #add interpolation = Lanczos for better quality

    # Overlay images without interpolation for better performance
    ax.imshow(img, extent=(0, x_dim, 0, y_dim, i, i), interpolation='none')

# Remove tick labels for better visualization
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Set title and adjust aspect ratio of the plot
ax.set_title('3D Stacked Plot')
ax.set_box_aspect([1, 1, 1])

# Save the plot with higher resolution
fig.savefig('stacked_images.png', dpi=500)

# Show the plot
plt.show()
