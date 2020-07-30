import os
import pandas as pd

### Importing and exporting
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv('url', header=None)
headers = [
    "symboling",
    "normalized_losses",
    "make",
    "fuel_type",
    "aspiration",
    "number_of_doors",
    "body_style",
    "drive_wheels",
    "engine_location",
    "wheel_base",
    "length",
    "width",
    "height",
    "curb_weight",
    "engine_type",
    "number_of_cylinders",
    "engine_size",
    "fuel_system",
    "bore",
    "stroke",
    "compression_ratio",
    "horsepower",
    "peak_rpm",
    "city_mpg",
    "highway_mpg",
    "price"]
df.columns = headers
print(df.dtypes)
print(df["engine_size"])
print(df["engine_size"][df["engine_size"] > 130])
# df.to_csv("./test.csv")

# Analyzing Data in Python
df.describe(include="all")
# df.info()
