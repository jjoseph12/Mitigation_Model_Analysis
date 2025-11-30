import os
import rasterio
from rasterio.enums import Resampling
import requests

# Example NLCD link for CONUS
NLCD_URL = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/ows?service=WCS&version=1.0.0&request=GetCoverage&coverage=NLCD_2019_Land_Cover_L48&format=GeoTIFF"

def download_nlcd(output_path="data/raw/nlcd/nlcd.tif"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("Downloading NLCD...")
    r = requests.get(NLCD_URL, stream=True)
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    print("Saved NLCD")

if __name__ == "__main__":
    download_nlcd()
