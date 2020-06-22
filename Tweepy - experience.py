import tweepy
from threading import Timer
import keyboard
import json 
import pymongo
from pymongo import MongoClient
from datetime import datetime 
from geo_track import geo_tracker

#Declarações 
chave_consumidor = 'iYp4Z39sT0FgYILG7KCPVsRwd'
segredo_consumidor = 'jlyavSiYi7avSMO2OZqlbyhsJDhhBHFoCgdaCvwCKmFKlfyqry'
token_acesso = '1266133176059080705-vIw80k2r61FsGmubL8vxRV02hgvB44'
token_acesso_segredo = '9amCbSPFl8onmN0aYfxKY3L0xly3QTxXWbMTq1mYlh9Ls' 
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso,token_acesso_segredo)
twitter =  tweepy.API(autenticacao)
user_teste = twitter.user_timeline('generico')
lista_tweets = []
aux = 0 
conteudo = []
interval = 5.0
tweet_repo = []
time = datetime.now()
print (type (time))

geo = geo_tracker()

coordinate_y = geo.location.longitude
coordinate_x = geo.location.latitude
radius  = 10000
coordinates = str([coordinate_x, coordinate_y,radius])

print (coordinates)

def bot_func() :
    termo_busca = "live"
    busca = twitter.search(q= termo_busca, result_type = "recent",lang = "pt", until = "2020-06-21" )
    print(len(busca))
    for tweet in busca:
        tweet_repo.append(tweet.id)
        #retweet(tweet.id)
        #twitter.update_status(f'Ola @{tweet.user.screen_name}, vi que me chamou em que posso ajudar ?',tweet.id)
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
def retweet (tweet_id):
    try:
     twitter.retweet(tweet_id)
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
        bot_func()
        setTime(wrapper)      
            

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
setInterval(bot_func,interval)
#retweet()
#append_text()
#reply()
#destroy_tweet()
#match_followers()
#banco_bot()
#bot_func()