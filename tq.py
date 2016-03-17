import tweepy
import os
import time
import random
class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)


def deleteline(todelete):
    
    f = open('.\quotes.txt','w')
    c = 1
    for line in mylist:
        print 'line '+line + '\n'
        if line != todelete:
            print 'to delete '+ todelete
            print '%s' %c
            f.write(line)
            f.write('\n')
            c += 1
            
if __name__ == "__main__":
    twitter = TwitterAPI()
    with open('c:\users\user\desktop\quotes.txt') as f:
        mylist = f.read().splitlines() 
    quotes = random.choice(mylist)
    twitter.tweet(quotes)
    deleteline(quotes)
        

            
