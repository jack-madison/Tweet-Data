import pandas as pd
import time
import requests

#Import the bearer tokens
from twitter_authentication import bearer_token_4
from twitter_authentication import bearer_token_5
from twitter_authentication import bearer_token_6
from twitter_authentication import bearer_token_7

# Read in the CSV of tweets
print("Downloading February")
feb_tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2019/02_2019.csv')
print("Done!")
print("Downloading March")
mar_tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2019/03_2019.csv')
print("Done!")
print("Downloading April")
apr_tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2019/04_2019.csv')
print("Done!")
print("Downloading May")
may_tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2019/05_2019.csv')
print("Done!")
print("Downloading June")
jun_tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2019/06_2019.csv')
print("Done!")

# Extract the unique loaction IDs
feb_location_ids = feb_tweets['tweet_location_id'].unique().tolist()
mar_location_ids = mar_tweets['tweet_location_id'].unique().tolist()
apr_location_ids = apr_tweets['tweet_location_id'].unique().tolist()
may_location_ids = may_tweets['tweet_location_id'].unique().tolist()
jun_location_ids = jun_tweets['tweet_location_id'].unique().tolist()

# Create a master list
location_ids = feb_location_ids + mar_location_ids + apr_location_ids + may_location_ids + jun_location_ids
location_ids_set = set(location_ids)
location_ids_unique = list(location_ids_set)

# Read in the dataframe of locations already collected
locations = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/locations/locations.csv')

# Save the old locations list as a CSV
locations.to_csv('./old_locations.csv')

# Get a list of the already collected location ids
location_ids = locations['tweet_location_id'].unique().tolist()

# Remove the location_ids that have already been collected from the tweet_location_ids list
location_ids_unique = list(set(location_ids_unique) - set(location_ids))

# Initialize the counter for the barer tokens
token_no = 0

# Create a list of barer tokens
bearer_tokens = [bearer_token_4, bearer_token_5, bearer_token_6, bearer_token_7]

# Create an empty dictionary
location_dict = []

# Pull the location info from the twitter API and write it to the location_dict dictionary
for x in location_ids_unique:
    if token_no > 3: token_no = 0
    url = "https://api.twitter.com/1.1/geo/id/" + str(x) + ".json"
    headers = {"Authorization": "Bearer {}".format(bearer_tokens[token_no])}
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
    bearer_tokens[token_no]
    token_no = token_no + 1
    time.sleep(4)

# Turn the dictionary into a dataframe
tweet_location_df = pd.DataFrame(location_dict)

# Append the newly collected locations to the location df
locations = locations.append(tweet_location_df)

# Save the locations df
locations.to_csv('./locations.csv', index = False)

# Print to the console that the code is finished
print("Done!")