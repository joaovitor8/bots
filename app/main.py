# Importações
import tweepy
from keys import api_key, api_secret, bearer_token, access_token, access_token_secret, api_nasa_key
import requests


# Autenticação
auth = tweepy.OAuthHandler(api_key, api_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)


# API Nasa
api_nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={api_nasa_key}"
request = requests.get(api_nasa_url)

if request.status_code == 200:
  dados = request.json()
  data = dados['date']
  url = dados['url']
  titulo = dados['title']


# ------------
api.update_status_with_media(status="teste", filename="nasa_image.jpg")

#print(media.media_id)
