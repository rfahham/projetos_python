def validar_cpf(cpf):
    # Remova quaisquer caracteres não numéricos do CPF
    cpf = ''. join(filter(str.isdigit, cpf))

    # Verifique se o CPF possui 11 dígitos 
    if len(cpf) != 11:
        return False

    # Calculo do Primeiro Dígito Verificador (YV1)
    soma = 0
    peso = 10
    for i in range(9):
        soma += int (cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        yy1 = 0
    else:
        yy1 = 11 - resto

    # Cálculo do Segundo Dígito Verificador (YV2)
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        yy2 = 0
    else:
        yy2 = 11 - resto

    # Verifique se os dígitos calculados correspondem aos dígitos originais
    if int(cpf[9]) == yy1 and int(cpf[10]) == yy2:
        return True
    else:
        return False

# Exemplo de uso da função para validar um CPF
cpf = input("Insira o número do cpf: ") # Substitua pelo CPF que deseja validar
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")