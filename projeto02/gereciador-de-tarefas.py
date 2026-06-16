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

lista_tarefa = []

def menuExibe():
    os.system("cls")
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
            pass
        elif user_opcao == 4: #buscar tarefa
            pass
        elif user_opcao == 5: #alterar status da tarefa
            pass
        elif user_opcao == 0: #sair/encerrar do programa
            pass
        else:
            pass
    except:
        pass

def add_tarefa(): #nome da tarefa | prazo(curto/medio/longo) | status (concluida/pendente)
    os.system("cls")
    
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
    os.system("cls")
    
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


def retorna_menu():
    input("\ntecle ENTER para voltar ao menu")
    main()

def main():
    menuExibe()
    opcoesMenu()

if __name__ == '__main__':
    main()