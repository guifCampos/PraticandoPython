clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

#==============================================================

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1 #adicionado a operacao para que a condicao colocada no loop While rodasse enquanto o contador fosse menor que 10 (0-9)

#==============================================================

'''
menos verbal
um pouco mais rapido para a ocasiao
sabe-se exatamente qnd deve-se parar
'''
for i in range(5):
    print("bem-vindo buscante")

#ou

'''
mais verbal
um pouco mais lento para a ocasiao
nao se sabe qnd deve parar
'''
mensagem = 0

while mensagem < 5:
    print("bem-vindo buscante")
    mensagem += 1

#==============================================================

valores = [10, 20, 30, 40, 50]

total = 0

for valor in valores:
    total += valor
    print(f"a soma dos valores e: {total}")#print dentro do loop para verificar os resultados das somas anteriores

#==============================================================

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None: #posso subrtituir o "==" para "is", pois diz que se projeto é None, exibe a mensagem
        print("projeto ausente")
    else:
        print(f"{projeto}")
    
#==============================================================

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"o livro {livro} foi encontrado")
        break   #para a busca qnd o item espcifico e encontrado
    else:
        print("livro nao encontrado")
        break   #adicionada a instrucao break para evitar que a mensagem se repita mais vezes para o item nao encontrado

#==============================================================

estoque = 5

while estoque > 0:
    estoque -= 1
    print(f"venda feita! estoque restante: {estoque}")

print("sold out")

#==============================================================

for seg in range(10, 0, -1):
    if seg % 2 == 0:
        print(f"faltam apenas {seg}s - nao perca a oportunidade")
    else:
        print(f"a contagem continua: {seg}s restantes")

print("aproveite a promocao")

#==============================================================

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
       continue
    print(f"livro disponivel: {livro['nome']}")

#==============================================================

while True:
    nome = input("digite o nome de usuario: ")
    senha = input("digite a senha: ")

    if len(nome) < 5:
        print("nome de user deve conter pelo menos 5 caracteres")
        continue

    if len(senha) < 8:
        print("senha deve conter pelo menos 8 caracteres")
        continue

    print(f"usuario {nome} foi cadastrado com sucesso")
    break