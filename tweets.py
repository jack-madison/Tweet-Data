import pandas as pd
import numpy as np
import time
import tweepy
import requests

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

symptoms_tweets = []

for response in tweepy.Paginator(client.search_all_tweets, 
                                query = '-is:retweet -is:nullcast has:geo place_country:JP',
                                tweet_fields = ['author_id', 'created_at', 'geo', 'id', 'lang', 'public_metrics', 'source', 'text'],
                                start_time = '2020-03-08T00:00:00+09:00',
                                end_time = '2020-03-14T23:59:59+09:00',
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

tweets.to_csv('./tweet_data/2020/mar8_14.csv', index = False)