lista_compra = ("Lápis", 1.75, "Borracha", 2.0, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("-"*20)
print("Listagem de Compras")
print("-"*20)

for item in range(0, len(lista_compra)):
    if type(lista_compra[item]) == str:
        print("{:.<30}".format(lista_compra[item]), end="R$")
    else:
        print(lista_compra[item])