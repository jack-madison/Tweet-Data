import pandas as pd
import numpy as np
import time
import tweepy
import requests
from twitter_authentication import bearer_token

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

symptoms_tweets = []

for response in tweepy.Paginator(client.search_all_tweets, 
                                query = '-is:retweet -is:nullcast has:geo place_country:JP',
                                tweet_fields = ['author_id', 'created_at', 'geo', 'id', 'lang', 'public_metrics', 'source', 'text'],
                                start_time = '2020-02-01T00:00:00+09:00',
                                end_time = '2020-02-07T00:00:00+09:00',
                                max_results=500):
    time.sleep(1)
    symptoms_tweets.append(response)

result = []

# Loop through each response object
for response in symptoms_tweets:
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
# Change this list of dictionaries into a dataframe
tweets = pd.DataFrame(result)

# Extract all the unique location IDs and write them to a list
location_list = tweets['tweet_location_id'].unique().tolist()

# Specify the barer token for the geo location ID search
headers = {"Authorization": "Bearer {}".format(bearer_token)}

# Create an empty dictionary
location_dict = []

# Loop over the location IDs and pull the location info from the twitter API
for x in location_list:
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

# Write the location info to a dataframe
locations = pd.DataFrame(location_dict)

# Save the location info to a CSV
locations.to_csv('./locations.csv', index = False)

# Left join the location info with the tweet data
tweets = pd.merge(tweets, locations, how='left', on='tweet_location_id')

# Save the data to a CSV
tweets.to_csv('./tweet_data/2020/feb1_7.csv', index = False)