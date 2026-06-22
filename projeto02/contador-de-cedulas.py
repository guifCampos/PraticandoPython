#++++++++REQUISITOS+++++++
#programa deve solicitar um valor (inteiro) ao user
#contar a quantiade de cedulas para aquele valor
#usar a menor quantidade de cedulas possiveis
#$100 | $50 | $20 | $10 | $5 | $2
#deve possuir tratamento de erro caso haja uma entrada invalida
#>>valores impares -> valor deve ser multiplo de 2
#>>valor igual a 0 -> o valor deve ser positivo e maior q zero

def caixa():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor_saque = int(input("qual o valor q deseja sacar? "))

        if valor_saque <= 0:
            print("o valor precisa ser positivo")
            print("o valor deve ser maior q zero")
        elif valor_saque % 2 != 0:
            print("o valor dever um numero par")
        else:
            print('''CEDULAS ENTREGUES
================
''')
            for cedula in cedulas:
                quantia = valor_saque//cedula
                if quantia > 0:
                    print(f"{quantia} cedula de ${cedula}")
                    valor_saque = valor_saque % cedula
    except ValueError:
        print("digite um valor numerico inteiro valido")

caixa()