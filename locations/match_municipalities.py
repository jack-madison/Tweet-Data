import pandas as pd
import numpy as np
import math

# Read in the tweet location list
locations = pd.read_csv('./locations/locations.csv')

# Read in the municipality list
municipalities = pd.read_excel('./locations/mun_list.xlsx')

# Create a list of the municipality coordinates
municipality_coordinates = [(x,y) for x,y in zip(municipalities['mun_X'] , municipalities['mun_Y'])]

# Create an empty column for the x and y coordinates for the closest municipality to each tweet location
locations['mun_X'] = np.nan
locations['mun_Y'] = np.nan

# For each tweet, find the closest lat and lon pair and then write that pair to the mun_X and mun_Y variables
for x in range(len(locations)):
    closest = min(municipality_coordinates, key=lambda point: math.hypot(locations['centroid_lat'][x]-point[1], locations['centroid_lon'][x]-point[0]))
    locations['mun_X'][x] = closest[0]
    locations['mun_Y'][x] = closest[1]
    x

# Merge the municipality info with the tweet info
locations = pd.merge(locations, municipalities, how = 'left', on = ['mun_X', 'mun_Y'])

# Output to CSV
locations.to_csv('./locations/matched_locations.csv', index = False)