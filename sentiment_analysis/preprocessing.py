import pandas as pd
import numpy as np
import pytz

# Import all of the data for the specific year
tweets_feb = pd.read_csv('./all_tweets/tweet_data/2019/02_2019.csv')
tweets_mar = pd.read_csv('./all_tweets/tweet_data/2019/03_2019.csv')
tweets_apr = pd.read_csv('./all_tweets/tweet_data/2019/04_2019.csv')
tweets_may = pd.read_csv('./all_tweets/tweet_data/2019/05_2019.csv')
tweets_jun = pd.read_csv('./all_tweets/tweet_data/2019/06_2019.csv')

# Congatinate the data into one dataframe
tweets = pd.concat([tweets_feb, tweets_mar, tweets_apr, tweets_may, tweets_jun], axis = 0, join = 'outer')

# Remove duplicate tweets that could show up in the data collection process
tweets = tweets.drop_duplicates()

# Import the location dataset
locations = pd.read_csv('./locations/matched_locations.csv')

# Add the tweet location data to the tweets data
tweets = pd.merge(tweets, locations, how = 'left', on = 'tweet_location_id')

# Remove tweets where there is no municipality attached
tweets = tweets[tweets['mun_id'].notna()]

# Remove tweets where the associated location is an administration or a country
tweets = tweets[(tweets['place_type'] != 'admin') & (tweets['place_type'] != 'country')]

# Reformat the time so that it is in local Japanese time
tweets['tweet_created_at'] = pd.to_datetime(tweets['tweet_created_at'])
tweets['tweet_created_at'] = tweets['tweet_created_at'].dt.tz_convert('Japan')

# Output the dataframe to CSV
tweets.to_csv('./all_tweets/tweet_data/2019/preprocessed_2019.csv', index=False)

