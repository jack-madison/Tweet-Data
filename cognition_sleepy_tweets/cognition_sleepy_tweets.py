import pandas as pd
import time
import tweepy

#Import the bearer tokens
from twitter_authentication import bearer_token_1
from twitter_authentication import bearer_token_2
from twitter_authentication import bearer_token_3
from twitter_authentication import bearer_token_4
from twitter_authentication import bearer_token_5
from twitter_authentication import bearer_token_6
from twitter_authentication import bearer_token_7
from twitter_authentication import bearer_token_8

# Create a list of barer tokens
bearer_tokens = [bearer_token_1, bearer_token_2, bearer_token_3, bearer_token_4, bearer_token_5, bearer_token_6, bearer_token_7, bearer_token_8]

# Initialize the counter for the barer tokens
token_no = 0

# Create a list of keywords to search
keywords = ['眠い', 'ねむい', '眠たい', 'ねむたい', '眠すぎる', 'ねむすぎる']

for keyword in keywords:
    if token_no > 7: token_no = 0

    query_str = '"' + str(keyword) + '" -is:retweet -is:nullcast has:geo place_country:JP'

    print(str(query_str) + ' using barer token ' + str(bearer_tokens[token_no]))

    client = tweepy.Client(bearer_tokens[token_no], wait_on_rate_limit=True)

    keyword_tweets = []

    for response in tweepy.Paginator(client.search_all_tweets, 
                                    query = str(query_str),
                                    tweet_fields = ['author_id', 'created_at', 'geo', 'id', 'lang', 'public_metrics', 'source', 'text'],
                                    start_time = '2006-03-22T00:00:00+09:00',
                                    end_time = '2022-01-01T00:00:00+09:00',
                                    max_results=500):
        time.sleep(1)
        keyword_tweets.append(response)

    result = []

    # Loop through each response object
    for response in keyword_tweets:
        try:
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
                except KeyError:
                    print("Key Error")
        except TypeError:
            print("Type Error")
        except KeyError:
            print("Key Error")

    # Change this list of dictionaries into a dataframe
    tweets = pd.DataFrame(result)

    # Save the tweets as a CSV
    tweets.to_csv('./cognition_sleepy_tweets/cognition_sleepy_keyword_tweets/' + str(keyword) + '_tweets.csv', index = False)

    token_no = token_no + 1

print("Done!")