class Pessoa:
    nome = None
    idade = None
    telefone = None

    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def seApresentar(self):
        print(f"Meu nome é {self.nome}")

    def fazerAniversario(self):
        print(f"Você agora tem {self.idade + 1}")
