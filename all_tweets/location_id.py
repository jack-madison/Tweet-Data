import pandas as pd
import numpy as np
import time
import requests

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token

# Download the tweets data from GitHub
tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/all_tweets/tweet_data/2020/feb_2020.csv')

# Pull the unique tweet location IDs from the tweets dataframe
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
    time.sleep(12)

# Turn the dictionary into a dataframe
df_locations = pd.DataFrame(location_dict)

