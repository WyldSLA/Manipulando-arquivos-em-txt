matriz = [[0, 0 , 0], [0, 0 , 0], [0, 0, 0]]
somapar = somaterceira =0

for l in range(0,3 ): #Linhas
    for c in range(0,3): #Colunas
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-="*20)
for l in range(0,3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end=" ")
        if matriz[l][c] % 2 == 0:
            somapar+= matriz[l][c]
        if c == 2:
            somaterceira+= matriz[l][2]

    print()
print("-="*20)
print(f"A soma dos valores pares é igual a {somapar}.")
print(f"A soma da terceira coluna é igual a {somaterceira}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}.")


# L0 - C0, C1, C2
# L1 - C0, C1, C2
# L2 - C0, C1, C2

