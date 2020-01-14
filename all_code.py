!pip install geopy

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
