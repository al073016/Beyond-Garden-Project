import os
import numpy as np
import pandas as pd
from osgeo import gdal

# Carpeta con los archivos MOD11C3
folder = "/home/maoh/Earth/MOD11C3_061-20250923_232238"

# Coordenadas aproximadas de Yucatán
lat_min, lat_max = 19.0, 21.5
lon_min, lon_max = -90.5, -87.0

def process_array(ds):
    arr = ds.ReadAsArray().astype(float)
    arr[arr == 0] = np.nan  # nodata
    arr = (arr * 0.02) - 273.15  # Escala a °C
    return arr

def get_index(lat, lon, gt):
    x0, dx, _, y0, _, dy = gt
    x = int((lon - x0) / dx)
    y = int((lat - y0) / dy)
    return x, y

def classify_temp(temp):
    if np.isnan(temp):
        return "Sin datos"
    elif temp < 20:
        return "Frío"
    elif temp < 30:
        return "Templado"
    else:
        return "Caluroso"

results = []

for file in sorted(os.listdir(folder)):
    if file.endswith(".hdf"):
        filepath = os.path.join(folder, file)
        print(f"Procesando {file}...")

        try:
            subdatasets = gdal.Open(filepath).GetSubDatasets()
            lst_day_ds = gdal.Open(subdatasets[0][0])   # LST_Day_CMG
            lst_night_ds = gdal.Open(subdatasets[4][0]) # LST_Night_CMG

            lst_day = process_array(lst_day_ds)
            lst_night = process_array(lst_night_ds)

            gt = lst_day_ds.GetGeoTransform()
            x_min, y_max = get_index(lat_max, lon_min, gt)
            x_max, y_min = get_index(lat_min, lon_max, gt)

            lst_day_yuc = lst_day[y_max:y_min, x_min:x_max]
            lst_night_yuc = lst_night[y_max:y_min, x_min:x_max]

            avg_day = np.nanmean(lst_day_yuc)
            avg_night = np.nanmean(lst_night_yuc)

            # Extraer mes
            year = file.split(".")[1][1:5]
            doy = int(file.split(".")[1][5:8])  # día del año
            month = pd.to_datetime(f"{year}-{doy}", format="%Y-%j").strftime("%Y-%m")

            results.append({
                "month": month,
                "LST_Day_C": avg_day,
                "estado_dia": classify_temp(avg_day),
                "LST_Night_C": avg_night,
                "estado_noche": classify_temp(avg_night),
            })

        except Exception as e:
            print(f"Error con {file}: {e}")

# Guardar a CSV sin agrupar otra vez
df = pd.DataFrame(results)
df.to_csv("lst_yucatan_monthly.csv", index=False)

print("Resultados guardados en lst_yucatan_monthly.csv")
print(df)
