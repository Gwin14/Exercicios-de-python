# Chico tem 1,50m e cresce 2 centímetros por ano, enquanto luca tem 1,10m e cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima quantos anos serão necessários para que luca seja maior que chico.

"""
alturaChico = 1.50
alturaLuca = 1.10
anosPassados = 0

while alturaChico > alturaLuca:
    alturaChico += 0.02
    alturaLuca += 0.03
    anosPassados += 1

print(
    f"Se passaram {anosPassados} anos para que Luca tenha passado Chico. \n Chico ficou com {round(alturaChico, 2)}m de altura. \n Luca ficou com {round(alturaLuca, 2)}m de altura"
)
"""

# Faça um algoritmo que leia vários números e informe quantos desses números entre 100 e 200 foam digitados. Quando o valor 0 (zero) for lido o algoritmo deverá cessar sua execução.

"""
contagem = 0

while True:
    numero = int(
        input(
            "Diga um número entre 100 e 200 para contar, e digite 0 para encerrar o programa: "
        )
    )

    if numero == 0:
        print(f"Encerrado, foram digitados {contagem} números (sem contar com 0).")
        break
    elif numero < 100 or numero > 200:
        print("Somente números entre 100 e 200.")
    else:
        print("Número contado, continue digitando.")
        contagem += 1
"""

# Construa um algoritmo que leia uma quantidade indeterminada de números inteiros positivos e identifique qual for o maior número digitado. O final da série de números deve ser indicado pela entrada de -1

"""
maiorNumero = -2

while True:
    numero = int(
        input(
            "Diga um números para no final dizer qual foi o maior digitado, encerre com -1: "
        )
    )

    if numero == -1:
        if numero > maiorNumero:
            maiorNumero = numero
        print(f"O maior número digitado foi {maiorNumero}.")
        break

    if numero < 0:
        print("Somente números positivos.")
        continue

    if numero > maiorNumero:
        maiorNumero = numero
"""

# Escreva um aplicativo que recebe inteiro e recebe os números pares e ímpares (separados), de 1 até esse inteiro.

"""
numero = int(input("Informe um número: "))

for x in range(1, numero + 1):
    if x % 2 == 0:
        print(f"Par: {x}")
    else:
        print(f"Ímpar: {x}")
"""

# Uma rainha requisito os serviços de um monge,o qual exigiu o pagamento em grãos de trigo da seguinte maneira: os grão de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira peça do tabuleiro tivesse um grão, e as casas seguintes o dobro da anterior. Construa um algoritmo que calcule quantos grãos de trigo a rainha deverá pagarao monge. Um tabuleiro tem 64 casas.

"""
graos = 1
soma = 0

for x in range(0, 64):
    soma += graos
    graos *= 2
    print(f"Resultado: {soma}.")
"""

# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:

# Média do salário da população;

# Média do número de filhos;

# Maior salário;

# Percentual de pssoas com salário até R$100,00

# O final da leitura de dados se dará com a entrada de um salário negativo.

quantidadeGente = 0
somaSalarios = 0
somaFilhos = 0
maior = 0
quantidadeSalarios100 = 0

while True:
    salario = float(input("Digite um salário: "))
    if salario < 0:
        break
    filhos = int(input("Quantos filhos você tem: "))
    quantidadeGente += 1
    somaSalarios = salario
    somaFilhos += filhos

    if salario > maior:
        maior = salario
    if salario <= 100:
        quantidadeSalarios100 = +1

print(f"A soma dos salários é de {somaSalarios / quantidadeGente}")
print(f"A média de filhos é de {somaFilhos / quantidadeGente}")
print(f"O maior salário é de R${maior}")
print(
    f"Percentual de pessoas com salário até R$100 {quantidadeSalarios100 * 100 / quantidadeGente}"
)
