from keys import api_nasa_key
import requests

api_nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={api_nasa_key}"

request = requests.get(api_nasa_url)

if request.status_code == 200:
  dados = request.json()
  data = dados['date']
  url = dados['url']
  titulo = dados['title']

print(data)
print(url)
print(titulo)
