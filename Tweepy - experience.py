import tweepy
from threading import Timer
import keyboard
import json 
import pymongo
from pymongo import MongoClient
import datetime

#Declarações 
chave_consumidor = 'XXXXXXXXXXXXXXXXXXX'
segredo_consumidor = 'XXXXXXXXXXXXXXXXX'
token_acesso = 'XXXXXXXXXXXXXXX'
token_acesso_segredo = 'XXXXXXXXXXXXXXXX'
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso,token_acesso_segredo)
twitter =  tweepy.API(autenticacao)
user_teste = twitter.user_timeline('generico')

lista_tweets = []
aux = 0 
conteudo = []
interval = 5.0
tweet_repo = []

def busca_func() :
    termo_busca = input ("De o termo de busca:")
    busca = twitter.search(q= termo_busca, result_type = "recent")
    for tweet in busca:
        tweet_repo.append(tweet.id)
        twitter.update_status(f'Ola @{tweet.user.screen_name}, vi que me chamou em que posso ajudar ?',tweet.id)
        print(f'User:{tweet.user.screen_name} text: {tweet.text}')


def banco_bot () :
    cliente = MongoClient('localhost',27017)
    banco = cliente.bot
    logs_pesquisa = banco.logs_pesquisa
    logs_id = logs_pesquisa.insert_one(match_followers()) 
def reply():
    for tweet in user_teste:
                twitter.update_status("Oi linda, expressando meu afeto fazendo oq eu sei fazer de melhor(ou mais ou menos) <3 , @inoimisets", tweet.id)
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
def retweet ():
    try:
     twitter.retweet()
     print("rt com sucesso")
    except:
        print("erro ")
def spam ():
         global aux
         twitter.update_status(lista_tweets[aux])
         aux = aux + 1
def setInterval (function,interval):
    def setTime(wrapper):
        wrapper.timer = Timer(interval,wrapper)
        wrapper.timer.start()

    def wrapper():
        spam()
        setTime(wrapper)
        if(aux == len(lista_tweets)):
            clearInterval(wrapper)

    setTime(wrapper)
    return wrapper
def destroy_tweet():
    for tweet in user_teste:
        twitter.destroy_status(tweet.id)
def clearInterval(wrapper):
    wrapper.timer.cancel()
#comit

#Executando 
#tweetar()
#setInterval(spam,interval)
#retweet()
#append_text()
#reply()
#destroy_tweet()
#match_followers()
#banco_bot()
busca_func()