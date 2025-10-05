import xarray as xr
import pandas as pd
from pathlib import Path

# Ubicaciopn del dataset
data_dir = Path.home() / "Earth" / "GPM_3IMERGDF_07-20250922_233850"

# Coordenadas de la peninsula
lat_min, lat_max = 17.5, 22.5
lon_min, lon_max = -92.5, -86.0

dfs = []

for file in sorted(data_dir.glob("*.nc4")):
    ds = xr.open_dataset(file)

    # Variable principal: precipitación diaria (mm/día)
    precip = ds["precipitation"]

    # Recorta a la Península y calcula promedio espacial
    region = precip.sel(lat=slice(lat_min, lat_max),
                        lon=slice(lon_min, lon_max))
    mean_precip = region.mean(dim=["lat", "lon"])

    # Convierte a DataFrame
    df = mean_precip.to_dataframe().reset_index()
    dfs.append(df)

# Unir todos los días
data = pd.concat(dfs).sort_values("time").reset_index(drop=True)

# Clasificar días lluviosos
data["rain_flag"] = (data["precipitation"] >= 1).astype(int)

# Categorías de intensidad
def classify_rain(x):
    if x < 1:
        return "No rain"
    elif x < 5:
        return "Light"
    elif x < 20:
        return "Moderate"
    else:
        return "Heavy"

data["rain_intensity"] = data["precipitation"].apply(classify_rain)

# Extraer mes
data["month"] = data["time"].dt.month

# Exportar CSV diario
data.to_csv("IMERG_2024_Yucatan.csv", index=False)

# Probabilidades por mes
monthly = data.groupby("month").agg(
    prob_rain=("rain_flag", "mean"),
    light=("rain_intensity", lambda x: (x=="Light").mean()),
    moderate=("rain_intensity", lambda x: (x=="Moderate").mean()),
    heavy=("rain_intensity", lambda x: (x=="Heavy").mean())
).reset_index()

# Exportar CSV mensual
monthly.to_csv("IMERG_2024_Yucatan_probs.csv", index=False)

print("Listo: CSV diario y mensual con probabilidades e intensidades generados.")
