import folium
from folium import plugins
from folium.plugins import BeautifyIcon
import pandas as pd
import webbrowser
import numpy as np
from folium.plugins import FloatImage
from folium.features import DivIcon

F_in_StationLocations = "U:/Documents/BUT3/SAE/SAE_Asie/DataForTP_20231022/StationsLocation.xlsx"
F_out = "U:/Documents/BUT3/SAE/SAE_Asie"
df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),
    columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
                    tiles = 'OpenStreetMap',
                    width="100%",height="100%",)

study_zone_map.save(F_out)