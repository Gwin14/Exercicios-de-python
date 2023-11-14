class Animal:
    nome = None
    idade = None
    som = None

    def __init__(self, nome, idade, som):
        self.nome = nome
        self.idade = idade
        self.som = som

    def info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}.")

    def fazer_som(self):
        print(f"Som: {self.som}.\n")


class Carro:
    marca = None
    modelo = None
    ano = None
    quilometragem = None

    def __init__(self, marca, modelo, ano, quilometragem) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def info(self):
        print(
            f"Dados:\nMarca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Quilometragem: {self.quilometragem}"
        )

    def dirigir(self, quilometros):
        self.quilometragem += quilometros
        print(f"Quilometragem após andar {quilometros} metros: {self.quilometragem}\n")


class Calculadora:
    def soma(numero1, numero2):
        return numero1 + numero2

    def subtracao(numero1, numero2):
        return numero1 - numero2

    def multiplicacao(numero1, numero2):
        return numero1 * numero2

    def divisao(numero1, numero2):
        return numero1 / numero2
