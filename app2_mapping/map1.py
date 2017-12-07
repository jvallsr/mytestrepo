import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map([38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg1 = folium.FeatureGroup("Volcanoes")
# Points layer
for i, j, k, l in zip(lat, lon, name, elev):
    fg1.add_child(folium.CircleMarker(location=[i, j],
    radius=6, color=color_producer(l), fill=True, fill_opacity=0.7,
    popup=folium.Popup(k+" "+str(l)+" m", parse_html=True)))

fg2 = folium.FeatureGroup("Population")
# Polygons choropleth layer
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())

map.save("Map1.html")
