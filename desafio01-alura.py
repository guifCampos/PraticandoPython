#sistema de delivery o qual o valor da taxa depende da distancia ate o cliente e se o pedido foi feito em dia de chuva
#Regras:
#1. entrega de ate 5km, taxa = 5brl
#2. entrega de 5km a 10km, taxa = 8brl
#3. entrega de 10km a 20km, taxa = 10brl
#4. estado de chuva, soma-se 2brl a taxa padrao

distancia = float(input("qual a distancia? >>"))

chuva = input("esta chovendo?(s/n) >>")

if distancia <= 5:
    taxa = 5
    print(f"valor adicional da taxa e de {taxa}brl")
elif distancia <= 10:
    taxa = 8
    print(f"valor adicional da taxa e de {taxa}brl")
elif distancia <= 20:
    taxa = 10
    print(f"valor adicional da taxa e de {taxa}brl")
else:
    print("valor invalido para distancia")

if chuva == "s":
    taxa += 2
    print(f"valor adicional da taxa e de {taxa}brl")
elif chuva == "n":
    print(f"valor da taxa nao sofreu alteracao")

print(f"\nvalor final da taxa de entrega e de {taxa}brl")