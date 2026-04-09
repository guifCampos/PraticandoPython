import os

#dicionario com os sabores de pizza pre-estabelecidos
sabores = [{'nome': 'Pepperoni', 'categoria': 'Salgada', 'disponibilidade': True},
           {'nome': 'Banana Nevada', 'categoria': 'Doce', 'disponibilidade': False},
           {'nome': 'Marguerita', 'categoria': 'Salgada', 'disponibilidade': True}
           ]

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
            alterna_disponibilidade_do_sabor()
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
    nome_do_sabor = input("digite o nome do sabor: ")
    categoria_sabor = input(f"digite a categoria do sabor (salgado ou doce): ")
    dados_do_sabor = {'nome':nome_do_sabor, 'categoria':categoria_sabor, 'disponibilidade':False}
    sabores.append(dados_do_sabor)
    print(f"o sabor {nome_do_sabor} foi adicionado com sucesso ao cardapio")
    retorna_menu_principal()

#esta funcao lista todos os sabores contidos na lista
def listagem_de_sabores():
    os.system("cls")
    print("listando os sabores\n")
    #laco de repeticao para emitir a lista de sabores
    #caso haja itens(sabores) dentro da lista de sabores ele ira exibir os sabores

    print(f"{'SABOR'.ljust(21)} || {'CATEGORIA'.ljust(21)} || DISPONIBILIDADE")
    for sabor in sabores:
        nome_sabor = sabor['nome']
        categoria_sabor = sabor['categoria']
        disponibilidade_sabor = sabor['disponibilidade']
        disponibilidade_sabor = 'Disponivel' if sabor['disponibilidade'] else 'Indisponivel'   
        print(f">>{nome_sabor.ljust(19)} || {categoria_sabor.ljust(21)} || {disponibilidade_sabor}")
    retorna_menu_principal()

#alterna o estado de disponibilidade de um sabor de pizza no cardapio
def alterna_disponibilidade_do_sabor():
    print("alterando disponibilidade do sabor\n")
    nome_sabor = input("digite o nome do sabor que deseja alterar a disponibilidade: ")
    sabor_encontrado = False
    
    for sabor in sabores:
        if nome_sabor == sabor['nome']:
            sabor_encontrado = True
            sabor['disponibilidade'] = not sabor['disponibilidade']
            notificacao = f"o sabor {nome_sabor} ficou disponivel" if sabor['disponibilidade'] else f"o sabor {nome_sabor} nao esta disponivel"
            print(notificacao)

    #condicional para caso nao haja o sabor no cardapio
    if not sabor_encontrado:
        print("sabor nao encontrado no cardapio")

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