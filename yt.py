from pytube import YouTube
import os
import re
from moviepy.editor import *

def download_video():
    url = input("Insira o link do vídeo do YouTube: ")
    
    # Verificar se o URL possui o formato correto
    if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', url):
        print("URL inválido do YouTube.")
        return
    
    yt = YouTube(url)
    print("Título do vídeo:", yt.title)
    
    # Selecionar a maior qualidade do vídeo
    stream = yt.streams.get_highest_resolution()
    
    # Pasta de destino pré-definida
    folder_path = "C:/Users/erick/Downloads/videos"
    
    # Verificar se a pasta existe, caso contrário, criar
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Fazer o download do vídeo
    print("Fazendo o download do vídeo...")
    video_file_path = stream.download(output_path=folder_path)
    
    print("Download do vídeo concluído com sucesso!")
    
    # Perguntar ao usuário se deseja converter o vídeo para áudio
    convert_to_audio = input("Deseja converter o vídeo para áudio? (S/N): ").strip().upper()
    
    if convert_to_audio == "S":
        convert_video_to_audio(video_file_path)
    elif convert_to_audio == "N":
        print("Operação concluída.")
    else:
        print("Opção inválida.")

def convert_video_to_audio(video_file_path):
    # Carregar o arquivo de vídeo usando o MoviePy
    video = VideoFileClip(video_file_path)
    
    # Extrair o nome do arquivo sem a extensão para criar o arquivo de áudio
    audio_file_path = os.path.splitext(video_file_path)[0] + ".mp3"
    
    # Converter o vídeo para áudio e salvar no caminho especificado
    print("Convertendo o vídeo para áudio...")
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    audio.close()
    video.close()
    
    print("Conversão para áudio concluída com sucesso!")

if __name__ == "__main__":
    print("1. Inserir link")
    print("2. Cancelar")
    choice = int(input("Digite o número da opção desejada: "))
    
    if choice == 1:
        download_video()
    elif choice == 2:
        print("Operação cancelada.")
    else:
        print("Opção inválida.")
