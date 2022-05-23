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
keywords = ['42鯛', 'DV', 'SOS', 'zisatu', 'いじめ', 'いなくなりたい', 'いやがらせ', 'いらない人間', 'うつ', 'うつ病', 'おわりにしたい', 'カウンセリング',
'きえたい', 'グモる', 'くるしい', 'クローゼット　首', 'サイレース', 'ジサツ', 'じさつ', 'しにたあい', 'しにたい', 'しぬ', 'しぬしかない', 'しんどい',
'ストレスチェック', 'セクハラ', 'たすけて', 'タヒ', 'つかれた', 'つらい', 'ドアノブ　首', 'なやみ', 'ノイローゼ', 'はやくしにたい', 'ハラスメント',
'パワハラ', 'ひきこもり', 'ひとりぼっち', 'マイスリー', 'メンヘラ', 'もうだめ', 'もう消えたい', 'モラハラ', 'リスカ', 'リストカット', 'デパス', '安楽死',
'遺書', '一緒に死', '引きこもり', '押しつぶされる', '価値がない', '過労', '学校行きたくない', '学校行けない', '楽な死に方', '楽になりたい', '楽に死ぬ',
'虐タイ', '虐待', '居場所がない', '苦しい', '嫌がらせ', '孤独', '孤立', '抗うつ薬', '殺して', '殺してほしい', '殺入', '惨めな人生だった', '産後うつ',
'仕事ができない', '仕事が見つからない', '仕事つらい', '仕事できない', '仕事行きたくない', '仕事行けない', '仕事辞める', '仕事失敗', '死', '死なせて欲しい',
'死にたあ', '死にたい', '死にたくて仕方ない', '死にたくなったら', '死に方', '死ぬ方法', '死ねる場所', '死ねる薬', '死のう', '死んでお詫びしたい',
'死んでやり直したい', '死んで償う方法', '自サツ', '自殺', '自殺 ガス', '自殺 願望', '自殺 手段', '自殺 場所', '自殺 相談', '自殺 投稿', '自殺 動画',
'自殺 募集', '自殺サイト', '自殺したい', '自殺掲示板', '自殺志願', '自殺対策', '自殺方法', '自殺未遂', '自殺名所', '自死', '自傷行為したい',
'手っ取り早い死に方', '首つり', '受験失敗', '樹海', '就職できない', '就職失敗', '助けて', '消えたい', '焼身', '寝れない', '心中', '辛い', '人間関係うまくいかない',
'人生あきらめたい', '人生あきらめる', '人生つかれた', '人生終わった', '人生終わりにしたい', '睡眠薬', '生きたくない', '生きづらい', '生きている意味ない',
'生きにくい', '生きる意味', '生きる意味がない', '生活が苦しい', '精神科', '精神疾患', '精神病', '逝きたい', '逝く方法', '青木ヶ原', '早く消えたい',
'相談 SNS', '相談 電話', '相談窓口', '誰か 殺して', '致死性', '仲間外れにされる', '鉄道　賠償金', '東尋坊', '逃げたい', '毒親', '入水', '悩み', '悩み相談',
'悩んでいる', '疲れ', '疲れた', '飛び降り', '病む', '病んだ', '不安', '不満', '不眠', '服毒', '暴力', '無気力', '無能', '命を絶つ', '迷惑かけたくない',
'友だち つらそう', '友達がいない', '硫化水素', '劣等感', '練炭', '鬱', '鬱しにたい']

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
    tweets.to_csv('./suicidal_tweets/suicidal_keyword_tweets/' + str(keyword) + '_tweets2.csv', index = False)

    token_no = token_no + 1

print("Done!")