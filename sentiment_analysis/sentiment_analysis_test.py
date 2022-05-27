# This is a file to test the capabilities of the asari sentiment analysis package
from asari.api import Sonar

# Initialize sonar
sonar = Sonar()

# The following strings are samples to compare "cleaned up" tweets with uncleaned tweets
sentiment1 = sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…")

sentiment1['classes'][0]['confidence']

sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…😵")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…(´+ω+｀)")
sonar.ping(text="@mika_pollen_b なんだかしんどいと思ったら気圧のせいか…")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…。https://twitter.com/terunekootenki/status/1524699067569229825?s=20&t=OC7RWlnr7ifTa2ExRZY-WQ")
sonar.ping(text="@mika_pollen_b なんだかしんどいと思ったら気圧のせいか…😵(´+ω+｀) https://twitter.com/terunekootenki/status/1524699067569229825?s=20&t=OC7RWlnr7ifTa2ExRZY-WQ")

sonar.ping(text="senの箸置きをもらった。")
sonar.ping(text="senの箸置きをもらった😍")
sonar.ping(text="senの箸置きをもらった(^^)/")
sonar.ping(text="@mika_pollen_b senの箸置きをもらった。")
sonar.ping(text="senの箸置きをもらった https://twitter.com/sennostore/status/1482943517614014464?s=20&t=DnG8A50srEIOaZHZG-ubig")
sonar.ping(text="@mika_pollen_b senの箸置きをもらった😍(^^)/ https://twitter.com/sennostore/status/1482943517614014464?s=20&t=DnG8A50srEIOaZHZG-ubig")

sonar.ping(text="Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる。")
sonar.ping(text="Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる😭😭")
sonar.ping(text="Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる( ；∀；)")
sonar.ping(text="@mika_pollen_b Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる。")
sonar.ping(text="Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる https://twitter.com/ABCMART_INFO/status/1519642632301215745?s=20&t=DnG8A50srEIOaZHZG-ubig")
sonar.ping(text="@mika_pollen_b Rainbow Stansmithあまりの可愛さに靴紐を白色に付け替えて履いてる😭😭( ；∀；) https://twitter.com/ABCMART_INFO/status/1519642632301215745?s=20&t=DnG8A50srEIOaZHZG-ubig")

sonar.ping(text="雨が止んで良かったね。")
sonar.ping(text="雨が止んで良かったね😊")
sonar.ping(text="雨が止んで良かったね(^^)")
sonar.ping(text="@mika_pollen_b 雨が止んで良かったね。")
sonar.ping(text="雨が止んで良かったね https://twitter.com/Yahoo_weather/status/1525579771723542528?s=20&t=DnG8A50srEIOaZHZG-ubig")
sonar.ping(text="@mika_pollen_b 雨が止んで良かったね😊(^^) https://twitter.com/Yahoo_weather/status/1525579771723542528?s=20&t=DnG8A50srEIOaZHZG-ubig")

sonar.ping(text="⛰🏫⛰⛰🚶🏻‍♀️🐗⛰⛰⛰⛰⛰")
sonar.ping(text="_(:3 」∠)__(┐「ε:)__(:3 」∠)_")
sonar.ping(text="@mika_pollen_b @mika_pollen_b @mika_pollen_b")
sonar.ping(text="_(:3 」∠)__(┐「ε:)__(:3 」∠)_。 https://twitter.com/mika_pollen_a/status/1526732089726742528?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")
sonar.ping(text="@mika_pollen_b @mika_pollen_b @mika_pollen_b ⛰🏫⛰⛰🚶🏻‍♀️🐗⛰⛰⛰⛰⛰ _(:3 」∠)__(┐「ε:)__(:3 」∠)_ https://twitter.com/mika_pollen_a/status/1526732089726742528?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")

sonar.ping(text="疲れた。泣きそう。もう消えたい。")
sonar.ping(text="疲れた。泣きそう。もう消えたい。😭😭")
sonar.ping(text="疲れた。泣きそう。もう消えたい。( ；∀；)")
sonar.ping(text="@mika_pollen_b 疲れた。泣きそう。もう消えたい。")
sonar.ping(text="疲れた。泣きそう。もう消えたい https://twitter.com/mika_pollen_a/status/1526735493815496705?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")
sonar.ping(text="@mika_pollen_b 疲れた。泣きそう。もう消えたい。😭😭( ；∀；) https://twitter.com/mika_pollen_a/status/1526735493815496705?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")

sonar.ping(text="またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。")
sonar.ping(text="またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。😓😓")
sonar.ping(text="またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。(/ _ ; )")
sonar.ping(text="@mika_pollen_b またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。")
sonar.ping(text="またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ… https://twitter.com/mika_pollen_a/status/1526741304205783040?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")
sonar.ping(text="@mika_pollen_b またしんどくなるんじゃ無いかと思うと出かけるの憂鬱だ…。😓😓(/ _ ; ) https://twitter.com/mika_pollen_a/status/1526741304205783040?s=20&t=GmwN2Q7f5jj7FMh5bufGFw")

sonar.ping(text="やったー合格したー")
sonar.ping(text="やったー合格したー！！！！！")
sonar.ping(text="やったー合格したー？？？？？")

sonar.ping(text="えーん。憂鬱だー")
sonar.ping(text="えーん。憂鬱だー！！！！！")
sonar.ping(text="えーん。憂鬱だー？？？？？")

sonar.ping(text="")


import oseti 

analyzer = oseti.Analyzer()

analyzer.analyze('天国で待ってる。')


analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！')


analyzer.analyze_detail('お金も希望もない！')