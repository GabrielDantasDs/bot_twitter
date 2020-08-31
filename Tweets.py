import login


class tweets:
    def __init__(self):
        self.tweet_text = 'alo'
        self.tweet_id = -1
        
    def catch_tweet (self,twitter):
        tweets_tl = twitter.user_timeline('@MInfraestrutura')
        tweet = []
        n = 0
    #Pula replys mas não pula retweets ainda 
        while(tweets_tl[n].text.find('@') == 0):
            if not tweets_tl[n].retweeted :
                n +=1
                #print('n é,',n)
                #print(tweets_tl[n].text) 
        self.tweet_text = tweets_tl[n].text.split(' ')
        self.tweet_id = str (tweets_tl[n].id)
        #print(tweet_text)       
         
