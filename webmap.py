import folium

fg = folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(date =(open("india_states.json" , "r" ,encoding="utf-8-sig").read())))


map = folium.Map(location =(20.0000,75.0000),zoom_start = 4)
map.add_child(fg)
map.save("sample.html")