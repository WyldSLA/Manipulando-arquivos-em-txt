from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contador de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for n in range(inicio, fim + passo, passo):
            print(n, end=" ", flush=True)
            sleep(0.5)
        print("Fim!")
        print("-="*15)
    
    else:
        for n in range(inicio, fim - passo, -passo):
            print(n, end=" ", flush=True)
            sleep(0.5)
        print("Fim!")
        print("-="*15)

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora personalize! :D")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
print("-="*15)
contador(i, f, p)