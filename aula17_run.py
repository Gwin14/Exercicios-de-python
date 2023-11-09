import json
from titanic import Titanic

tit = json.load(open("titanic.json", "r"))


"""
pessoa1 = Pessoa("Fábio", 19, "49837564")

print(pessoa1.nome)

pessoa1.seApresentar()

pessoa1.fazerAniversario()
"""
"""
pessoas = []

for x in range(10):
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua nome? "))
    telefone = input("Qual seu telefone? ")
    pessoa2 = Pessoa(nome, idade, telefone)
    pessoas.append(pessoa2)

    print(pessoas)
"""

# Crie uma lista com varias instancias do arquivo titanic e botar numa lista

passageiros = []

for x in tit:
    passag = Titanic(
        x["PassengerId"],
        x["Survived"],
        x["Pclass"],
        x["Name"],
        x["Sex"],
        x["Age"],
        x["SibSp"],
        x["Parch"],
        x["Ticket"],
        x["Fare"],
        x["Cabin"],
        x["Embarked"],
    )

    passageiros.append(passag)

for x in passageiros:
    print(x.name)
