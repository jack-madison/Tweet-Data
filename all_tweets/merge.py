# The following python code merges the tweet data. I decided to pull the data in smaller
# batches to aviod going over the rate limit and losing the entire dataframe.

import pandas as pd
import numpy as np

apr1_7 = pd.read_csv('./all_tweets/tweet_data/2020/apr1_7.csv')
apr8_14 = pd.read_csv('./all_tweets/tweet_data/2020/apr8_14.csv')
apr15_21 = pd.read_csv('./all_tweets/tweet_data/2020/apr15_21.csv')
apr22_30 = pd.read_csv('./all_tweets/tweet_data/2020/apr21_30.csv')

april = apr1_7.append(apr8_14)
april = april.append(apr15_21)
april = april.append(apr22_30)

april = april.drop_duplicates()

april = april.sort_values(by = 'tweet_created_at')

april = april.reset_index(drop = True)

april.to_csv('./all_tweets/tweet_data/2020/apr_2020.csv')