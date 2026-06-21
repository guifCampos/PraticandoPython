#----REQUISITOS----
#programa com menu interativo
#funcoes:
#>adicionar tarefa
#>visualizar tarefas
#>remover tarefa
#buscar tarefa por palavra-chave
#sair do programa
#------------------
#entrada esperada:
#1.adicionar tarefa
#2.visualizar tarefas
#3.remover tarefa
#4.buscar tarefa por palavra-chave
#5.sair do programa
#escolha uma opcao: $
#------------------
#saida esperada:
#em caso de adicionar tarefa:
#digite a tarefa: tarefa 1
#tarefa adicionada com sucesso!
#==============================
#em caso de visualizar tarefas:
#tarefas:
#1. tarefa 1
#==============================
#em caso de remover tarefa:
#digite o numero da tarefa a ser removida: 1
#certeza de que deseja remover a tarefa 1? (s/n): s/n
#tarefa removida com sucesso!
#em caso de nao remover a tarefa >> tarefa nao removida.
#==============================
#em caso de buscar tarefa por palavra-chave:
#digite a palavra-chave: tarefa
#tarefas encontradas:
#1. tarefa 1
#==============================
#em caso de sair do programa:
#saindo do programa... ate logo!

import os
import time

lista_tarefa = []

def menuExibe():
    limpa_tela()
    print('''
H--------------------------H
H>> 1)Adicionar Tarefa     H
H>> 2)Visualizar Tarefa    H
H>> 3)Remover Tarefa       H
H>> 4)Buscar Tarefa        H
H>> 5)Alterar Status Trefa H
H>> 0)Sair                 H
H--------------------------H
''')
    
def opcoesMenu():

    try:
        user_opcao = int(input("o q deseja fazer: "))

        if user_opcao == 1: #adiconar tarefa
            add_tarefa()
        elif user_opcao == 2: #vizualizar lista de tarefas
            visualiza_tarefas()
        elif user_opcao == 3: #remover tarefa
            dlt_tarefa()
        elif user_opcao == 4: #buscar tarefa
            busca_tarefa()
        elif user_opcao == 5: #alterar status da tarefa
            altera_status_tarefa()
        elif user_opcao == 0: #sair/encerrar do programa
            encerra_programa()
        else:
            opcao_invalida()
    except:
        pass

def add_tarefa(): #nome da tarefa | prazo(curto/medio/longo) | status (pendente - por padrao)
    limpa_tela()
    
    print('''
ADICIONA TAREFA
===============
''')
    
    nome_tarefa = input("qual a tarefa a ser feita? ")
    prazo_tarefa = input("ela eh de curto, medio ou longo prazo? ")
    dados_tarefa = {'tarefa':nome_tarefa, 'prazo':prazo_tarefa, 'status':False}
    lista_tarefa.append(dados_tarefa)

    print("sua tarefa foi adicionada a lista. para ve-la volte ao menu e va em '2)Visualizar'")
    retorna_menu()

def visualiza_tarefas():
    limpa_tela()
    
    print('''LISTANDO TAREFAS
================
''')
    
    for tarefa in lista_tarefa:
        nome_tarefa = tarefa['tarefa']
        prazo_tarefa = tarefa['prazo']
        status_tarefa = tarefa['status']
        status_tarefa = 'CONCLUIDA' if tarefa['status'] else 'PENDENTE'
        print(f">>{nome_tarefa.ljust(9)} | {prazo_tarefa.ljust(9)} | {status_tarefa}")
    
    retorna_menu()

def dlt_tarefa():
    limpa_tela()

    print('''DELETANDO TAREFA
================
''')

    nome_tarefa = input("qual a tarefa que deseja remover da lista? ")
    tarefa_encontrada = False

    for tarefa in lista_tarefa:
        if nome_tarefa == tarefa['tarefa']:
            tarefa_encontrada = True
            
            decisao =input("voce deseja desistir de cumprir esta tarefa? vai arregar mesmo?(sim/nao) ")
            if decisao == "sim":
                lista_tarefa.remove(tarefa)
                print("sua tarefa foi removida. voce arregou, guerreiro. que decepcao.")
                retorna_menu()
            elif decisao == "nao":
                print("sua tarefa nao sera removida. parabens por nao desistir, guerreiro. orgulho de ti.")
                retorna_menu()
            else:
                print("insira uma resposta valida (sim/nao)")
                time.sleep(3)
                dlt_tarefa()

    if not tarefa_encontrada:
        print("nao ha a tarefa mencionada.\n")
        time.sleep(2)
        decisao2 = input("deseja tentar deletar outra tarefa? ")
        if decisao2 == "sim":
            dlt_tarefa()
        elif decisao2 == "nao":
            retorna_menu()

def busca_tarefa():
    limpa_tela()

    print('''BUSCANDO TAREFA
================
''')

    nome_tarefa = input("qual/quais tarefas voce esta procurando? ")
    tarefa_encontrada = False

    for tarefa in lista_tarefa:
        if nome_tarefa in tarefa['tarefa']: 
            print(f">>{tarefa['tarefa']} | {tarefa['status']}")
            tarefa_encontrada = True
            
    if tarefa_encontrada == False:
        print(f"nao foram encontradas tarefas com esse nome: {nome_tarefa}")
        time.sleep(2)

        decisao3 = input("deseja buscar por outra tarefa? ")

        if decisao3 == "sim":
            busca_tarefa()
        elif decisao3 == "nao":
            retorna_menu()

    retorna_menu()


def altera_status_tarefa():
    limpa_tela()

    print('''ALTERANDO STATUS DA TAREFA
================
''')
    
    nome_tarefa = input("qual tarefa voce deseja alterar o status? ")
    tarefa_encontrada = False

    for tarefa in lista_tarefa:
        if nome_tarefa == tarefa['tarefa']:
            tarefa_encontrada = True
            tarefa['status'] = not tarefa['status']
            print(f"a tarefa {nome_tarefa} teve o status dela alterado")
            retorna_menu()

    if not tarefa_encontrada:
        print("nao ha a tarefa mencionada.\n")
        time.sleep(2)
        decisao2 = input("deseja tentar alterar outra tarefa? ")
        if decisao2 == "sim":
            altera_status_tarefa()
        elif decisao2 == "nao":
            retorna_menu()

def encerra_programa():
    limpa_tela()
    print("saindo...")

def opcao_invalida():
    print("opcao invalida")
    input("tecle ENTER para voltar\n" + "\n")
    main()

def limpa_tela():
    os.system("cls")

def retorna_menu():
    input("\ntecle ENTER para voltar ao menu")
    main()

def main():
    menuExibe()
    opcoesMenu()

if __name__ == '__main__':
    main()