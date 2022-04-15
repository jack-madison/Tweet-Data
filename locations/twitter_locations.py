import pandas as pd
import numpy as np
import time
import tweepy
import requests
import math

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token_1

# Read in the CSV of tweets
tweets = pd.read_csv('./pollen_tweets/pollen_tweets.csv')

# Read in the dataframe of locations already collected
locations = pd.read_csv('./locations/locations.csv')

# Extract the unique location IDs
tweet_location_ids = tweets['tweet_location_id'].unique().tolist()

# Get a list of the already collected location ids
location_ids = locations['tweet_location_id'].unique().tolist()

# Remove the location_ids that have already been collected from the tweet_location_ids list
tweet_location_ids = list(set(tweet_location_ids) - set(location_ids))

# Specify the barer token for the geo location id search
headers = {"Authorization": "Bearer {}".format(bearer_token_1)}

# Create an empty dictionary
location_dict = []

# Pull the location info from the twitter API and write it to the location_dict dictionary
for x in tweet_location_ids:
    url = "https://api.twitter.com/1.1/geo/id/" + str(x) + ".json"
    r = requests.get(url, headers = headers)
    json_data = r.json()
    if 'name' in json_data:
        if 'centroid' in json_data:
            location_dict.append({
                                'tweet_location_id': x,
                                'name': json_data['name'],
                                'full_name': json_data['full_name'],
                                'country': json_data['country'],
                                'country_code': json_data['country_code'],
                                'place_type': json_data['place_type'],
                                'centroid_lon': json_data['centroid'][0],
                                'centroid_lat': json_data['centroid'][1]
                                })
        else:
            location_dict.append({
                                'tweet_location_id': x,
                                'name': json_data['name'],
                                'full_name': json_data['full_name'],
                                'country': json_data['country'],
                                'country_code': json_data['country_code'],
                                'place_type': json_data['place_type']
                                })  
    else:
        location_dict.append({'tweet_location_id': x,})
    x
    time.sleep(15)

# Turn the dictionary into a dataframe
tweet_location_df = pd.DataFrame(location_dict)

# Append the newly collected locations to the location df
locations = locations.append(tweet_location_df)

# Save the locations df
locations.to_csv('./locations/locations.csv', index = False)

# Merge the locations and tweets dataframes
tweets_location = pd.merge(tweets, locations, how='left', on='tweet_location_id')

# Filter the new tweets data to not include tweets that lack a location lat and lon or if the location is at the prefecture or country level
tweets_location = tweets_location[tweets_location['centroid_lon'].notna()]
tweets_location = tweets_location[(tweets_location['place_type'] != 'admin') & (tweets_location['place_type'] != 'country')]

# Reset the index of the tweets_location dataframe
tweets_location = tweets_location.reset_index(drop=True)

# Read in the municipality list
municipalities = pd.read_excel('./locations/mun_list.xlsx')

# Create a list of the municipality coordinates
municipality_coordinates = [(x,y) for x,y in zip(municipalities['mun_X'] , municipalities['mun_Y'])]

# Create an empty column for the x and y coordinates for the closest municipality to each tweet location
tweets_location['mun_X'] = np.nan
tweets_location['mun_Y'] = np.nan

# For each tweet, find the closest lat and lon pair and then write that pair to the mun_X and mun_Y variables
for x in range(len(tweets_location)):
    closest = min(municipality_coordinates, key=lambda point: math.hypot(tweets_location['centroid_lat'][x]-point[1], tweets_location['centroid_lon'][x]-point[0]))
    tweets_location['mun_X'][x] = closest[0]
    tweets_location['mun_Y'][x] = closest[1]
    x

# Merge the municipality info with the tweet info
tweets_location = pd.merge(tweets_location, municipalities, how = 'left', on = ['mun_X', 'mun_Y'])

# Output to CSV
tweets_location.to_csv('./pollen_tweets/pollen_tweets_with_location.csv', index = False)