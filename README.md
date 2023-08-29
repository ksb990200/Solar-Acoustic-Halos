# Solar Physics Project Code Repository

Welcome to the Solar Physics Project Code Repository! This repository contains Python scripts for analyzing solar data, creating animations, and generating visualizations. Below, you'll find descriptions and instructions for running each code snippet.

## Code Snippets

### 1. Analyzing Solar Acoustic Halos

- **Filename:** `acoustic_power_analysis.py`
- **Description:** This script analyzes solar acoustic halos using AIA 1700 angstrom image data from the Solar Dynamics Observatory (SDO) telescope. It performs Fourier transform-based analysis to calculate the acoustic power of solar features, particularly sunspots. The results are visualized using power maps.
- **Instructions:** Customize folder paths as needed and run the script.
- The data given to the code is in .sav format created by IDL data co-alignment routine, containing data cubes with time series information of certain regions of the Sun, also having x and y Centre values of the slected region.
- Data is tracked for rotation w.r.t the first frame. Later coaligned using get_correl_offsets. xcen, ycen, are in arcsecs.

### 2. Vector Magnetogram Analysis

- **Filename:** `vector_magnetogram_analysis.py`
- **Description:** This script analyzes vector magnetogram data from the SDO telescope. It calculates the inclination angle of the magnetic field with respect to the solar surface. The script also visualizes the inclination angles and magnetic field strengths, comparing them to the central pixel's line of sight angle obtained from continuum data.
- Vector magnetogram data along with respective uncertainties. Inclination is w.r.t line of sight.
- **Instructions:** Customize folder paths as needed and run the script.
- 

### 3. FITS Data Animation

- **Filename:** `fits_data_animation.py`
- **Description:** This script creates an animation from time series data in FITS format. It loads FITS files containing data cubes, and each frame of the animation displays a slice of the data cube at a specific time index.
- **Instructions:** Customize folder paths, dimensions, and run the script.

### 4. 3D Stacked Image Visualization

- **Filename:** `create_3d_stacked_image.py`
- **Description:** This script generates a 3D stacked image visualization using a list of image files. It stacks images in 3D to visualize altitude information.
- **Instructions:** Replace image filenames, customize parameters, and run the script.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the repository directory in your terminal.
3. Follow the instructions provided for each code snippet to run the scripts.

Feel free to explore, adapt, and experiment with these code snippets to further your understanding of solar physics and data visualization!
