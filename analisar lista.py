lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Erro!")
        resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Você digitou {len(lista)} elementos.")
print(f"Lista em ordem decrescente: {sorted(lista, reverse=True)}")
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")