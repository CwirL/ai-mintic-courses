import os
from googlemaps import Client
from pprint import pprint
from variables import google_maps_key

gmaps = Client(key=google_maps_key)


def address_to_latlng(addr):
    response = gmaps.geocode(addr)[0]
    location = response['geometry']['location']

    addr_comp = response['address_components']
    print(addr, addr_comp[len(addr_comp) - 1]['long_name'], location)
    return location
