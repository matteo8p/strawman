# @strawmanbot
### Matthew Wang, Aatmik Mallya, Daniel Hsu, Michael Chung October 2020 
<br>

# Synopsis 

**Note: Sarcasm below**

It's October, and voting is right around the corner. Voter turnout among the youth has always been an issue. A lot of the youth do not think politics applies to them, or they simply do not find it interesting. 


@strawmanbot is a solution to make news more engaging and fun. It scans for tweets from news outlets and generate goofy mad-lib translations. It is also listening for @ mentions. We can translate your tweets too (See the Try It Yourself section)


Follow [@strawmantest](https://twitter.com/strawmantest) on Twitter for your #1 most entertaining news source! 

# Try It Yourself 

Tag [@strawmantest](https://twitter.com/strawmantest) in one of your tweets. You can type anything. Tell us about your day! Talk about your favorite food! We will translate your tweet into a goofy mad-lib. 

Note that due to API rate limiting, it may take up to 5 minutes for your tweet to process. 

# How we made it 

@strawmanbot is written in a Python script hosted to run 24/7 on Google Cloud Compute instance. There are 4 components to the project. 

1. index.py. This is the main file of the project that pieces the other compoments together 
2. twitter.py Uses tweepy API library to interact with our twitter account. It's functions include create tweet, scan for tweets, and scan for mentions 
3. nlp.py Is a natural language processor using spacy.io library. We use nlp.py to detect part of speech in a tweet 
4. wordlib.py contains all of the nouns, verbs, and adjectives we use to construct goofy sentences. 

Due to rate limiting, the python script only does scans creates tweets every minute. 

