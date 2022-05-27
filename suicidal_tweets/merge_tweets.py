import pandas as pd

keywords = ['42鯛', 'DV', 'SOS', 'zisatu', 'いじめ', 'いなくなりたい', 'いやがらせ', 'いらない人間', 'うつ', 'うつ病', 'おわりにしたい', 'カウンセリング',
'きえたい', 'グモる', 'くるしい', 'クローゼット 首', 'サイレース', 'ジサツ', 'じさつ', 'しにたあい', 'しにたい', 'しぬ', 'しぬしかない', 'しんどい',
'ストレスチェック', 'セクハラ', 'たすけて', 'タヒ', 'つかれた', 'つらい', 'ドアノブ 首', 'なやみ', 'ノイローゼ', 'はやくしにたい', 'ハラスメント',
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
'相談 SNS', '相談 電話', '相談窓口', '誰か 殺して', '致死性', '仲間外れにされる', '鉄道 賠償金', '東尋坊', '逃げたい', '毒親', '入水', '悩み', '悩み相談',
'悩んでいる', '疲れ', '疲れた', '飛び降り', '病む', '病んだ', '不安', '不満', '不眠', '服毒', '暴力', '無気力', '無能', '命を絶つ', '迷惑かけたくない',
'友だち つらそう', '友達がいない', '硫化水素', '劣等感', '練炭', '鬱', '鬱しにたい']

keywords_2 = ['自殺', 'じさつ', 'ジサツ']

tweets = pd.DataFrame()

keyword_count = []

for keyword in keywords:
    keyword
    try:
        df = pd.read_csv('./suicidal_tweets/suicidal_keyword_tweets/' + str(keyword) + '_tweets2.csv')

        keyword_count.append({'keyword': keyword, 'count': len(df)})

        tweets = tweets.append(df)
    except:
        print("Error with " + str(keyword))
        
        keyword_count.append({'keyword': keyword, 'count': 'error'})

counts = pd.DataFrame(keyword_count)

counts.to_csv('./suicidal_tweets/keyword_counts.csv', index = False)

tweets = tweets.drop_duplicates()

locations = pd.read_csv('./locations/matched_locations.csv')

tweets = pd.merge(tweets, locations, how='left', on = 'tweet_location_id')

tweets = tweets[tweets['mun_id'].notna()]
tweets = tweets[(tweets['place_type'] != 'admin') & (tweets['place_type'] != 'country')]

tweets['tweet_created_at'] = pd.to_datetime(tweets['tweet_created_at'])
tweets['tweet_created_at'] = tweets['tweet_created_at'].dt.tz_convert('Japan')

tweets.to_csv('./suicidal_tweets/alert_tweets_with_location.csv', index=False)

tweets = tweets.reset_index(drop = True)

tweets1 = tweets[(tweets.index >= 0) & (tweets.index <= 699999)]
tweets2 = tweets[(tweets.index >= 700000) & (tweets.index <= 1399999)]
tweets3 = tweets[(tweets.index >= 1400000) & (tweets.index <= 2099999)]
tweets4 = tweets[(tweets.index >= 2100000) & (tweets.index <= 2799999)]
tweets5 = tweets[(tweets.index >= 2800000) & (tweets.index <= 3499999)]
tweets6 = tweets[(tweets.index >= 3500000) & (tweets.index <= 4199999)]
tweets7 = tweets[(tweets.index >= 4200000) & (tweets.index <= 4899999)]
tweets8 = tweets[(tweets.index >= 4900000) & (tweets.index <= 5599999)]
tweets9 = tweets[(tweets.index >= 5600000) & (tweets.index <= 6299999)]
tweets10 = tweets[(tweets.index >= 6300000) & (tweets.index <= 6999999)]

tweets1.to_csv('./suicidal_tweets/alert_tweets_with_location1.csv', index=False)
tweets2.to_csv('./suicidal_tweets/alert_tweets_with_location2.csv', index=False)
tweets3.to_csv('./suicidal_tweets/alert_tweets_with_location3.csv', index=False)
tweets4.to_csv('./suicidal_tweets/alert_tweets_with_location4.csv', index=False)
tweets5.to_csv('./suicidal_tweets/alert_tweets_with_location5.csv', index=False)
tweets6.to_csv('./suicidal_tweets/alert_tweets_with_location6.csv', index=False)
tweets7.to_csv('./suicidal_tweets/alert_tweets_with_location7.csv', index=False)
tweets8.to_csv('./suicidal_tweets/alert_tweets_with_location8.csv', index=False)
tweets9.to_csv('./suicidal_tweets/alert_tweets_with_location9.csv', index=False)
tweets10.to_csv('./suicidal_tweets/alert_tweets_with_location10.csv', index=False)


