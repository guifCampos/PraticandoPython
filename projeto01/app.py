import os

#define o nome do programa
def nome_programa(): 
    print(
    """

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝█████╗░░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║███████╗██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░

    ██████╗░░█████╗░████████╗░█████╗░███████╗░█████╗░░██████╗░░█████╗░
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝░██╔══██╗
    ██████╦╝██║░░██║░░░██║░░░███████║█████╗░░██║░░██║██║░░██╗░██║░░██║
    ██╔══██╗██║░░██║░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░╚██╗██║░░██║
    ██████╦╝╚█████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝╚██████╔╝╚█████╔╝
    ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░╚═════╝░░╚════╝░
    """
    )

#exibe as opcoes de entrada do programa
def exibe_opcao():
    print("""
    ==================================================================
    1.Cadastrar restaurante
    2.Listar restaurantes
    3.Ativar restaurante
    4.Sair
    ==================================================================
    """)

#entrada de uma opcao no programa
def selecina_opcao():
    try:
        theChosen = int(input("selecione uma opcao: "))


        if theChosen == 1:
            print("vc escolheu cadastrar um restaurante")
        elif theChosen == 2:
            print("vc escolheu listar os restaurantes")
        elif theChosen == 3:
            print("vc escolheu ativar um restaurante")
        elif theChosen == 4:
            encerra_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#limpa o terminal deixando apenas a mensagem do print
def encerra_app():
    os.system("cls")
    print("encerrando app")


def opcao_invalida():
    print("opcao invalida")
    input("tecle qualquer coisa para voltar\n" + "\n")
    main()

#contem todos as funcoes deste arquivo (app.py)
def main():
    nome_programa()
    exibe_opcao()
    selecina_opcao()

if __name__ == '__main__':
    main()