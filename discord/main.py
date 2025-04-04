import requests

import discord
from discord.ext import commands

#from deep_translator import GoogleTranslator
#from atproto import Client


intents - discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
  print("Bot Iniciado!!")





def fetch_nasa_media_data(api_key):
  #"""Obtém os dados da mídia do dia da API da NASA."""
  response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
  if response.status_code == 200:
    data = response.json()
    return {
      'copyright': data['copyright'],
      'date': data['date'],
      'url': data['url'],
      'title': data['title']
    }
  else:
    print("Falha ao obter dados da API da NASA.")
    return None




bot.run()
