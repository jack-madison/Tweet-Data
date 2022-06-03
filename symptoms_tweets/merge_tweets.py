import pandas as pd

keywords = ['鼻水', 'はなみず', 'ハナミズ', '鼻づまり', 'はなづまり', 'ハナヅマリ', '鼻がつまる', 'はながつまる', '鼻つまる', 'はなつまる', 'くしゃみ', 
'クシャミ', '目のかゆみ', '目がかゆい', 'めがかゆい', '目かゆい', 'めかゆい', '眼がかゆい', '眼のかゆみ']

tweets = pd.DataFrame()

for keyword in keywords:
    keyword
    try:
        df = pd.read_csv('./symptoms_tweets/symptoms_keyword_tweets/' + str(keyword) + '_tweets.csv')

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

tweets.to_csv('./symptoms_tweets/symptoms_tweets_with_locations.csv', index=False)