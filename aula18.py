from classes_aula18 import Animal, Carro, Calculadora

"""
Exercício:
Objetivo:

Crie uma classe chamada Animal em um arquivo chamado classes_aulas.py.
Adicione os seguintes atributos à classe:
    nome (uma string que representa o nome do animal)
    idade (um inteiro que representa a idade do animal)
    som (uma string que representa o som que o animal faz)
Crie um método fazer_som que imprime o som do animal.
Crie um método info que imprime as informações do animal (nome e idade).
Crie pelo menos duas instâncias da classe Animal e teste os métodos criados nesse arquivo aula18.py.
"""

print("")

gato = Animal("Frederico", 9, "Miau")
cachorro = Animal("Jhonson", 10, "Auau")

gato.info()
gato.fazer_som()

cachorro.info()
cachorro.fazer_som()

print("--------------------------------------\n")


# --------------------------------------------

"""
Crie uma classe chamada carro.
Adicione os seguintes atributos à classe:
    marca (uma string que representa a marca do carro)
    modelo (uma string que representa o modelo do carro)
    ano (um inteiro que representa o ano de fabricação do carro)
    quilometragem (um float que representa a quilometragem do carro)
Crie um método info que imprime as informações do carro (marca, modelo, ano e quilometragem).
Crie um método dirigir que recebe a quantidade de quilômetros a ser percorrida e atualiza a quilometragem do carro.
Crie pelo menos duas instâncias da classe Carro e teste os modelos criados.
"""

McQueen = Carro("Ford", "Corrida", "1952", 9754)

McQueen.info()
McQueen.dirigir(87)

print("--------------------------------------\n")

"""
Exercício 3:
Objetivo: criar uma classe para representar uma calculadora.

Crie uma classe chamada calculadora.
Adicione os seguintes métodos à classe:
    soma que recebe dois números e retorna a soma deles.
    subtracao que recebe dois números e retorna a subtração do segundo do primeiro.
    multiplicacao que recebe dois números e retorna o resultado da multiplicação
    divisao que recebe dois números e retorna o resultado da divisão.
Instancie essa classe e utilize seus métodos.
"""
numero1 = 7
numero2 = 8

print(f"Números: {numero1} e {numero2}.\n\n")

print(
    f"Operação de soma:\n{numero1} + {numero2} = {Calculadora.soma(numero1, numero2)}.\n\n"
)

print(
    f"Operação de subtração:\n{numero1} - {numero2} = {Calculadora.subtracao(numero1, numero2)}.\n\n"
)

print(
    f"Operação de multiplicação:\n{numero1} * {numero2} = {Calculadora.multiplicacao(numero1, numero2)}.\n\n"
)

print(
    f"Operação de divisão:\n{numero1} / {numero2} = {Calculadora.divisao(numero1, numero2)}.\n"
)
