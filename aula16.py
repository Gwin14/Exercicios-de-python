import json
from datetime import datetime

airbnb = json.load(open("airbnb.json", "r"))

# ------ Calcule e exiba a contagem total por bairro

"""
bairros = {}

for x in airbnb:
    b = x["bairro"]
    if b in bairros.keys():
        bairros[b] += 1
    else:
        bairros[b] = 1

print(bairros)
"""

# ------ Encontre e exiba o preço mais baixo

"""
maiorPreco = 9999999
nome = ""

for x in airbnb:
    if float(x["preco"]) < maiorPreco:
        maiorPreco = float(x["preco"])
        nome = x["nome_hotel"]

print(nome)
print(maiorPreco)
"""

# ------ Calcule e exiba a média de avaliações por mês

"""
media = 0
divisor = 0

for x in airbnb:
    if x["avaliacaoes_por_mes"] == "":
        continue

    media += float(x["avaliacaoes_por_mes"])
    divisor += 1

print(media / divisor)
"""

# ------ Calcule e exiba a contagem total de tipos de quartos

"""
tiposQuartos = {}

for x in airbnb:
    quarto = x["tipo_quarto"]

    if quarto in tiposQuartos:
        tiposQuartos[quarto] += 1
    else:
        tiposQuartos[quarto] = 1

print(tiposQuartos)
"""

# ------ Encontre e exiba o bairro com a maior quantidade de hospedagem

"""
maiorHospedagem = 0
nome = ""

for x in airbnb:
    if float(x["numero_de_avaliacoes"]) > maiorHospedagem:
        maiorHospedagem = float(x["numero_de_avaliacoes"])
        nome = x["nome_hotel"]

print(nome)
print(maiorHospedagem)
"""

# ------ Identifique e exiba o nome do anfitrião que possui a listagem mais recente

# ------ Encontre e exiba o nome do hóspede que possui o maior número de hospedagem

# ------ Encontre e exiba a latitude e longitude da listagem mais cara

"""
preco = 0
nomeHotel = ""
longitude = ""
latitude = ""

for x in airbnb:
    if float(x["preco"]) > preco:
        preco = float(x["preco"])
        longitude = x["longitude"]
        latitude = x["latitude"]
        nomeHotel = x["nome_hotel"]

print(nomeHotel)
print(preco)
print(longitude)
print(latitude)
"""

# ------ Calcule e exiba a média de disponibilidade anual por tipo de quarto

# ------ Calcule e exiba a média de preços por tipo de quarto
