#importacao do pacote random
import random
from os import system, name

#funcao para limpar a tela a cada execucao
def limpa_tela():
    #windows
    if name == 'nt':
        _= system('cls')
    
    #mac ou linux
    else:
        _= system('clear')

#funcao game
def game():
    limpa_tela()
    print("-----Bem vindo ao Jogo da Forca-----")
    print("Adivinhe a palavra abaixo: \n")

#definicao da lista de palavras
palavras_possiveis = ["laranja", "uva", "morango", "banana", "melancia", "amora", "abacate"]

#escolha randomicamente uma palavra
palavra = random.choice(palavras_possiveis)
