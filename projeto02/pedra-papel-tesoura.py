#+++++REQUISITOS+++++
#user escolhe entre as opcoes de pedra papel ou tesoura
#maquina escolhe aleatoriamente entre as mesmas
#====================
#pedra > tesoura
#tesoura > papel
#papel > pedra
#opcao do user = opcao maquina -> empate
#====================
#saida esperada:
#user: $opcao$
#maquina: $opacao$
#voce $venceu ou perdeu$

import random

print('''
Escolha uma da opcoes:
>> 1-PEDRA
>> 2-PAPEL
>> 3-TESOURA
''')

def ped_pap_tes():
    opcoes = ['pedra','papel','tesoura']
    maquinaOpcao = random.choice(opcoes)
    userOpcao = int(input("sua opcao eh? "))

    if userOpcao not in [1,2,3]:
        print("escolha uma opcao valida")
        return
    
    if userOpcao == 1:
        userOpcao = opcoes[0]
    elif userOpcao == 2:
        userOpcao = opcoes[1]
    elif userOpcao == 3:
        userOpcao = opcoes[2]

    print(f'''
user: {userOpcao}
maquina: {maquinaOpcao}
''')

    if userOpcao == maquinaOpcao:
        print("Empate")
    elif (
        (userOpcao == 'pedra' and maquinaOpcao == 'tesoura') or
        (userOpcao == 'papel' and maquinaOpcao == 'pedra') or
        (userOpcao == 'tesoura' and maquinaOpcao == 'papel')
    ):
        print("humano venceu")
    else:
        print("humano otario, foi derrota por uma maquina kkkkkkkkkkk")

ped_pap_tes()
