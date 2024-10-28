import tweepy
from keys import api_key, api_secret, bearer_token, access_token, access_token_secret

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

client.create_tweet(text= "Teste bot4")

print("enviado")
