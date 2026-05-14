def validaCpf(cpf):
    if not cpf.isdigit():
        return "ocorreu um erro!!! - o cpf deve conter apenas numeros"
    if len(cpf) != 11:
        return "ocorreu um erro!!! - o cpf deve conter 11 digitos"
    else:
        return "cpf valido"


cpf = input("insira o seu CPF: ")
print(validaCpf(cpf))