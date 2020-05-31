import folium       #folium is used on an interactive leaflet map. It enables both the binding of data to a map.Folium is a third party library
                    #third party means which I install from net.
import pandas       #Pandas is a module & manipulation tool.
data = pandas.read_csv("Volcanoes.txt")  #The csv module implements classes to read and write tabular data in CSV format
lat = list(data["LAT"]) #latitude is a distance of north or south. Latitude& longitude are geographical coordinates
lon = list(data["LON"]) #longitude is a distance of east or west
elev = list(data["ELEV"])
def country_color(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <=elevation <3000:
        return 'red'
    else:
        return 'green'
map = folium.Map(location = [38.58, -99.09],zoom_start = 6,tiles = "Stamen Terrain")     #tiles is background of map."map" is object & "Map" is class. [LAT=38.58,LON= -99.09]
country = folium.FeatureGroup(name = "Country") #this "Country" stays at the right side of the map as an option "
for lt,ln,el in zip(lat,lon,elev):  #zip is a function which join two tuples together
    country.add_child(folium.Marker(location=[lt,ln],radius = 6,popup=str(el)+"m distance",
    fill_color = country_color(el),color = "gray", fill_opacity = 0.7))
population = folium.FeatureGroup(name = "Population")   #this "Population" stays at the right side of the map as an option "
population.add_child(folium.GeoJson(data = open("world.json","r",encoding = "utf-8-sig").read(), #JSON is a syntax for storing and exchanging data.JSON is text, written with JavaScript object notation.
style_function = lambda x:{'fillColor':'red' if x['properties']['POP2005'] < 10000000            #'POP2005' means population of 2005
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'yellow'}))
map.add_child(country)
map.add_child(population)
map.add_child(folium.LayerControl())
map.save("Map1.html")