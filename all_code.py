!pip install geopy
!pip install folium
import folium

from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd

# Geocode single address
geolocator = Nominatim(timeout=10, user_agent = "myGeolocator")
location = geolocator.geocode('4550 Kester Mill Rd,Winston-Salem,NC')
print(location)
print((location.latitude, location.longitude))

# Calculate the distance b/w 2 addresses
location_1 = geolocator.geocode('11415 Quaker Ave,Lubbock,TX')
location_1_gps = (location_1.latitude, location_1.longitude)
location_2 = geolocator.geocode('4550 Kester Mill Rd,Winston-Salem,NC')
location_2_gps = (location_2.latitude, location_2.longitude)
# distance in miles
distance_calc_mi = distance.distance(location_1_gps, location_2_gps).miles
print(distance_calc_mi)
# distance in kilometers
distance_calc_km = distance.distance(location_1_gps, location_2_gps).km
print(distance_calc_km)

# Geocode in a pandas DataFrame
df = pd.read_csv('sample_addresses.csv')
df['full_address'] = df.address + "," + df.city + "," + df.state
df['gcode'] = df.full_address.apply(geolocator.geocode)
df['lat'] = [g.latitude for g in df.gcode]
df['long'] = [g.longitude for g in df.gcode]

# Map the addresses
mapa = folium.Map(location=(36.104087829589844,-86.77576446533203), zoom_start=5)
for index, row in df.iterrows():
  folium.Marker(location=(row['lat'],row['long'])).add_to(mapa)
display(mapa)
