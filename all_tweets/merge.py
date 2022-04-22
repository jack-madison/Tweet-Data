# The following python code merges the tweet data. I decided to pull the data in smaller
# batches to aviod going over the rate limit and losing the entire dataframe.
import pandas as pd
import numpy as np

week1 = pd.read_csv('./all_tweets/tweet_data/2019/feb1_7.csv')
week2 = pd.read_csv('./all_tweets/tweet_data/2019/feb8_14.csv')
week3 = pd.read_csv('./all_tweets/tweet_data/2019/feb15_21.csv')
week4 = pd.read_csv('./all_tweets/tweet_data/2019/feb22_28.csv')

month = week1.append(week2)
month = month.append(week3)
month = month.append(week4)

month = month.drop_duplicates()

month = month.sort_values(by = 'tweet_created_at')

month = month.reset_index(drop = True)

month.to_csv('./all_tweets/tweet_data/2019/02_2019.csv')