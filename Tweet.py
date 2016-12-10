import tweepy

import csv

from textblob import TextBlob


consumer_key= 'he8TzJJectSQsrQ3gC09XQuH3'
consumer_secret= 'zMn8uScwocSxiBdWZo6rBKARoUa6wHckY71XFh86PTlYasiH8c'

access_token= '2351884572-UhucAenFEvtnzPLHz4czNrRah5lStNEomN83nzB'
acces_token_secret= 'wblXNMdAK5kUbvhaiETSBmjbzztZb01zlWlsVaqmItY9K'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

word = raw_input('Enter the word to find sentiments about: ') #Change to input if using Python3

public_tweets = api.search(word)

with open('Tweet_Sentiments', 'w') as pointer:
	newFileWriter = csv.writer(pointer)
	newFileWriter.writerow(['Tweet', 'Label'])


i=0.0
k=0.0

for tweet in public_tweets:
	
	analysis = TextBlob(tweet.text)

	k+=1.0

	if analysis.sentiment.polarity>0:
		Label = 'POSITIVE'
		i+=1.0
	else :
		Label = 'NEGATIVE'


	with open('Tweet_Sentiments', 'a') as pointer:
		newFileWriter = csv.writer(pointer)
		newFileWriter.writerow([ tweet.text.encode('utf-8') , Label])



if i/k >0.8:
	print('Tweeters love ' + word)

elif i/k > 0.5:
	print('Tweeters have good things to say about ' + word)

elif i/k > 0.3:
	print('Tweeters don\'t really like ' + word)
else: 
	print('Tweeters hate ' + word)
