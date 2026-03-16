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

sabores = []

#exibe as opcoes de entrada do programa
def exibe_opcao():
    print("""
    ==================================================================
    1.Cadastrar novo sabor
    2.Listar sabores
    3.Ativar sabor
    4.Sair
    ==================================================================
    """)

#entrada de uma opcao no programa
def selecina_opcao():
    #try except e um metodo para tratamento de erro
    try:
        theChosen = int(input("selecione uma opcao: "))

        if theChosen == 1:
            cadastrar_novo_sabor()
        elif theChosen == 2:
            listagem_de_sabores()
        elif theChosen == 3:
            print("vc escolheu ativar um sabor")
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

#caso entrada seja uma opcao invalida, exibe a mensagem de invalidez e ao teclar ENTER volta para o menu
def opcao_invalida():
    print("opcao invalida")
    input("tecle qualquer coisa para voltar\n" + "\n")
    main()

#esta funcao adciona um novo item a lista de sabores
def cadastrar_novo_sabor():
    os.system("cls")
    print("cadastro de novo sabor\n")
    nome_do_sabor = input("insira o nome do novo sabor: ")
    sabores.append(nome_do_sabor)
    print(f"sabor {nome_do_sabor} adicionado ao cardapio!")
    retorna_menu_principal()

#esta funcao lista todos os sabores contidos na lista
def listagem_de_sabores():
    os.system("cls")
    print("listando os sabores\n")
    #um laco de repeticao para emitir a lista de sabores
    #caso haja itens(sabores) dentro da lista de sabores ele ira exibir os sabores 
    for sabor in sabores:    
        print(f">>{sabor}")
    retorna_menu_principal()

#retorna para o menu principal da aplicacao
def retorna_menu_principal():
    input("\ndigite qualquer tecla para voltar ao menu")
    main()

#contem todos as funcoes deste arquivo (app.py)
def main():
    os.system("cls")
    nome_programa()
    exibe_opcao()
    selecina_opcao()

if __name__ == '__main__':
    main()