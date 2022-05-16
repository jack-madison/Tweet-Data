# This is a file to test the capabilities of the asari sentiment analysis package
from asari.api import Sonar

# Initialize sonar
sonar = Sonar()

# The following strings are taken from the twitter data feb_2020 in the tweet_data/2020 folder
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…😵")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…(´+ω+｀)")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか…。https://twitter.com/terunekootenki/status/1524699067569229825?s=20&t=OC7RWlnr7ifTa2ExRZY-WQ")
sonar.ping(text="なんだかしんどいと思ったら気圧のせいか… @jckmadison")

