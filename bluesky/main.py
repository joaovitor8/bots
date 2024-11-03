from atproto import Client
import requests
import os
import schedule
import time

# Configurações de ambiente
BLUESKY_USERNAME = os.environ['BLUESKY_USERNAME']
BLUESKY_PASSWORD = os.environ['BLUESKY_PASSWORD']
API_NASA_KEY = os.environ['API_NASA_KEY']


def fetch_nasa_media_data(api_key):
  #"""Obtém os dados da mídia do dia da API da NASA."""
  response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
  if response.status_code == 200:
    data = response.json()
    return {
      'date': data['date'],
      'url': data['url'],
      'title': data['title']
    }
  else:
    print("Falha ao obter dados da API da NASA.")
    return None


def download_media(url):
  #"""Baixa a mídia (imagem ou vídeo) da URL fornecida e salva localmente."""
  media_type = 'video' if url.endswith(('.mp4', '.mov')) else 'image'
  file_extension = '.mp4' if media_type == 'video' else '.jpg'
  file_path = f"nasa_media{file_extension}"

  response = requests.get(url)
  if response.status_code == 200:
    with open(file_path, "wb") as file:
      file.write(response.content)
    print(f"{media_type.capitalize()} baixado(a) com sucesso!")
    return file_path, media_type
  else:
    print(f"Falha ao baixar a mídia. Código de status:", response.status_code)
    return None, None


def upload_to_bluesky(username, password, title, date, media_path, media_type):
  #"""Faz o upload da mídia para o Bluesky com título e data."""
  client = Client()
  client.login(username, password)

  with open(media_path, 'rb') as media_file:
    media_data = media_file.read()

  if media_type == 'image':
    client.send_image(text=f'{title} - {date}', image=media_data, image_alt=title)
  elif media_type == 'video':
    client.send_video(text=f'{title} - {date}', video=media_data, video_alt=title)

  print(f"Mídia ({media_type}) enviada com sucesso para o Bluesky.")


def delete_local_file(file_path):
  #"""Remove o arquivo local se ele existir."""
  if os.path.exists(file_path):
    os.remove(file_path)
    print("Mídia deletada com sucesso!")
  else:
    print("Arquivo não encontrado.")


def main():
  # Etapa 1: Obter dados da mídia
  media_data = fetch_nasa_media_data(API_NASA_KEY)
  if not media_data:
    return  # Encerra se falhar ao obter dados
  
  # Etapa 2: Baixar mídia
  media_path, media_type = download_media(media_data['url'])
  if not media_path:
    return  # Encerra se falhar ao baixar a mídia

  # Etapa 3: Fazer upload para o Bluesky
  upload_to_bluesky(BLUESKY_USERNAME, BLUESKY_PASSWORD, media_data['title'], media_data['date'], media_path, media_type)

  # Etapa 4: Deletar arquivo local
  delete_local_file(media_path)


# Agendando a execução diária às 15:00
schedule.every().day.at("15:30").do(main)

# Loop para manter o script em execução e verificar o agendamento
if __name__ == "__main__":
  print("Script agendado para rodar diariamente às 15:30.")
  while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto se é hora de executar a tarefa

