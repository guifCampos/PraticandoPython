#+++++REQUISITOS+++++
#user seleciona o nivel de dificuldade
#facil >> 0-10 com 5 tentativas
#medio >> 0-50 com 6 tentativas
#dificil >> 0-100 com 7 tentativas
#====================
#sistema gera um numero aleatoria de 0 a 100
#user digita um numero
#user acerta numero >> user venceu
#user erra numero >> sistema da uma dica se e maior ou menor e continua o jogo
#user esgota as tentativas >> user perdeu

import random
import os

def seleciona_dificuldade():
    print('''
#SELECIONE O MODO DE JOGO#
#========================#
#>>1)FACIL - 5x | 0-10   # 
#>>2)MEDIO - 6x | 0-50   #
#>>3)DIFICIL - 7x | 0-100#
#========================#
''')
    userOpacao = input("digite o nivel de dificuldade desejado: ").lower()

    if userOpacao == "1" or userOpacao == "facil":
        facil()
    elif userOpacao == "2" or userOpacao == "medio":
        medio()
    elif userOpacao == "3" or userOpacao == "dificil":
        dificil()
    else:
        print("opcao invalida")
        limpa()
        seleciona_dificuldade()     


def facil():
    numeroSecreto = random.randint(0,10)
    maxTentativas = 5
    
    for tentativas in range(maxTentativas):
        try:
            palpite = int(input("tente adivinhar o numero (0-10): "))

            if not 0 <= palpite <= 10:
                raise ValueError("numero nao esta no intervalo. insira um numero entre 0 e 10")

            if palpite == numeroSecreto:
                print("parabens vc acertou!")
                input("tecle qualquer coisa para voltar ao menu\n" + "\n")
                break

            elif palpite > numeroSecreto:
                print("numero secreto e menor")
            
            elif palpite < numeroSecreto:
                print("numero secreto e maior")   
        
        except ValueError as e:
            print(f"entra invalida: {e}")
    else:
        print(f"vc perdeu, o numero era {numeroSecreto}")

    limpa()
    seleciona_dificuldade()

def medio():
    numeroSecreto = random.randint(0,50)
    maxTentativas = 6
    
    for tentativas in range(maxTentativas):
        try:
            palpite = int(input("tente adivinhar o numero (0-50): "))

            if not 0 <= palpite <= 50:
                raise ValueError("numero nao esta no intervalo. insira um numero entre 0 e 50")

            if palpite == numeroSecreto:
                print("parabens vc acertou!")
                input("tecle qualquer coisa para voltar ao menu\n" + "\n")
                break

            elif palpite > numeroSecreto:
                print("numero secreto e menor")
            
            elif palpite < numeroSecreto:
                print("numero secreto e maior")   
        
        except ValueError as e:
            print(f"entra invalida: {e}")
    else:
        print(f"vc perdeu, o numero era {numeroSecreto}")

    limpa()
    seleciona_dificuldade()

def dificil():
    numeroSecreto = random.randint(0,100)
    maxTentativas = 7
    
    for tentativas in range(maxTentativas):
        try:
            palpite = int(input("tente adivinhar o numero (0-100): "))

            if not 0 <= palpite <= 100:
                raise ValueError("numero nao esta no intervalo. insira um numero entre 0 e 100")

            if palpite == numeroSecreto:
                print("parabens vc acertou!")
                input("tecle qualquer coisa para voltar ao menu\n" + "\n")
                break

            elif palpite > numeroSecreto:
                print("numero secreto e menor")
            
            elif palpite < numeroSecreto:
                print("numero secreto e maior")   
        
        except ValueError as e:
            print(f"entra invalida: {e}")
    else:
        print(f"vc perdeu, o numero era {numeroSecreto}")

    limpa()
    seleciona_dificuldade()

def limpa():
    os.system("cls")

seleciona_dificuldade()


