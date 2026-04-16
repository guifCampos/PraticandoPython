maca = input("quantas macas foram vendidas? ")
banana = input("quantas bananas foram vendidas? ")

print(f"macas vendidads: {maca} || bananas vendidas: {banana}")

if maca > banana:
    print("macas tiveram maior venda")
elif banana > maca:
    print("bananas tiveram maior venda")
else:
    print("vendas foram equilibradas")

#==============================================================

print("\ndigite o tempo em dias\n")
a = int(input("quanto tempo vc levou para concluir a atividade A? "))
b = int(input("quanto tempo vc levou para concluir a atividade B? "))
c = int(input("quanto tempo vc levou para concluir a atividade C? "))

if (a >= 0 and b >= 0 and c >= 0):
    tempo_total = a + b + c
    print(f"{a} + {b} + {c} = {tempo_total}")
else:
    print("os dias devem ser positivos")

#==============================================================

temp_limite = 23

temp_atual = float(input("qual a temperatura atual? "))

if temp_atual > temp_limite:
    print("Alerta! temperatura acima do limite permitido")
else:
    print("temperatura dentro do limite")

#==============================================================

peso = float(input("qual o seu peso (kg)? "))
altura = float(input("qual a sua altura (m)? "))

imc = peso/altura**2

print(f"seu imc e: {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 25:
    print("peso ideal")
elif imc >= 25:
    print("acima do peso")

#==============================================================

limite = 3000

despesasDoMes =  float(input("digite o total das despesas do mes: "))

if despesasDoMes <= limite:
    print("vc esta dentro do orçamento")
elif despesasDoMes > limite:
    print("ATENÇÃO!!! vc passou do limite do orçamento")


#==============================================================

num = int(input("digite um numero: "))

parImpar = num % 2

if parImpar == 0:
    print("numero e par")
else:
    print("numero e impar")

#==============================================================

rendaMensal = 2000

minhaRm = int(input("digite sua renda mensal: "))
parcela = int(input("digite o valor da parcela desejada: "))

if minhaRm * 0.3 < parcela and minhaRm > rendaMensal:
    print("parcela approved")
elif minhaRm <= rendaMensal:
    print("emprestimo not approved - renda insuficiente")
else:
    print("parcela not approved - acima de 30% da renda")
