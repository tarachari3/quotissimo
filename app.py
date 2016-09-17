# coding: utf-8
# pip install --upgrade watson-developer-cloud
from flask import Flask
from flask import request, render_template
import json
import tweepy
import nltk
from watson_developer_cloud import AlchemyLanguageV1
import unicodedata
import numpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quoteGen')
def authorize():
	auth = tweepy.OAuthHandler('xpGsNwsKdtsMus1dZBBINYHcf', '6IKBQVjymWRGreXHkKhDg7EG8IEd14cewJAHC0zSn82Cf8bdzJ')
	auth.set_access_token('776993594980831232-UcnUJa08VgIR5WMPmRLlam3QFyZ4hb1', '9KRcUxxjfSPluY3UsDaD9Wx60CT97OThehDpoFRPe9AW3')

	# auth = tweepy.OAuthHandler('QvadGhIMnZxIcrovlPqwvMnu9', 'XKiHd8SxMr4eysjkqrz09uUDbtB85Pr2iXihZrfr8phW32rpHc')
	# auth.set_access_token('777163050990338048-g1MKzFlzfAYydENWkSwpdkeUtDd7iWD', 'p5ozx8ndZE4fNyUL8jChLmDWcBeGDjLDd7yXL7xO5WOz9')

	api = tweepy.API(auth)
	return api

def getTweets(screen_name, api):
	try:
		public_tweets = api.user_timeline(screen_name, count = 3200)
		tweet_string = ''
		for tweet in public_tweets:
		    tweet_string = tweet_string + '|' + unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')
		return tweet_string.encode('utf-8')
	except:
		return 'nope'

def parseTweets(tweet_string):

	words = tweet_string.split()
	toRemove = ['-', '_', '<', '@', ':', '.com', '.COM', '.edu', '>', '.uk', '/', '\\', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '#', 'htt', 'RT' , '`', '(', ')', '^', '#', '$', '%', '_', '=', '+', '[', ']', '{', '}', '...', '..']
	for char in toRemove:
		for x in words:
			if char in x:
				ind = words.index(x)
				words[ind] = '*'
			elif '|' in x:
				ind = words.index(x)
				words[ind] = '.'
	words = filter(lambda a: a != '*', words)
	return ' '.join(words)

def makeQuote(tweetList): 
#for tweet in tweetList:

	alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
	relations = json.loads(json.dumps(alchemy_language.relations(text =tweetList,max_items=100),indent=2))['relations']

	
	alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
	relations = json.loads(json.dumps(alchemy_language.relations(text =tweetList,max_items=300),indent=2))['relations']

		#print json.dumps(alchemy_language.entities(text =tweetList,max_items=100),indent=2)


	subjects = dict()
	actions = dict()
	objects = dict()

	for i in relations:
		if 'subject' in i:
			subjectWord = json.loads(json.dumps(json.loads(json.dumps(i))['subject']))['text']
			if subjectWord not in subjects:
				subjects[subjectWord] = float(tweetList.count(subjectWord))
		if 'action' in i:
			actionWord = json.loads(json.dumps(json.loads(json.dumps(i))['action']))['text']
			if actionWord not in actions:
				actions[actionWord] = float(tweetList.count(actionWord))
		if 'object' in i:
			objectWord = json.loads(json.dumps(json.loads(json.dumps(i))['object']))['text']
			if objectWord not in objects:
				objects[objectWord] = float(tweetList.count(objectWord))


	# get prob.'s' (SUBJECTS)
	for key,value in subjects.iteritems():
		subjects[key] = value/len(subjects)

	# scale prob's

		# get prob.'s' (SUBJECTS)
	for key,value in subjects.iteritems():
		subjects[key] = value/len(subjects)

		# scale prob's

	sum =0.0;
	for key,value in subjects.iteritems():
		sum = sum + value
	for key,value in subjects.iteritems():
		subjects[key] = value/sum
	#------------------------



	# get prob.'s' (OBJECTS)
	for key,value in objects.iteritems():
		objects[key] = value/len(objects)

	# scale prob's

		# get prob.'s' (OBJECTS)
	for key,value in objects.iteritems():
		objects[key] = value/len(objects)

		# scale prob's

	sum =0.0;
	for key,value in objects.iteritems():
		sum = sum + value
	for key,value in objects.iteritems():
		objects[key] = value/sum
	#------------------------



	# get prob.'s' (ACTIONS)
	for key,value in actions.iteritems():
		actions[key] = value/len(actions)

	# scale prob's

		# get prob.'s' (ACTIONS)
	for key,value in actions.iteritems():
		actions[key] = value/len(actions)

		# scale prob's

	sum =0.0;
	for key,value in actions.iteritems():
		sum = sum + value
	for key,value in actions.iteritems():
		actions[key] = value/sum
	#------------------------


	# GENERATE QUOTE

		# GENERATE QUOTE


	startSubject = numpy.random.choice(subjects.keys(),1)[0]
	nextVerb = numpy.random.choice(actions.keys(),1)[0]
	lastObj = numpy.random.choice(objects.keys(),1)[0]

	finalQuote = startSubject+" "+nextVerb+" "+lastObj

	#print finalQuote

	if startSubject.islower():
		startSubject = startSubject.title()
	if not nextVerb.islower() and not nextVerb.isupper():
		nextVerb = nextVerb.lower()

	if "'" in nextVerb:
		nextVerb = numpy.random.choice(actions.keys(),1)[0]+nextVerb


	finalQuote = startSubject+" "+nextVerb+" "+lastObj

	noPeriods = finalQuote[0:len(finalQuote)-1].replace('...',',')
	finalQuote = noPeriods.replace('.',',')+finalQuote[len(finalQuote)-1]

	return finalQuote


def getImage(screen_name, api):
	user_info = api.get_user(screen_name)
	if user_info.default_profile_image is False:
		image_url = user_info.profile_image_url
		image_url = image_url.replace('_normal', '')
		return image_url
	else:
		return

	
def printQuote(screen_name):
	api = authorize()
	string = getTweets(screen_name, api)
	if not (string is 'nope'):
		words = parseTweets(string)
		final = makeQuote(words)
		image = getImage(screen_name, api)
	return final

def findMusic():
	return

print printQuote('VaidehiGarg')

# alchemy_language = AlchemyLanguageV1(api_key='e06c74ac7872e80fbad8f78f7a670c662ecee9d1')
# print(json.dumps(alchemy_language.keywords(url='twitter.com/ibmwatson'),indent=2))
# return 'Hello, World!'
