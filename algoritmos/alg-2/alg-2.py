import random
import os

palavras = []

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def divisor():
    print("............................................")

def lerTxt(palavras):
    with open('/home/thayro/Repos/atividades-finais/algoritmos/alg-2/palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

def escolherPalavra(palavras):
    index = random.randint(0, len(palavras) - 1)
    return palavras[index]

def exibir_palavra_misteriosa(palavra_escolhida, letras_certas):
    for n in palavra_escolhida:
        if n in letras_certas:
            print(n, end=" ", flush=True)
        else:
            print("_", end=" ", flush=True)
    print("\n")
    divisor()

def jogada():
    letra_escolhida = input('- Tente adivinhar uma letra: ').lower()
    return letra_escolhida

def jogar():
    game = True
    letras_certas = []
    lerTxt(palavras)
    palavra_escolhida = escolherPalavra(palavras)
    while game:
        limpar_terminal()
        exibir_palavra_misteriosa(palavra_escolhida, letras_certas)
        letra = jogada()
        
        if letra in palavra_escolhida and letra not in letras_certas:
            letras_certas.append(letra)
        
        if set(letras_certas) == set(palavra_escolhida):
            print("Parabéns! Você adivinhou a palavra:", palavra_escolhida)
            game = False

jogar()
