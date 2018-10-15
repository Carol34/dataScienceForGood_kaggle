import numpy as np
import geopandas as gpd
from geopandas.tools import sjoin
from matplotlib import pyplot as plt
import pandas as pd
from shapely.geometry import Point
import shapefile as shp
import matplotlib.pyplot as plt

NAD1983 = 'PROJCS["NAD_1983_StatePlane_Texas_Central_FIPS_4203_Feet",GEOGCS["GCS_North_American_1983",DATUM["North_American_Datum_1983",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["False_Easting",2296583.333333333],PARAMETER["False_Northing",9842499.999999998],PARAMETER["Central_Meridian",-100.3333333333333],PARAMETER["Standard_Parallel_1",30.11666666666667],PARAMETER["Standard_Parallel_2",31.88333333333333],PARAMETER["Latitude_Of_Origin",29.66666666666667],UNIT["Foot_US",0.30480060960121924],AUTHORITY["EPSG","102739"]]'

# Create new directory for 37-00027
try:
    mkdir -p ./new/dept_37-00027   # Using a magic shell command instead of Python
    print("This is fine.")
except:
    next
    

# Create new PRJ file
with open('./new/dept_37-00027/APB_DIST.prj', 'w') as outfile:
    outfile.write(NAD1983)


# Copy the rest of the shapefiles
try:
    cp ../37-00027_Shapefiles/* ./new/dept_37-00027/ # Using a magic shell command instead of Python
except:
    next


# Read shape file
df = gpd.read_file('./new/dept_37-00027/APD_DIST.shp')


# Save and reopen with new projection
df.to_file(filename='./new/dept_37-00027/APD_DIST.shp',driver='ESRI Shapefile',crs_wkt=NAD1983)
df = gpd.read_file('./new/dept_37-00027/APD_DIST.shp')
print(df.crs)
df = df.to_crs(epsg=4326)
print(df.crs)