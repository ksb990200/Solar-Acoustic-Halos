# Import necessary libraries
import sunpy
from sunpy.net import Fido, attrs as a

# Initialize JSOC client
client = sunpy.net.jsoc.JSOCClient()

# Selecting the time of observation using Fido search
# here we download 1 hr data, in AIA 1700 angstrom range
# further information on syntax can be found here
# https://docs.sunpy.org/en/stable/tutorial/acquiring_data/index.html#sunpy-tutorial-acquiring-data-index
result = Fido.search(a.Time('2023/08/05 04:00:00', '2023/08/05 04:59:59'), a.Instrument.aia,a.Wavelength(1700*u.angstrom))

# Download the files locally
downloaded_files = Fido.fetch(result, path='data_folder')

# Display the list of downloaded files
print("Downloaded files:")
for file in downloaded_files:
    print(file)
