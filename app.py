# pip install --upgrade watson-developer-cloud
import json
from watson_developer_cloud import AlchemyLanguageV1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/quoteGen')
def quoteGen(userID):
	auth = OAuthHandler('5CNyTE0rJ0w05DfKWtMVVwvxA', 'XsRhR7CxcUUuKfvbpyWpOTapPpkbh2m3P347c4hZUhx7wplJCe')
	auth.set_access_token('2297646115-TZ3TdumkhL1lwJqX9XddIUPbtd54nAwMwT3rC8J', 'frDOLPLf2olmSIK3WhfOCnvqz8AxJE6X5C2M8jWAf27DS')

	api = tweepy.API(auth)

	public_tweets = api.user_timeline('AnnCoulter')
	for tweet in public_tweets:
	    print tweet.text
	    
# 	alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
# print(json.dumps(alchemy_language.keywords(url='twitter.com/ibmwatson'),indent=2))
#     return 'Hello, World!'