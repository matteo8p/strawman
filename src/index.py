' #!/usr/bin/python3 '
import twitter as twitter
import time
import datetime
import nlp as nlp 

delayTime = 60                                 #Run while loop every X seconds 

targetTwitterHandles = {'realDonaldTrump', 'BarackObama', 'JoeBiden', 'elonmusk', 'SpaceX', 'CNN', 'cnnbrk', 'CNNPolitics', 'VP', 'VICENews', 'VICE', 'VICETV',
'WSJ', 'nytimes', 'ABC', 'NBCNews', 'nowthisnews', 'CBSNews', 'SkyNews', 'NewYorker', 'BBCNews', 'SportsCenter', 'espn', 'NBA', 'NBATV', 'KingJames', 'jimmyfallon',
'Oprah', 'JLo', 'BBCBreaking'}

latestTweets = {}                               #Dictionary that pairs Twitter handle to latest tweet ID. Example, {'realDonaldTrump': 123}               
latestMentions = []                     

tweetStack = []                                 #Queue of tweets to tweet out 

def main(): 
    while(True):                                #Infinite Loop 
        now = datetime.datetime.now()                                       #Get current time 
        print('{} --------------------'.format(now.strftime("%Y-%m-%d %H:%M:%S")))  
        print('')
        for handle in targetTwitterHandles:
            try: 
                print('Scanning @{}'.format(handle))
                tweet = twitter.getLatestTweet(handle)

                if handle not in latestTweets:                                  #First time scan, the dictionary will be empty. Initialize the dictionary. 
                    print('Initializing Dictionary for @{}'.format(handle))
                    latestTweets[handle] = tweet.id
                elif latestTweets[handle] != tweet.id:                          #If the new Tweet ID does not match the previous, we know a new message was created. 
                    print('New tweet for @{} found'.format(handle))             #We will then process this new tweet and tweet out our version of it 
                    translated_message = nlp.doNLP(tweet.full_text)
                    tweetStack.append('From ' + handle + ': ' + translated_message)
                    latestTweets[handle] = tweet.id                             #Update tweet ID 
                else:                                                           #No new tweets were found 
                    print('No new tweets found from @{}'.format(handle))
            except: 
                continue
        
        try: 
            mentions = twitter.getMentions()
            for mention in mentions: 
                mention_id = mention.id
                handle = mention.user.screen_name
                text = mention.text 

                if mention_id not in latestMentions:
                    print('New mention detected from {} detected'.format(handle))
                    latestMentions.append(mention_id)
                    translated_message = nlp.doNLP(text)
                    tweetStack.append('From ' + handle + ': ' + translated_message)
        except: 
            continue

        if len(tweetStack) > 0:                                             #At most only do one tweet per minute. 
            twitter.createTweet(tweetStack.pop())
        if len(tweetStack) > 20: 
            tweetStack.clear()                                              #Clear tweet stack if stack is too large 

        print(latestTweets)
        print(latestMentions) 
        print('Currently {} tweets in tweet queue'.format(len(tweetStack)))
        print('Sleep for {} minutes'.format(delayTime / 60))
        print('')
        time.sleep(delayTime)                                               #Sleep   

def initialize():
        mentions = twitter.getMentions()
        for mention in mentions: 
            latestMentions.append(mention.id)

initialize()
main() 

