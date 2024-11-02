from atproto import Client
import requests

BLUESKY_USERNAME="contato.unyverso@gmail.com"
BLUESKY_PASSWORD="27102001j8"
API_NASA_KEY = "Jumo10stBfTfBMu3NJJ7NcaurYDm0IKXQ1i9JMWz"

api_nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={API_NASA_KEY}"

request = requests.get(api_nasa_url)

if request.status_code == 200:
  dados = request.json()
  data = dados['date']
  url = dados['url']
  titulo = dados['title']


response = requests.get(url)

if response.status_code == 200:
  with open("nasa_image.jpg", "wb") as file:
    file.write(response.content)
  print("Imagem baixada com sucesso!")
else:
  print("Falha ao baixar a imagem. Código de status:", response.status_code)


client = Client()
client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

with open("nasa_image.jpg", 'rb') as f:
  img_data = f.read()

client.send_image(text=f'{titulo} - {data}', image=img_data, image_alt=titulo)
