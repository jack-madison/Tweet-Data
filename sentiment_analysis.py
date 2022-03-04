# This is a file to test the capabilities of the asari sentiment analysis package
from asari.api import Sonar

# Initialize sonar
sonar = Sonar()

# The following strings are taken from the twitter data feb_2020 in the tweet_data/2020 folder
sonar.ping(text="危機感がない奴が多過ぎて泣けてくる・・")
sonar.ping(text="A happy new month!!")
sonar.ping(text="日生さやま台 シェパードが徘徊中　注意")
sonar.ping(text="#スカイツリー 今夜のスカイツリー光ぐ普段と違ってスゴーく色かかんってるw https://t.co/5o9cJsANfr")
sonar.ping(text="@Uber81678071 引っ越しですか？ ようこそ、渋谷区へψ(｀∇´)ψ")