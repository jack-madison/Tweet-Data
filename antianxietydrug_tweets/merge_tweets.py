import pandas as pd

keywords = ['抗不安薬', 'デパス', 'グランダキシン', 'ワイパックス', 'エリスパン', 'コンスタン', 'ソラナックス', 'レキソタン', 'メレックス', 'リボトリール',
'セルシン', 'セパゾン', 'コントール', 'セレナール', 'メイラックス', 'ホリゾン', 'エチゾラム', 'トフィソパム', 'クロチアゼパム', 'ロラゼパム', 'フルジアゼパム',
'アルプラゾラム', 'ブロマゼパム', 'メキサゾラム', 'クロナゼパム', 'ジアゼパム', 'クロキサゾラム', 'クロルジアゼポ', 'オキサゾラム', 'ロフラゼプ', 'ジアゼパム']

tweets = pd.DataFrame()

for keyword in keywords:
    keyword
    try:
        df = pd.read_csv('./antianxietydrug_tweets/antianxietydrug_keyword_tweets/' + str(keyword) + '_tweets.csv')

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

tweets.to_csv('./antianxietydrug_tweets/antianxietydrug_tweets_with_locations.csv', index=False)