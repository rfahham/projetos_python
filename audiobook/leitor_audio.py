from gtts import gTTS
import pygame
import time

def ler_arquivo_texto(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return ""

def falar_com_gtts(texto):
    tts = gTTS(text=texto, lang='pt')
    tts.save("fala.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("fala.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def main():
    texto = ler_arquivo_texto("entrada.txt")
    if texto:
        print("Lendo com gTTS...")
        falar_com_gtts(texto)

if __name__ == '__main__':
    main()
