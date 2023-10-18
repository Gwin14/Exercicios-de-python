# Calcular porcentagem usando função

"""
numero = int(input("Diga um número: "))
porcentagem = int(input("Diga uma porcentagem: "))


def calcular_porcentagem(numero, porcentagem):
    return numero / 100 * porcentagem


print(calcular_porcentagem(numero, porcentagem))
"""

# Calcular quantos dias se passaram desde o início do ano

mesAtual = int(input("Diga que mês é hoje: "))
diaAtual = int(input("Diga que dia é hoje: "))


def calcularDias(diaAtual, mesAtual):
    mesAtual = (mesAtual - 1) * 30
    return diaAtual + mesAtual


print(f"Se passaram {calcularDias(diaAtual, mesAtual)} dias desde o início do ano.")
