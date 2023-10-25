# Criar um programa que pergunta pro usuário o nome de um livro, o autor e o ano de lancamento até o usuario não querer mais. Em um dicionário. No final dizer os livros.
dados = []
while True:
    escolha = input("Digite 1 para adicionar uma pessoa, 0 para sair: ")

    if escolha == "0":
        break

    if escolha == "1":
        quantidade = input("Quantos livros você deseja informar dessa pessoa: ")
        dados_livros = []

        for x in range(0, quantidade):
            nome_livro = input("Qual o nome do livro: ")
            ano_lancamento = int(input("Qual o ano de lançamento: "))
            autor = input("Qual o autor do livro: ")

        dados_livros.append(
            {
                "autor": autor,
                "nome": nome_livro,
                "ano": ano_lancamento,
            }
        )

        dados.append({"livros": dados_livros})

print(dados)
