import os
import glob
import numpy as np
import pandas as pd
from osgeo import gdal

# Carpeta con los archivos HDF
data_dir = "/home/maoh/Earth/MYD13C2_061-20250924_010142"

# Coordenadas aproximadas Península de Yucatán
lat_min, lat_max = 17.5, 22.5
lon_min, lon_max = -92.5, -86.0

# Función para clasificar NDVI
def classify_ndvi(value):
    if np.isnan(value):
        return "Sin datos"
    elif value < 0.2:
        return "Bajo"
    elif value < 0.5:
        return "Moderado"
    else:
        return "Alto"

results = []

# Recorremos todos los archivos HDF en la carpeta
for file in sorted(glob.glob(os.path.join(data_dir, "*.hdf"))):
    print(f"Procesando: {os.path.basename(file)}")

    # Abrir dataset y seleccionar el subdataset de NDVI
    hdf = gdal.Open(file)
    ndvi_subdataset = [
        s for s in hdf.GetSubDatasets() if "CMG 0.05 Deg Monthly NDVI" in s[0]
    ][0][0]

    ndvi_ds = gdal.Open(ndvi_subdataset)
    ndvi_array = ndvi_ds.ReadAsArray().astype(float)

    # Reemplazar valores de "sin datos" (-3000)
    ndvi_array[ndvi_array == -3000] = np.nan

    # Aplicar factor de escala
    ndvi_array = ndvi_array * 0.0001

    # Extraer info geoespacial
    gt = ndvi_ds.GetGeoTransform()
    lon0, dx, _, lat0, _, dy = gt

    # Índices de la Península de Yucatán
    x_min = int((lon_min - lon0) / dx)
    x_max = int((lon_max - lon0) / dx)
    y_min = int((lat_max - lat0) / dy)
    y_max = int((lat_min - lat0) / dy)

    region = ndvi_array[y_min:y_max, x_min:x_max]

    # Calcular promedio
    ndvi_mean = np.nanmean(region)

    # Clasificar
    estado = classify_ndvi(ndvi_mean)

    # Extraer fecha del nombre del archivo (ejemplo: A2024001 → 2024-01)
    fname = os.path.basename(file)
    year = fname[9:13]
    doy = int(fname[13:16])
    month = pd.to_datetime(f"{year}-{doy}", format="%Y-%j").month

    results.append({"year": int(year), "month": month,
                   "NDVI": ndvi_mean, "estado": estado})

# Guardar resultados en CSV
df = pd.DataFrame(results)
df.to_csv("NDVI_Yucatan_MODIS.csv", index=False)

print("Listo: NDVI_Yucatan_MODIS.csv generado.")
