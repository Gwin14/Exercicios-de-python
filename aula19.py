"""
Exercício 1:
Objetivo: Criar classes que representam uma escola com estudantes.

Crie uma classe chamada Escola.
Adicione um atributo de classe chamado estudante que seja uma lista para armazenar instâncias de estudantes.
Crie uma classe de estudante como o nome e matrícula como atributo e media de notas.
Adicione um método de classe chamado adicionar_estudante que recebe uma instância de Estudante e a adiciona à lista de estudantes.
Adicione um método de classe chamado obter_media_notas que calcula e retorna a média das notas de todos os estudantes na escola.
Adapte o método adicionar_estudante para tratar exceções caso o objeto passado não seja uma instância de Estudante.
Crie os gets e sets para as classes.
"""

"""
from classes import Escola, Estudante

estudante1 = Estudante("fabio", "ciencias", 10)
estudante2 = Estudante("artur", "ads", 8)

senac = Escola()

senac.adicionar_estudante(estudante1)
senac.adicionar_estudante(estudante2)

senac.obter_media_notas()
"""

# -------------------------------------------------------

"""
Exercício 2: Criar classes de uma Mecânica

Crie uma classe chamada Mecânica.
Adicione um atributo de classe chamado Carro que seja uma lista para armazenar instâncias de carros.
Crie uma classe de Carro com atributos descrição e valor.
Adicione um método de classe chamado adicionar_carro que recebe uma instância de Carro e a adiciona à lista de carros.
Adicione um método de classe chamado obter_valores que calcula e retorna os valores dos serviços somados de todos os carros.
Crie os gets e os sets para as classes.
Teste os métodos usados com exemplos de instâncias de Estudante e Escola.
"""

from classes import Mecanica, Carro

mcQuenn = Carro("corrida", 8000)
mate = Carro("guincho", 4000)

mecanica = Mecanica()

mecanica.adicionar_carro(mcQuenn)
mecanica.adicionar_carro(mate)

mecanica.obter_valores()
