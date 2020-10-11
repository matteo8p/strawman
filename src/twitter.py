import tweepy                           
import datetime, time

#-------------
# ACCOUNT CREDENTIALS
#-------------
CONSUMER_KEY = 'XX'  
CONSUMER_SECRET = 'XX'
ACCESS_KEY = 'XX'
ACCESS_SECRET = 'XX'

#--------------
# ACCOUNT API SETUP 
#--------------
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#--------------------
# Verify Credentials 
# returns: True or False if credentials are verified 
def verifyCredentials(): 
    try: 
        api.verify_credentials()
    except: 
        print('ERROR: Bad API Credentials')
        return False
    return True

#--------------------
# createTweet() will create a tweet on the account 
# params: text that contains what is being tweeted 
# returns: N/A
def createTweet(text): 
    if(verifyCredentials() == False):
        return 

    try: 
        api.update_status(text)
    except Exception as ex: 
        print('ERROR: Could not create tweet. {}'.format(ex))
        return 
    
    print('Tweet Created: {}'.format(text))

#--------------------
# getLatestTweet(username) will get the latest tweet of the given username
# params: username
# output: The latest tweet of given username. 

msg = ""
timeFrame = 0

def getLatestTweet(username):
    tweet = api.user_timeline(username, count=1, tweet_mode='extended')[0]
    return tweet

def getRateLimit(): 
    verifyCredentials()
    return api.rate_limit_status()


# Write a method getMentions() in twitter.py. getMentions() will return a JSON data of the 20 most recent @ mentions to the Strawmanbot account.
#--------------------
# getMentions() will get recent mentions to the Strawmanbot account
# params: N/A
# output: JSON data of 20 most recent @ mentions
def getMentions():
    return api.mentions_timeline()
