"""
Crie uma lista para cada informação a seguir:
>Lista de números de 1 a 10;
>Lista com quatro nomes;
>Lista com o ano que você nasceu e o ano atual.
==================================================
Crie uma lista e utilize um loop for para percorrer todos os elementos da lista
==================================================
Utilize um loop for para calcular a soma dos números ímpares de 1 a 10
==================================================
Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente
==================================================
Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10
==================================================
Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções
==================================================
Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

nomes = ["kumo", "otto", "sild", "tharun"]
print(nomes)

anos = [2005, 2026]
print(anos, "\n")
#=================================================

lista = [0, 1, 2, 3, 4]

for i in lista:
    print(i)
print("\n")
#=================================================

soma_impares = 0

for i in range(1, 11, 2):
    soma_impares = i + soma_impares #poderia ser assim tbm --> soma_impares += i
print(soma_impares)
print("\n")
#=================================================

for i in range(10, 0, -1):
    print(i)
print("\n")
#=================================================

num = int(input("digite um numero para ver sua tabuada: "))

for i in range(1, 11):
    tabuada = num * i
    print(f"{num} x {i} = {tabuada}")
print("\n")
#=================================================

lista_nums = [1, 1, 1, 1, 1]
soma_nums = 0

try:
    for num in lista_nums:
        soma_nums += num
    print(soma_nums)
except Exception as e:
    print(f"erro identificado: {e}")
#=================================================

lista_de_numeros = [2, 6, 2, 6, 2]
soma = 0

#! TODO: exolplorar mais as possibilidades de ocorrencia de error no try except
try:
    for numero in lista_de_numeros:
        soma += numero
    media = soma/len(lista_de_numeros)
    print(f"esta e a media da lista: {media}")
except ZeroDivisionError:
    print("a lista esta vazia")
except Exception as e:
    print(f"erro encontrado: {e}")