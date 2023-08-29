# Solar Physics Project Code Repository

Welcome to the Solar Physics Project Code Repository! This repository contains Python scripts for analyzing solar data, creating animations, and generating visualizations. Below, you'll find descriptions and instructions for running each code snippet.

# Introduction

Enhanced power of high-frequency waves surrounding strong-magnetic field structures observed in the Solar Atmosphere.
This excess power is known as "Acoustic Halo", first observed in early 1990’s at photospheric (Brown et al., 1992) as well as chromospheric (Braun et al., 1992) heights, at frequencies above the photospheric cut-off of ≈ 5.3 mHz, in the range of 5.5 - 7 mHz, and over regions of weak to intermediate strength (50 - 250 G) photospheric magnetic field.

This repository contains the codes to visualize this phenomenon.
The data used here are of 2 types: 
1) .fits data from JSOC client
2) .sav data generated with IDL data co-aligning routine which corrects for the Sun's rotation

The data that I used for my project are taken by SDO space telescope, which contains **HMI Dopplergram, HMI Continuum, Vector Magnetogram, AIA 1700 and 1600 angstrom data.**




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
- **Data:** Vector magnetogram data along with respective uncertainties. Inclination is w.r.t line of sight.
- **Instructions:** Customize folder paths as needed and run the script.

### 3. FITS Data Animation

- **Filename:** `fits_data_animation.py`
- **Description:** This script creates an animation from time series data in FITS format. It loads FITS files containing data cubes, and each frame of the animation displays a slice of the data cube at a specific time index.
- **Instructions:** Customize folder paths, dimensions, and run the script.

### 4. 3D Stacked Image Visualization

- **Filename:** `create_3d_stacked_image.py`
- **Description:** This script generates a 3D stacked image visualization using a list of image files. It stacks images in 3D to visualize altitude information.
- **Instructions:** Replace image filenames, customize parameters, and run the script.

### 5. Scatter plots of power and field parameters
- **Filename:** `scatter_plots_of_power_and_field_parameters.py`
- **Description:** This script will make scatter plots to visualize the dependancy of Power emitted on Magnetic field strength and inclination. The data given to the code is in .sav format containing information Field strength, inclination with respective errors and x and y centre values.
- **Instructions:**  To find the central inclination value, full disk data has to be given to the code.
- **Data:** Vector magnetogram data along with respective uncertainties. Inclination is w.r.t line of sight.

### 6. Download Full disk data
- **Filename:** `download_solar_data.py`
- **Description:** This script uses the SunPy library to search for solar data on the JSOC server within a specific time range, based on instrument, sample rate, and physical observable. It then downloads the matched files and saves them to the specified local path. Make sure to have the necessary libraries (sunpy, astropy, etc.) installed before running this script.
- **Instructions:** To find the syntax for choosing differrent time of observation, use this link https://docs.sunpy.org/en/stable/tutorial/acquiring_data/index.html#sunpy-tutorial-acquiring-data-index
- **Data:** Full disk data will be downloaded with an image size of 4000 $\times$ 4000.

## Usage
1. Make sure you have the required libraries installed. You can install them using the following command:
   ```bash
   pip install sunpy astropy glob2 matplotlib drms zeep 


## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the repository directory in your terminal.
3. Follow the instructions provided for each code snippet to run the scripts.

## Contributing

Contributions to this repository are welcome! If you have improvements, bug fixes, or additional features to suggest, feel free to open an issue or submit a pull request. Please follow the existing code style and conventions.


Feel free to explore, adapt, and experiment with these code snippets to further your understanding of solar physics and data visualization!
For questions or further information, please contact Karthik at ksb990200@gmail.com.

