lista = []
pares = []
impares = []
def parouimpar(numeros):
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

def analisarResposta(resposta):
    while resposta != "S" and resposta != "N":
        print("Erro!")
        resposta = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    analisarResposta(resp)
    if resp == "N":
        break

print(f"A lista dos números: {lista}")

parouimpar(lista)

print(f"Lista dos números pares: {pares}")
print(f"Lista dos números ímpares: {impares}")