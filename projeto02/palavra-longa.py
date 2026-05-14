frase = input("digite uma frase: ")

palavraLonga = []

for palavra in frase.split():
    if len(palavra) >= 10:
        palavraLonga.append(palavra)

if palavraLonga:
    print("palavras longas encontradas: ")
    for palavra in palavraLonga:
        print(palavra)
else:
    print("nao ha palavras longas")
