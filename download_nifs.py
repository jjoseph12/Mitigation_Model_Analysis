import requests
import os

NIFS_URL = "https://opendata.arcgis.com/api/v3/datasets/0a4dc366e7cb4a76a8d6cb1ea2f5ba9a_0/download?format=geojson"

def download_nifs(output_path="data/raw/nifs/dozer_lines.geojson"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("Downloading NIFS dozer lines...")
    r = requests.get(NIFS_URL, stream=True)
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved NIFS dozer lines to {output_path}")

if __name__ == "__main__":
    download_nifs()
