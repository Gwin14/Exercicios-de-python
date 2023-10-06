# Num determinado Estado, para transferência de veículos, o DETRAN cobra uma taxa de 1% para carros fabricados antes de 1990, em diante. Taxa essa incidindo sobre o valor de tabela do carro. O algoritmo abaixo lê o ano e o preço do carro e a seguir calcula e imprime imposto a ser pago.

"""
precoCarro = int(input("Diga o preço do carro: "))
dataCarro = int(input("Diga a data do carro: "))

if dataCarro < 1990:
    desconto = precoCarro / 100
    precoCarro += desconto

print(f"O preço do carro é R${precoCarro}")
"""

# Faça um programa que mostre a tabuada de 0 até 9.

"""
for x in range(0, 9):
    for y in range(0, 11):
        print(f"{x} x {y} = {x * y}")
    print("")
"""

# Faça um programa que calcule e escreva a seguinte soma: soma = 1/1 + 3/2 + 5/3 + 7/4 ... + 99/50.

"""
for x in range(1, 100):
    if x % 2 != 0:
        print(f"{x}/{(x + 1) / 2}")
"""

# Escrever um algoritmo que gere e escreve os números ímpares entre 100 e 200.

"""
for x in range(100, 200):
    if x % 2 != 0:
        print(x)
"""

# Faça um algoritmo que leia tantos números que o usuário desejar e imprima a soma dele.

"""
numeroResp = int(input("Diga quantas vezes deseja somar numeros: "))
soma = 0

for x in range(numeroResp):
    mais = int(input(f"Diga o número {x}:"))
    soma += mais

print(f"O total da soma de todos os números deu: {soma}")
"""
