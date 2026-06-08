#+++REQUISITOS+++
#================================
#deve conter:
#letras maiusculas (A-Z)
#letras minusculas (a-z)
#numeros (0-9)
#especiais (!@#$%&*)
#================================
#tamanho fixo de 12 caracteres
#================================
#exibir a senha gerada
#saida esperada ==> A1b@C3d$E5f&
#================================

import random

def gera_senha():
    maiscula = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minuscula = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numero = ['0','1','2','3','4','5','6','7','8','9']
    especiais = ['!','@','#','$','%','&','*']

    senha = [
        random.choice(maiscula),
        random.choice(minuscula),
        random.choice(numero),
        random.choice(especiais)
    ]

    caracteres = maiscula + minuscula + numero + especiais
    senha.extend(random.choices(caracteres, k=8))
    random.shuffle(senha)
    
    return ''.join(senha)

print(f"senha gerada foi: {gera_senha()}")