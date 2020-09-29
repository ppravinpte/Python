""" Webmap to display Volcano locations and population with markers and polygon layer.
1)Created webmap to display volcanoes location in US as per file Volcanoes.txt. 
Location markers are displayed with different colors as per height range
2) Used world.json file to add polygon layers to all countries.
3)Two feature group added with layer control. It allows to toggle between two mapsets"""
import folium
import pandas

map = folium.Map(location=[35.0, -121], zoom_start=4, tiles= "stamen Terrain")
file1 = pandas.read_csv('Volcanoes.txt')
lattitude = list(file1["LAT"])
longitude = list(file1["LON"])
elevation = list(file1["ELEV"])

def get_color(height):
    if height < 1000:
        #color_inp = 'green'
        return 'green'
    elif 1000 < height < 4000:
        #color_inp = 'blue'
        return 'blue'
    else:
        #color_inp = 'red'
        return 'red'
    #return color_inp1


fgvolcanoes = folium.FeatureGroup(name="US Volcanoes")

for lat,lon,elev in zip(lattitude, longitude, elevation):
    fgvolcanoes.add_child(folium.Marker(location=[lat,lon], popup ='Height:'+str(elev)+' m', icon=folium.Icon(color=get_color(elev))))

fgworldpop = folium.FeatureGroup(name="World Population")

fgworldpop.add_child(folium.GeoJson(data=open('world.Json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<100000000
    else 'orange' if 100000000 <= x['properties']['POP2005'] < 200000000
    else 'red'}))

map.add_child(fgvolcanoes)
map.add_child(fgworldpop)
map.add_child(folium.LayerControl())

map.save("webmap.html")
