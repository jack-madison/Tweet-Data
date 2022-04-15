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

client = tweepy.Client(bearer_token_1, wait_on_rate_limit=True)

pollen_tweets = []

for response in tweepy.Paginator(client.search_all_tweets, 
                                query = '((花粉) OR (花粉症) OR (スギ花粉)) -is:retweet -is:nullcast has:geo place_country:JP',
                                tweet_fields = ['author_id', 'created_at', 'geo', 'id', 'lang', 'public_metrics', 'source', 'text'],
                                start_time = '2006-03-22T00:00:00+09:00',
                                end_time = '2022-01-01T00:00:00+09:00',
                                max_results=500):
    time.sleep(1)
    pollen_tweets.append(response)

result = []

# Loop through each response object
for response in pollen_tweets:
    for tweet in response.data:
        try:
            # Put all of the information we want to keep in a single dictionary for each tweet
            result.append({
                    'author_id': tweet.author_id,
                    'tweet_text': tweet.text,
                    'tweet_created_at': tweet.created_at,
                    'tweet_location_id': tweet.geo['place_id']
                    })
        except TypeError:
            print("Type Error")
        except KeyError:
            print("Key Error")

# Change this list of dictionaries into a dataframe
tweets = pd.DataFrame(result)

# Save the tweets as a CSV
tweets.to_csv('./pollen_tweets/pollen_tweets.csv', index = False)















# Extract the unique location IDs
locations = tweets['tweet_location_id'].unique().tolist()

# Specify the barer token for the geo location id search
headers = {"Authorization": "Bearer {}".format(bearer_token)}

# Create an empty dictionary
location_dict = []

# Pull the location info from the twitter API and write it to the location_dict dictionary
for x in locations:
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
df_locations = pd.DataFrame(location_dict)

# Merge the locations and tweets dataframes
tweets_location = pd.merge(tweets, df_locations, how='left', on='tweet_location_id')

# Filter the new tweets data to not include tweets that lack a location lat and lon or if the location is at the prefecture or country level
tweets_location = tweets_location[tweets_location['centroid_lon'].notna()]
tweets_location = tweets_location[(tweets_location['place_type'] != 'admin') & (tweets_location['place_type'] != 'country')]

# Reset the index of the tweets_location dataframe
tweets_location = tweets_location.reset_index(drop=True)

# Read in the municipality list
municipalities = pd.read_excel('./symptoms_tweets/mun_list.xlsx')

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
tweets_location.to_csv('./pollen_tweets/pollen_tweets_with_locations.csv', index = False)