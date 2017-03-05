from pattern.web import Twitter,plaintext
from textblob import TextBlob

twitter = Twitter(language = 'en')


total_tweets=0
positive_tweets =0

word = raw_input("Enter your search term: ")

for tweet in twitter.search(word, cached = 'False'):

    total_tweets += 1

    print plaintext(tweet.text)

    analysis = TextBlob(tweet.text)

    if analysis.sentiment.polarity >0:
        positive_tweets += 1.0

if positive_tweets/total_tweets >0.8:
	print('Tweeters love ' + word)

elif positive_tweets/total_tweets > 0.5:
	print('Tweeters have good things to say about ' + word)

elif positive_tweets/total_tweets > 0.3:
	print('Tweeters don\'t really like ' + word)
else:
	print('Tweeters hate ' + word)
