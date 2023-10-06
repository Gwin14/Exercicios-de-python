# Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool: até 20 litros, desconto de 3% por litro e acima de 20 litros, desconto de 5% por litro. Gasolina: até 20 litros desconto de 4% por litro e acima de 20 litros, desconto de 6% por litro. Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (A-álcool, G-gasolina) e imprima o valor a ser pago pelo cliente. Considere que o preço do litro da gasolina é R$2,99 e o preço do litro de álcool é RS2,19.

"""
tipoCombustivel = input("Informe o tipo do combustível A/G: ")
litrosVendidos = float(input("Informe a quantidade de litros vendidos: "))

if tipoCombustivel == "A":
    if litrosVendidos > 20:
        desconto = litrosVendidos * 2.19 / 100 * 5
        print(f"O valor total deu R${litrosVendidos * 2.19 - desconto}")
    else:
        desconto = litrosVendidos * 2.19 / 100 * 3
        print(f"O valor total deu R${litrosVendidos * 2.19 - desconto}")
elif tipoCombustivel == "G":
    if litrosVendidos > 20:
        desconto = litrosVendidos * 2.19 / 100 * 6
        print(f"O valor total deu R${litrosVendidos * 2.19 - desconto}")
    else:
        desconto = litrosVendidos * 2.19 / 100 * 3
        print(f"O valor total deu R${litrosVendidos * 2.19 - desconto}")
else:
    print("Informe A ou G")
"""

# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um apresenta em relação ao total de eleitores.

"""
totalEleitores = int(input("Diga o total de eleitores: "))

votosBrancos = int(input("Diga o total de votos brancos: "))
votosNulos = int(input("Diga o total de votos nulos: "))
votosValidos = int(input("Diga o total de votos válidos: "))

totalBrancos = votosBrancos / 100 * totalEleitores
totalNulos = votosNulos / 100 * totalEleitores
totalValidos = votosValidos / 100 * totalEleitores


print(f"A procentagem de votos brancos é de {totalBrancos}%")
print(f"A procentagem de votos nulos é de {totalNulos}%")
print(f"A procentagem de votos válidos é de {totalValidos}%")
"""

# As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total de compra.

"""
macas = int(input("Diga a quantidade de maçãs compradas: "))
preco = 1.30

if macas >= 12:
    preco = 1.00

print(f"O valor total a pagar é R${macas * preco}")
"""
