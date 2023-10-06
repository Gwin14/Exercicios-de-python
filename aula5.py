# 1 --------------------------------------
"""
temperatura = float(
    input("Diga a temperatura em graus Celcius para converter em Firenheit: ")
)

print(f"A temperatura é de {temperatura * 1.8 + 32} graus Farenheit")
"""
# 2 --------------------------------------
"""
moedaUmCentavo = int(input("Diga a quantidade de moedas de um centavo: ")) / 100
moedaCincoCentavos = (
    int(input("Diga a quantidade de moedas de cinco centavos: ")) / 100 * 5
)
moedaDezCentavos = (
    int(input("Diga a quantidade de moedas de dez centavos: ")) / 100 * 10
)
moedaVinteECincoCentavos = (
    int(input("Diga a quantidade de moedas de vinte e cinco centavos: ")) / 100 * 25
)
moedaCinquentaCentavos = (
    int(input("Diga a quantidade de moedas de cinquenta centavos: ")) / 100 * 50
)
moedaUmReal = int(input("Diga a quantidade de moedas de um real: "))

total = (
    moedaUmCentavo
    + moedaCincoCentavos
    + moedaDezCentavos
    + moedaVinteECincoCentavos
    + moedaCinquentaCentavos
    + moedaUmReal
)

print(f"A quatidade de dinheiro arrecadado é de R${total}.")
"""
# 3 --------------------------------------
"""
salario = float(input("Diga o seu salário: "))
vendas = float(input("Diga o valor em vendas: "))

print(f"A comissão é de R${vendas / 100 * 4}")
print(f"O total a receber é R${salario + (vendas / 100 * 4)}")
"""
# 4 --------------------------------------
"""
peso = float(input("Diga o seu peso em quilos: "))

print(f"O novo peso aumentado é de {peso + (peso / 100 * 15)}Kg.")
print(f"O novo peso diminuído  é de {peso - (peso / 100 * 20)}Kg.")
"""
# 5 --------------------------------------
"""
salarioMinimo = float(input("Diga o valor do salário mínimo: "))
salarioFuncionario = float(input("Diga o valor do salário de um funcionário: "))

quantidadeSalarios = salarioMinimo / salarioFuncionario

print(f"O funcionário ganha {quantidadeSalarios} salários mínimos.")
"""
# 6 --------------------------------------
"""
numero = float(input("Diga um número a ser multiplicado de 1 até 10: "))

print(f"{numero} x 1 = {numero * 1}.")
print(f"{numero} x 2 = {numero * 2}.")
print(f"{numero} x 3 = {numero * 3}.")
print(f"{numero} x 4 = {numero * 4}.")
print(f"{numero} x 5 = {numero * 5}.")
print(f"{numero} x 6 = {numero * 6}.")
print(f"{numero} x 7 = {numero * 7}.")
print(f"{numero} x 8 = {numero * 8}.")
print(f"{numero} x 9 = {numero * 9}.")
print(f"{numero} x 10 = {numero * 10.}")
"""
# 7 --------------------------------------
"""
anoPessoa = int(input("Diga o seu ano de nascimento: "))
anoAtual = int(input("Diga o ano atual: "))

print(
    f"Você tem {anoAtual - anoPessoa} anos de vida, {(anoAtual - anoPessoa) * 12} meses de vida e {(anoAtual - anoPessoa) * 365} dias de vida."
)
"""
