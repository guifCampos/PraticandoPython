#aqui estarao alguns algoritmos basicos que farei para praticar minha logica de programacao

#soma de numeros/variaveis
g = 21
m = 18

a = g + m

print(a, "\n")

#--------------------------

x = int(input("Digite um valor numerico inteiro: "))
y = float(input("Digite um valor numerico real: "))

soma = float(x + y)

print(soma, "\n")

#---------------------------

letra1 = str(input("Digite uma letra: "))
letra2 = str(input("digite uma segunda letra: "))

somaLetras = letra1 + letra2

print(somaLetras, "\n")

#---------------------------
#verificando se um numero e par ou impar
n1 = float(input("insira um numero: "))

divisao = n1 % 2

if divisao == 0:
    print(n1, " e par")
else:
    print(n1 , " e impar\n")

#----------------------------
#verificando se individuo e menor, maior de idade ou idoso

idade = int(input("qual a sua idade? "))

if idade < 18:
    print("\nvc e menor de idade")
elif idade >= 18 and idade < 60:
    print("\nvc e maior de idade")
else:
    print("\nvc e idoso")