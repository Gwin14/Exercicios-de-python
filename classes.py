"""
class Produto:
    def __init__(self, descricao: str, valor: float) -> None:
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self) -> None:
        self.produtos = []

    def insetirProduto(self, produto: Produto):
        self.produtos.append(produto)


produto = Produto("Tenis, 500")
carrinho = Carrinho()
carrinho.insetirProduto(produto)
print(carrinho.produtos)
"""


"""

DANDO ERRO ------------

class Estudante:
    def __init__(self, nome: str, matricula: str, media_notas: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.media_notas = media_notas

    @property
    def nome(self) -> str:
        return self.nome

    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @property
    def matricula(self) -> str:
        return self.matricula

    @matricula.setter
    def matricula(self, valor):
        self.matricula = valor

    @property
    def media_notas(self) -> int:
        return self.media_notas

    @media_notas.setter
    def media_notas(self, valor):
        self.media_notas = valor


class Escola:
    def __init__(self) -> None:
        self.estudantes = []

    def adicionar_estudante(self, estudante: Estudante):
        try:
            self.estudantes.append(estudante)
        except:
            print("Passe um ESTUDANTE")

    def obter_media_notas(self):
        todas_medias = []

        for x in self.estudantes:
            todas_medias.append(x.media_notas)

        print(todas_medias)
"""


class Carro:
    def __init__(self, descricao: str, valor: int) -> None:
        self.descricao = descricao
        self.valor = valor


class Mecanica:
    def __init__(self) -> None:
        self.carros = []

    def adicionar_carro(self, carro: Carro):
        self.carros.append(carro)

    def obter_valores(self):
        contador = 0
        soma = 0
        for x in self.carros:
            contador += 1
            soma += x.valor

        print(soma / contador)
