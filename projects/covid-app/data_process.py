import os
from os import path
import numpy as np
import pandas as pd
from geolocation_data import address_to_latlng


def load_data():
    filename = path.join(os.getcwd(), 'projects', 'datasets', 'Casos_positivos_de_COVID-19_en_Colombia.csv')
    headers = ['id', 'notification-date', 'divipola-code', 'city', 'department',
               'status', 'age', 'sex', 'type', 'state',
               'procedence-country', 'fis', 'dead-date', 'diagnostic-date',
               'recovery-date', 'report-date', 'recovery-type', 'department-code',
               'country-code', 'ethnicity', 'ethnic-group-name']
    data = pd.read_csv(filename, header=None, names=headers)
    data.drop([0], inplace=True)
    return data


def city_location():
    # data = load_data()
    # cities = data["city"].value_counts(dropna=True)
    cities = ['Bogotá D.C.', 'Barranquilla', 'Cali', 'Medellin']
    locations = []
    for city in cities:
        locations.append(address_to_latlng(city))
    print(locations)


if __name__ == "__main__":
    city_location()
