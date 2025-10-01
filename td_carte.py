import folium
from folium import plugins
from folium.plugins import BeautifyIcon
import pandas as pd
import webbrowser
import numpy as np
from folium.plugins import FloatImage
from folium.features import DivIcon

F_in_StationLocations = "U:/Documents/BUT3/SAE/SAE_Asie/DataForTP_20231022/StationsLocation.xlsx"
F_out = "U:/Documents/BUT3/SAE/SAE_Asie/ManausMap.html"
df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

study_zone_map = folium.Map(location=[-3.1190, -60.0217],
tiles = 'OpenStreetMap',
width="100%",height="100%",)

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',
background_color='transparent', border_color='transparent',)

# add the icon to the map
folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],
tooltip="Click me!",
popup='Meteorological Station',
icon=icon_star,).add_to(study_zone_map)



for i in range(8) :
    folium.Circle(location=[df_StationsLocation['Lat'][i],df_StationsLocation['Lon'][i]],
    tooltip="Click me!",
    popup=df_StationsLocation['Label'][i],
    color='crimson',fill=True,radius=500).add_to(study_zone_map)


folium.map.Marker(
location=[df_airport.latitude.values,df_airport.longitude.values],
icon=DivIcon(icon_size=(150,36),
icon_anchor=(0,0),
html='Meteorological Station',)
).add_to(study_zone_map)




minimap = plugins.MiniMap(zoom_level_offset=-7)
study_zone_map.add_child(minimap)

legend_html = '''
    Meteorological Station
    Sample Location
'''
study_zone_map.get_root().html.add_child(folium.Element(legend_html))

study_zone_map.control_scale = True

north_arrow_url = 'https://upload.wikimedia.org/wikipedia/commons/8/84/North_Pointer.svg'
# Add the north arrow image to the map
FloatImage(north_arrow_url,
bottom=75, left=85,scale=0.2).add_to(study_zone_map)


study_zone_map.save(F_out)
webbrowser.open(F_out)

