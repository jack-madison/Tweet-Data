import pandas as pd
import time
import requests

#Import the bearer tokens
from twitter_authentication import bearer_token_1
from twitter_authentication import bearer_token_2
from twitter_authentication import bearer_token_3
from twitter_authentication import bearer_token_4
from twitter_authentication import bearer_token_5
from twitter_authentication import bearer_token_6
from twitter_authentication import bearer_token_7
from twitter_authentication import bearer_token_8

# Read in the CSV of tweets
tweets = pd.read_csv('./cognition_tweets/cognition_tweets.csv')

# Read in the dataframe of locations already collected
locations = pd.read_csv('./locations/locations.csv')

# Extract the unique location IDs
tweet_location_ids = tweets['tweet_location_id'].unique().tolist()

# Get a list of the already collected location ids
location_ids = locations['tweet_location_id'].unique().tolist()

# Remove the location_ids that have already been collected from the tweet_location_ids list
tweet_location_ids = list(set(tweet_location_ids) - set(location_ids))

# Check to see how many unique ids there are
len(tweet_location_ids)

# Initialize the counter for the barer tokens
token_no = 0

# Create a list of barer tokens
bearer_tokens = [bearer_token_1, bearer_token_2, bearer_token_3, bearer_token_4, bearer_token_5, bearer_token_6, bearer_token_7, bearer_token_8]

# Create an empty dictionary
location_dict = []

# Pull the location info from the twitter API and write it to the location_dict dictionary
for x in tweet_location_ids:
    if token_no > 7: token_no = 0
    try:
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
        print(x)
        print(bearer_tokens[token_no])
    except:
        print("An error occured")
        time.sleep(60)
        pass
    token_no = token_no + 1
    time.sleep(2)

# Turn the dictionary into a dataframe
tweet_location_df = pd.DataFrame(location_dict)

# Append to the locations dataframe
locations = locations.append(tweet_location_df)

# Save the locations df
locations.to_csv('./locations/locations.csv', index = False)