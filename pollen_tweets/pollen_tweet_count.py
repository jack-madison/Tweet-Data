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

for response in tweepy.Paginator(client.get_all_tweets_count, 
                                query = '((花粉) OR (花粉症) OR (スギ花粉)) -is:retweet -is:nullcast has:geo place_country:JP',
                                granularity = 'day',
                                start_time = '2006-03-22T00:00:00+09:00',
                                end_time = '2022-01-01T00:00:00+09:00'):
    time.sleep(1)
    pollen_tweets.append(response)

result = []

# Loop through each response object
for response in pollen_tweets:
    for i in response.data:
        try:
            # Put all of the information we want to keep in a single dictionary for each tweet
            result.append({
                    'end': i['end'],
                    'start': i['start'],
                    'tweet_count': i['tweet_count']
                    })
        except TypeError:
            print("Type Error")
        except KeyError:
            print("Key Error")

# Change this list of dictionaries into a dataframe
tweets = pd.DataFrame(result)





pollen_tweets_no_location = []

for response in tweepy.Paginator(client.get_all_tweets_count, 
                                query = '((花粉) OR (花粉症) OR (スギ花粉)) -is:retweet -is:nullcast',
                                granularity = 'day',
                                start_time = '2006-03-22T00:00:00+09:00',
                                end_time = '2022-01-01T00:00:00+09:00'):
    time.sleep(1)
    pollen_tweets_no_location.append(response)

result_no_location = []

# Loop through each response object
for response in pollen_tweets_no_location:
    for i in response.data:
        try:
            # Put all of the information we want to keep in a single dictionary for each tweet
            result_no_location.append({
                    'end': i['end'],
                    'start': i['start'],
                    'tweet_count': i['tweet_count']
                    })
        except TypeError:
            print("Type Error")
        except KeyError:
            print("Key Error")

# Change this list of dictionaries into a dataframe
tweets_no_location = pd.DataFrame(result_no_location)

all_tweets = pd.merge(tweets, tweets_no_location, how = 'right', on = ['end', 'start'])

all_tweets = all_tweets.rename(columns={'end': 'end', 'start': 'start', 'tweet_count_x': 'geotagged_tweets', 'tweet_count_y': 'all_tweets'})

all_tweets.to_csv('./pollen_tweets/pollen_tweet_counts.csv', index = False)



tweets = pd.read_csv('./pollen_tweets/pollen_tweets.csv')

tweets = tweets.drop_duplicates()

tweets.to_csv('./pollen_tweets/pollen_tweets_drop_dup.csv', index = False)