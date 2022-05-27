import pandas as pd
import numpy as np
import math

# Read in the tweet location list
locations = pd.read_csv('./locations/locations.csv')

# Read in the municipality list
municipalities = pd.read_csv('./locations/mun_list.csv')

# Subset the municipalities dataset to give just the lat, lon, and mun_id
mun_ids = municipalities[['mun_id', 'mun_X', 'mun_Y']]

# Subset the municipalities dataset to give just the lat, lon, and mun_id
municipalities_no_xy = municipalities[['mun_id', 'pref', 'municipality', 'yomigana', 'prefid']]

# Create a variable to indicate if the lat and lon for a location is missing
locations['missing_lat_lon'] = np.where(locations['centroid_lon'].isna(), True, False)

# Create a list of the municipality coordinates
municipality_coordinates = [(x,y) for x,y in zip(municipalities['mun_X'] , municipalities['mun_Y'])]

# Create an empty column for the x and y coordinates for the closest municipality to each tweet location
locations['mun_X'] = np.nan
locations['mun_Y'] = np.nan

# For each tweet, find the closest lat and lon pair and then write that pair to the mun_X and mun_Y variables
for x in range(len(locations)):
    if locations['missing_lat_lon'][x] == False:
        closest = min(municipality_coordinates, key=lambda point: math.hypot(locations['centroid_lat'][x]-point[1], locations['centroid_lon'][x]-point[0]))
        locations['mun_X'][x] = closest[0]
        locations['mun_Y'][x] = closest[1]
        x
    else:
        print("Skipped" + str(x))
        pass

# Merge the mun_ids to the location data
locations = pd.merge(locations, mun_ids, how = 'left', on = ['mun_X', 'mun_Y'])

# Drop the mun_X, mun_Y, and missing_lat_lon variables
locations = locations.drop(columns = ['mun_X', 'mun_Y', 'missing_lat_lon'])

# For 19 of the location IDs, city names were provided by the API but no latitude or longitude. I have found these cities in the mun_list dataset and
# manually set the mun_id variable below

locations.loc[(locations.tweet_location_id == 'adadb707dc48544a'),'mun_id'] = 261009
locations.loc[(locations.tweet_location_id == '780965936519e2cf'),'mun_id'] = 141003
locations.loc[(locations.tweet_location_id == '3c4ec10c90f4ed0d'),'mun_id'] = 221309
locations.loc[(locations.tweet_location_id == '3d77e5bd7f2d57bc'),'mun_id'] = 11002
locations.loc[(locations.tweet_location_id == '20bf61156942a95b'),'mun_id'] = 271004
locations.loc[(locations.tweet_location_id == '61bf1a5d65ddcaba'),'mun_id'] = 41009
locations.loc[(locations.tweet_location_id == '909a4283eb5a02ea'),'mun_id'] = 111007
locations.loc[(locations.tweet_location_id == '281186f046f02a30'),'mun_id'] = 221007
locations.loc[(locations.tweet_location_id == '764bba3fa1deb786'),'mun_id'] = 151009
locations.loc[(locations.tweet_location_id == 'c1075df95b2727c8'),'mun_id'] = 281000
locations.loc[(locations.tweet_location_id == 'd8ad75df51286882'),'mun_id'] = 401005
locations.loc[(locations.tweet_location_id == '0ae2935fbd73ea4f'),'mun_id'] = 231002
locations.loc[(locations.tweet_location_id == 'aa569457d63246bc'),'mun_id'] = 141500
locations.loc[(locations.tweet_location_id == 'b303981889700717'),'mun_id'] = 141305
locations.loc[(locations.tweet_location_id == '83bc030c4991a8db'),'mun_id'] = 331007
locations.loc[(locations.tweet_location_id == 'ce79bed9ac07a48d'),'mun_id'] = 401307
locations.loc[(locations.tweet_location_id == '7af909158a2459e3'),'mun_id'] = 121002
locations.loc[(locations.tweet_location_id == '3c83aaf3b387003a'),'mun_id'] = 341002
locations.loc[(locations.tweet_location_id == '30712571d1d88380'),'mun_id'] = 271403

# Merge the full municipality info with the locations based on mun_id
locations = pd.merge(locations, municipalities, how = 'left', on = 'mun_id')

# Output to CSV
locations.to_csv('./locations/matched_locations.csv', index = False)