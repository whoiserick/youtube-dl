from pytube import YouTube
import os
import re

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
    stream.download(output_path=folder_path)
    
    print("Download concluído com sucesso!")

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
