"""
Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""
x = float(input("insira um valor para x: "))
y = float(input("insira um valor para y: "))

if x > 0 and y > 0:
    print("vc esta no primeiro quadrante")
elif x < 0 and y > 0:
    print("vc esta no segundo quadrante")
elif x < 0 and y < 0:
    print("vc esta no tericeiro quadrante")
elif x > 0 and y < 0:
    print("vc esta no quarto quadrante")
else:
    print("vc esta na origem")
