import tweepy
from keys import api_key, api_secret, bearer_token, access_token, access_token_secret, api_nasa_key
import requests

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

api_nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={api_nasa_key}"

request = requests.get(api_nasa_url)

if request.status_code == 200:
  dados = request.json()
  data = dados['date']
  url = dados['url']
  titulo = dados['title']

hashtag = ""

print(data)
print(url)
print(titulo)


client.create_tweet(text= "Teste bot4", )

print("enviado")



# auth = tweepy.OAuthHandler(api_key, api_secret) 
# auth.set_access_token(access_token, access_token_secret) 
# api = tweepy.API(auth)
# tweepy.client.
