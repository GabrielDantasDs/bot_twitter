import tweepy
from threading import Timer
import keyboard
import json 
import pymongo
import numpy
from pymongo import MongoClient
from datetime import datetime 
from geo_track import geo_tracker
import login
from Tweets import tweets
import os
#Declarações 
lista_tweets = []
aux = 0 
conteudo = []
interval = 10
twitter = login.login.credentials()
tweet = tweets()
tweet.catch_tweet(twitter)
tweet_text = list(tweet.tweet_text)
new_id = 0

def friendship (credentials):
    followers = credentials.followers_ids('bot_liveon')
    for follower in followers:
        try:
            credentials.create_friendship(follower)
        except:
            print ("error")
    











 
  



def bot_func() :
    termo_busca = "live on"
    busca = twitter.search(q= termo_busca, result_type = "recent",lang = "pt", since_id = 1275474087545053187 )
    print(len(busca))
    
    for tweet in busca:
        tweet_repo = {"Usuario": tweet.user.screen_name,
                "tweet": tweet.text,
                "tweet_id":tweet.id,
                "retweet": retweet(tweet.id)}
        
        
        #twitter.update_status(f'Ola @{tweet.user.screen_name}, vi que me chamou em que posso ajudar ?',tweet.id)
        print(f'User:{tweet.user.screen_name} text: {tweet.text}')
    return tweet_repo

def banco_bot () :
    cliente = MongoClient('localhost',27017)
    banco = cliente.bot
    logs_pesquisa = banco.logs_pesquisa
    logs_pesquisa.insert_one(bot_func()) 



def reply(tweet,id_tweet):
    twitter.update_status(str(tweet),id_tweet)
    
def match_followers ():
    name = input ("De o @ do primeiro usuario:")
    name_other = input ("De o @ do segundo usuario:")
    name_wanted = bool (input ("De @ do procurado: "))
    followers = twitter.friends_ids(twitter.get_user(name).id)
    followers_other = twitter.friends_ids(twitter.get_user(name_other).id)
    match_list = []
    for l in followers:
        for i in followers_other:
            if (i == l):
                nome = twitter.get_user(i)
                match_list.append(nome.screen_name)
                with open ('matchs.json','w') as json_file:
                    json.dump(match_list,json_file,indent = 2)
                print (nome.screen_name)
                if (l == name_wanted):
                    name_wanted = True
    match_document = {
                        "User origem": name,
                        "User destino": name_other,
                        "nomes": match_list,
                        "resultado": name_wanted
                     }            
    return match_document 
def append_text ():
    global conteudo
    try:
        f = open('Texto.txt', 'r')
        print("Arquivo aberto com sucesso")
        conteudo = f.readlines()
    except:
        print("Erro")

    print ("passou pelo try")
    
    f.close()
def tweetar ():
    append_text()
    tweet = ''
    for line in conteudo:
        tweet = tweet + line
        lista_tweets.append(tweet)
    print(len (lista_tweets))
    return 0    
def retweet (tweet_id):
    try:
     twitter.retweet(tweet_id)
     retweet = True
     print("rt com sucesso")
    except:
        print("erro ")
        retweet = False
    return retweet 
def spam ():
         global aux
         twitter.update_status(lista_tweets[aux])
         aux = aux + 1


def setInterval (function,interval):

    def setTime(wrapper):
        wrapper.timer = Timer(interval,wrapper)
        wrapper.timer.start()

    def wrapper():
        tweet.catch_tweet(twitter)
        tweet_text = list(tweet.tweet_text)
        backtofront_reply(tweet_text, tweet.tweet_id)
        setTime(wrapper)      
            

    setTime(wrapper)
    return wrapper



def destroy_tweet():
    for tweet in user_teste:
        twitter.destroy_status(tweet.id)
def clearInterval(wrapper):
    wrapper.timer.cancel()

def filter (word, repetitions, list_filter):
    if(len (str(word)) > 3 and (str(word)).find('@') == -1 and repetitions > 1 and word not in list_filter):
        list_filter.append(word)


def catch_tweet():
    tweets_tl = twitter.user_timeline('@tteixeira47')
    tweet = []
    n = 0
 #Pula replys mas não pula retweets ainda 
    while(tweets_tl[n].text.find('@') == 0):
        if not tweets_tl[n].retweeted :
            n +=1
            print('n é,',n)
            print(tweets_tl[n].text) 
    tweet = tweets_tl[n].text.split(' ')
    print(tweet)       
    return tweet 



def backtofront_reply(lista, tweet_id) :
    global new_id
    update = '@tteixeira47'
    reverse = lista
    reverse.reverse()
    #print(reverse)
    for word in reverse:
        update = update + ' ' + word
    try:
        if(new_id != tweet_id):
            twitter.update_status(update,tweet_id)
            new_id = tweet_id
            return 1
    except:
        return 0
   




    #comit
    
    


def grab_words():

    list_filter = []
    lista_words = [100]
    time_line = twitter.user_timeline('@tteixeira47')
    for tweet in time_line:
        split = tweet.text.split(' ')
        for word in split:
            lista_words.append(word)
    for word in lista_words:
      filter(word,lista_words.count(word),list_filter)
    list_filter = sorted(set(list_filter))
    print(list_filter)
            
    

    

#backtofront_reply(tweet_text, tweet.tweet_id)
#friendship(twitter)
#Executando 
#tweetar()
setInterval(backtofront_reply(tweet_text, tweet.tweet_id),interval)
#retweet()
#append_text()
#reply()
#destroy_tweet()
#match_followers()
#banco_bot()
#bot_func()
#grab_words()
#reply (backtofront(catch_tweet()),'1295344810073751553')
#catch_tweet()

