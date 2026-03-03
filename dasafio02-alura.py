#conversor de moedas
#tipos de convesoes:
#brl >> us
#brl >> eur
#us >> brl
#us >> eur
#eur >> brl
#eur >> us
print(
"""
----CONVERSOES----
>>BRL -> US
>>BRL -> EUR
"""
)
valor = float(input("insira o valor que deseja converter: >>"))
tipoDeCambio = input("qual tipo do cambio? (US || EUR) >>")

if tipoDeCambio == "us":
    dolarCambio = valor//5
    print(f"esse e o valor em dolar: {dolarCambio}")
elif tipoDeCambio == "eur":
    eurCambio = valor//6
    print(f"esse e o valor em euro: {eurCambio}")
else:
    print("tipo de cambio invalido")


