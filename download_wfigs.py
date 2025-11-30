import requests
import os

def download_wfigs(output_path="data/raw/wfigs/wfigs.geojson"):
    url = "https://opendata.arcgis.com/api/v3/datasets/nifc::wfigs-interagency-fire-perimeters/download?format=geojson"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("Downloading WFIGS fire perimeters...")
    r = requests.get(url, stream=True)
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved WFIGS fire perimeters to {output_path}")

if __name__ == "__main__":
    download_wfigs()
