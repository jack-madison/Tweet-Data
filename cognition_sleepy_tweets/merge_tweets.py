import pandas as pd

# Create a list of keywords to search
keywords = ['眠い', 'ねむい', '眠たい', 'ねむたい', '眠すぎる', 'ねむすぎる']

tweets = pd.DataFrame()

for keyword in keywords:
    keyword
    try:
        df = pd.read_csv('./cognition_sleepy_tweets/cognition_sleepy_keyword_tweets/' + str(keyword) + '_tweets.csv')

        tweets = tweets.append(df)
    except:
        print("Error with " + str(keyword))
        
tweets = tweets.drop_duplicates()

locations = pd.read_csv('./locations/matched_locations.csv')

tweets = pd.merge(tweets, locations, how='left', on = 'tweet_location_id')

tweets = tweets[tweets['mun_id'].notna()]
tweets = tweets[(tweets['place_type'] != 'admin') & (tweets['place_type'] != 'country')]

tweets['tweet_created_at'] = pd.to_datetime(tweets['tweet_created_at'])
tweets['tweet_created_at'] = tweets['tweet_created_at'].dt.tz_convert('Japan')

tweets.to_csv('./cognition_sleepy_tweets/cognition_sleepy_tweets_with_locations.csv', index=False)