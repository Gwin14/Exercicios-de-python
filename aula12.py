nome_lista = []

while True:
    nome = input(
        "Diga um nome para adicionar um nome à lista de nomes. Digite 0 para parar: "
    )
    if nome == "0":
        break
    else:
        nome_lista.append(nome)

print("A lista de nomes é:")

for x in nome_lista:
    print(x)
