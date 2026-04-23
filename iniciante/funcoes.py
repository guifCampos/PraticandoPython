def idade(anoNasc, anoAtual):
    return anoAtual - anoNasc
    

nasc = int(input("digite seu ano de nascimento: "))
atual = int(input("digite o ano atual: "))

idadePessoa = idade(nasc, atual)

print(f"sua idade e {idadePessoa}")

#==============================================================

def conta_letras(letras):
    return len(letras)

palavra = str(input("insira uma palavra: "))

print(f"a palavra contem {conta_letras(palavra)} letras")

#==============================================================

def mensagem_do_dia(horario):
    if horario < 12:
        return "bom dia"
    elif 12 <= horario < 18:
        return "boa tarde"
    else:
        return "boa noite"

hora = int(input("digite a hora atual (0-23): "))
print(f"{mensagem_do_dia(hora)}")

#==============================================================

def converte_int(lista):
    return[int(telefone) for telefone in lista]

def confirm_conversao(lista):
    for num in lista:
        if not isinstance(num, int):
            return "erro na conversao"
        
    return "telefones convertidos com sucesso"

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 


telefones_converts = converte_int(telefones)
print(confirm_conversao(telefones_converts))

#==============================================================
'''
valores = input("digite os valores das vendas: ").split()
total = sum(map(float, valores))
print(f"total de vendas foi: {total}")
'''
#fazendo "no pelo"

def vendas():
    valorDeVenda = input("insira os valores das vendas: ")
    listaVendas = valorDeVenda.split()

    total = 0

    for item in listaVendas:
        valorInteiro = int(item)
        total += valorInteiro

    return total

resultadoDeVendas = vendas()
print(f"total de vendas foi de: {resultadoDeVendas}")

#==============================================================

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numPares(num):
    return num % 2 ==0

numeros = list(filter(numPares, listaNumeros))
print(numeros)

#==============================================================

frutas = input("digite a fruta separando por barras: ").split("/")
precos = input("digite os precos separando por barras: ").split("/")

for frutas, precos in zip(frutas, precos):
    print(f"{frutas.strip()} | {precos.strip()}")
    
#==============================================================

x = int(input("digite um numero: "))
y = int(input("digite outro numero: "))

soma = lambda x, y: x + y 
subtrai = lambda x, y: x - y 
multiplica = lambda x, y: x * y 
divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

operacao = input("escolha uma operacao | + | - | * | / |: ")

if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida")

#==============================================================


def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       return valor - (valor * (porcentagem / 100))  

   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  

calcular_preco_final = criar_desconto(desconto) 

valor = float(input("Digite o valor da compra: "))  

print(f"Preço final com desconto: {calcular_preco_final(valor)}") 

#==============================================================

def somaNumeros(n):
    if n == 1:
        return 1
    else:
        return n + somaNumeros(n-1)
    
numero = int(input("insira um numero: "))
print(somaNumeros(numero))