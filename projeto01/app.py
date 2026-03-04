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
    ==================================================================
    1.Cadastrar restaurante
    2.Listar restaurantes
    3.Ativar restaurante
    4.Sair
    ==================================================================
    """
    )


def exibe_opcao():
    print("""
    ==================================================================
    1.Cadastrar restaurante
    2.Listar restaurantes
    3.Ativar restaurante
    4.Sair
    ==================================================================
    """)


#limpa o terminal deixando apenas a mensagem do print
def encerra_app():
    os.system("cls")
    print("encerrando app")


theChosen = int(input("selecione uma opcao: "))


if theChosen == 1:
    print("Vvc escolheu cadastrar um restaurante")
elif theChosen == 2:
    print("vc escolheu listar os restaurantes")
elif theChosen == 3:
    print("vc escolheu ativar um restaurante")
elif theChosen == 4:
    encerra_app()
else:
    print("selecione uma opção válida")



def main():
    nome_programa()
    exibe_opcao()

if __name__ == __main__:
    main()