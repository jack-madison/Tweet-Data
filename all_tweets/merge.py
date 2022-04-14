# The following python code merges the tweet data. I decided to pull the data in smaller
# batches to aviod going over the rate limit and losing the entire dataframe.

import pandas as pd
import numpy as np

may1_7 = pd.read_csv('./all_tweets/tweet_data/2020/may1_7.csv')
may8_14 = pd.read_csv('./all_tweets/tweet_data/2020/may8_14.csv')
may15_21 = pd.read_csv('./all_tweets/tweet_data/2020/may15_21.csv')
may22_31 = pd.read_csv('./all_tweets/tweet_data/2020/may22_31.csv')

may = may1_7.append(may8_14)
may = may.append(may15_21)
may = may.append(may22_31)

may = may.drop_duplicates()

may = may.sort_values(by = 'tweet_created_at')

may = may.reset_index(drop = True)

may.to_csv('./all_tweets/tweet_data/2020/05_2020.csv')