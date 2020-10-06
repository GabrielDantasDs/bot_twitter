import tweepy
import json
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
KEY_COSTUMER = os.environ.get('KEY_COSTUMER')
ACESS_TOKEN = os.environ.get('ACESS_TOKEN')
SECRET_TOKEN_ACESS = os.environ.get('SECRET_ACESS_TOKEN')
print(SECRET_KEY)
print(KEY_COSTUMER)
print(ACESS_TOKEN)
print(SECRET_TOKEN_ACESS)

class login:

    def credentials():
        chave_consumidor = SECRET_KEY
        print(chave_consumidor)
        segredo_consumidor = KEY_COSTUMER
        print(segredo_consumidor)
        token_acesso = ACESS_TOKEN
        print(ACESS_TOKEN)
        token_acesso_segredo = SECRET_TOKEN_ACESS
        print(token_acesso_segredo)
        autenticacao = tweepy.OAuthHandler(
            chave_consumidor, segredo_consumidor)
        autenticacao.set_access_token(token_acesso, token_acesso_segredo)
        twitter = tweepy.API(autenticacao)
        return twitter

    