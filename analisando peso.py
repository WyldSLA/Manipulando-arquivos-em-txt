pessoas = []
pes = []
maior = menor = 0
while True:
    pes.append(str(input("Nome: ")))
    pes.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = pes[1]
    else:
        if pes[1] > maior:
            maior = pes[1]
        if pes[1] < menor:
            menor = pes[1]
    pessoas.append(pes[:])
    pes.clear()
    resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Erro!")
        resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    if resp == "N":
        break

print("-="*20)
print(f"Ao todo, foram cadastrados {len(pessoas)} pessoas.")
print(f"O maior peso foi {maior}Kg. Peso de ", end="")
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end=" ")
print(f"\nO menor peso foi {menor}Kg. Peso de ",end="")
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end=" ")


