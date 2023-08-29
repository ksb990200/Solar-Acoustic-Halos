# Import necessary libraries
import sunpy
from sunpy.net import Fido, attrs as a

# Initialize JSOC client
client = sunpy.net.jsoc.JSOCClient()

# Selecting the time of observation using Fido search
result = Fido.search(a.Time('2023/08/05', '2018/12/31'), a.Instrument.hmi, a.Sample(1440*u.minute), a.Physobs('intensity'))

# Download the files locally
downloaded_files = Fido.fetch(result, path='D:/Solar Physics project data/Sunspots_ML/New folder')

# Display the list of downloaded files
print("Downloaded files:")
for file in downloaded_files:
    print(file)
