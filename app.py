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
	alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
print(json.dumps(alchemy_language.keywords(url='twitter.com/ibmwatson'),indent=2))
    return 'Hello, World!'