import pandas as pd
import numpy as np
import time
import tweepy
import requests
import math

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token

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
headers = {"Authorization": "Bearer {}".format(bearer_token)}

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