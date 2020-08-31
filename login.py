import tweepy
import json

class login:

        def credentials_json ():
            with open ('credentials_second.json', 'r') as json_file :
                    leitura = json.load(json_file)
                    chave_consumidor = str (leitura['chave_consumidor'])
                    segredo_consumidor = str (leitura['segredo_consumidor'])
                    token_acesso = str (leitura['token_acesso'])
                    token_acesso_segredo = str (leitura['token_acesso_segredo'])
                    autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
                    autenticacao.set_access_token(token_acesso,token_acesso_segredo)
                    twitter = tweepy.API(autenticacao)
                    print(chave_consumidor)
            json_file.close()
            return twitter
