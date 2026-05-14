frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador_vogais = 0

for letra in frase:
    if letra in vogais:
        contador_vogais += 1
print(f"A frase contém {contador_vogais} vogais.")

