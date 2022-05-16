# This is a file to test the capabilities of the asari sentiment analysis package
from asari.api import Sonar

# Initialize sonar
sonar = Sonar()

# The following strings are samples to compare "cleaned up" tweets with uncleaned tweets
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…")
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