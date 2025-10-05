import xarray as xr
import numpy as np
import pandas as pd
import glob
import os

# Carpeta donde están los .nc
folder = "/home/maoh/Earth/CYGNSS_L3_SOIL_MOISTURE_V3.2_3.2-20250923_160527"
files = sorted(glob.glob(f"{folder}/*.nc"))

def procesar(files, resolucion):
    resultados = []
    
    for file in files:
        try:
            ds = xr.open_dataset(file)
            
            # Variables
            lat = ds["latitude"].values
            lon = ds["longitude"].values
            sm = ds["SM_daily"].values
            
            # Máscara para Yucatán
            mask = (lat >= 17) & (lat <= 22.5) & (lon >= -92) & (lon <= -86)
            sm_yucatan = np.where(mask, sm, np.nan)
            sm_promedio = np.nanmean(sm_yucatan)
            
            # Fecha
            fecha = pd.to_datetime(str(ds["time"].values[0]))
            
            resultados.append({
                "time": fecha,
                "SM_daily": sm_promedio
            })
            
            ds.close()
        
        except Exception as e:
            print(f"Error con {os.path.basename(file)}: {e}")
    
    # DataFrame
    df = pd.DataFrame(resultados).dropna(subset=["SM_daily"])
    df["month"] = df["time"].dt.to_period("M")
    df_monthly = df.groupby("month")["SM_daily"].mean().reset_index()
    
    # Clasificación
    def clasificar(sm):
        if np.isnan(sm):
            return "Sin datos"
        elif sm < 0.15:
            return "Bajo"
        elif sm < 0.30:
            return "Medio"
        else:
            return "Alto"

    df_monthly["estado"] = df_monthly["SM_daily"].apply(clasificar)
    
    # Exportar
    out = f"soil_moisture_yucatan_monthly_{resolucion}.csv"
    df_monthly.to_csv(out, index=False)
    print(f"Resultados guardados en {out}")
    return df_monthly

# Dividir archivos por resolución
files_36 = [f for f in files if "36km" in f]
files_9 = [f for f in files if "9km" in f]

print(f"Procesando {len(files_36)} archivos de 36km")
df36 = procesar(files_36, "36km")

print(f"Procesando {len(files_9)} archivos de 9km")
df9 = procesar(files_9, "9km")
