# Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte com o peso do prato
"""
pesoPrato = float(input("Diga o peso total do seu prato"))
valorQuilo = 12.00

print(
    f"Se o seu prato pesa {pesoPrato} Quilos. O valor total a pagar é {pesoPrato * valorQuilo}"
)
"""
# -------------------------------------------------------------

# Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%
"""
precoProduto = float(input("Diga o preço do produto"))
desconto = (precoProduto / 100) * 10

print(f"O valor final do produto com desconto é R${precoProduto - desconto}")
"""
# --------------------------------------------------------------

# A padaria hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$12,00 e a broa custa R$1,50. Ao final do dia, o dono quer saber o quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nesses fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.
"""
pao = 12.00
broa = 1.50

quantidadePaes = int(input("Diga a quantidade de pães vendidos: "))
quantidadeBroas = int(input("Diga a quantidade de broas vendidas: "))

total = (pao * quantidadePaes) + (broa * quantidadeBroas)

print(f"O total arrecadado é R${total}.")
print(f"E a poupança a ser guardada é R${(total / 100) * 10}.")
"""

# -----------------------------------------------------------------

# Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com aumento e o salário final.

"""
salarioInicial = float(input("Diga o seu salário: "))
salarioAumento = salarioInicial + (salarioInicial / 100 * 15)
salarioDesconto = salarioAumento - (salarioAumento / 100 * 8)

print(
    f"O seu salário normal é de R${salarioInicial}, o com aumento é R${salarioAumento} e com impostos é R${salarioDesconto}."
)
"""
