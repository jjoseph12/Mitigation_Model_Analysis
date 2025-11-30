import cdsapi
import os

def download_era5(year=2022, region=[-125, 32, -113, 43],
                  output_path="data/raw/era5/era5.nc"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                '2m_temperature', 'total_precipitation',
                '10m_u_component_of_wind', '10m_v_component_of_wind'
            ],
            'year': str(year),
            'month': [f"{m:02d}" for m in range(1, 13)],
            'day': [f"{d:02d}" for d in range(1, 32)],
            'time': [f"{h:02d}:00" for h in range(0, 24)],
            'area': region
        },
        output_path
    )
    print(f"Saved ERA5 to {output_path}")

if __name__ == "__main__":
    download_era5()
