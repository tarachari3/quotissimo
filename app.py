# pip install --upgrade watson-developer-cloud
import json
import tweepy
import nltk
from watson_developer_cloud import AlchemyLanguageV1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/quoteGen')
def quoteGen(screen_name):
	auth = tweepy.OAuthHandler('xpGsNwsKdtsMus1dZBBINYHcf', '6IKBQVjymWRGreXHkKhDg7EG8IEd14cewJAHC0zSn82Cf8bdzJ')
	auth.set_access_token('776993594980831232-UcnUJa08VgIR5WMPmRLlam3QFyZ4hb1', '9KRcUxxjfSPluY3UsDaD9Wx60CT97OThehDpoFRPe9AW3')

	api = tweepy.API(auth)

	public_tweets = api.user_timeline(screen_name, count = 2000)
	tweet_string = ''
	for tweet in public_tweets:
	    tweet_string = tweet_string + tweet.text
	return tweet_string.encode('utf-8')

def removeUsers(tweet_string):
	words = tweet_string.split()
	toRemove = ['-', '<', '@', ':', '.com', '.COM', '.edu', '>', '.uk', '/', '\\', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '#', '`', '(', ')', '|', '^', '#', '$', '%', '_', '=', '+', '[', ']', '{', '}']
	for char in toRemove:
		for x in words:
			if char in x:
				ind = words.index(x)
				words[ind] = '*'
	words = filter(lambda a: a != '*', words)
	return words
	

string = quoteGen('AnnCoulter')
words = removeUsers(string)
print words

length = len(words)
print words[length-1]

# 	alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
# print(json.dumps(alchemy_language.keywords(url='twitter.com/ibmwatson'),indent=2))
#     return 'Hello, World!'