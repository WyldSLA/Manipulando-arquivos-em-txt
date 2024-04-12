nome = str(input("Digite o seu nome completo: ")).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

print("Nome com todas as letras maiúsculas: {}".format(nome_maiusculo))
print("Nome com todas as letras minúsculas: {}".format(nome_minusculo))

contadorletras = len(nome) - nome.count(" ")

print("Qntd de letras no nome: {}".format(contadorletras))

div = nome.split()
letra_primeiro = len(div[0])

print("Qnt de letras do primeiro nome: {}".format(letra_primeiro))


print("O nome tem Silva? {}".format("SILVA" in nome_maiusculo))
começo = nome_maiusculo.startswith("SANTO")
print("O primeiro nome começa com Santo? {}".format(começo))

primeiro_nome = div[0]
ultimo_nome = div[len(div) - 1]

print("Primeiro nome: {}".format(primeiro_nome))
print("Último nome: {}".format(ultimo_nome))

letraA = nome_maiusculo.count("A")

 

