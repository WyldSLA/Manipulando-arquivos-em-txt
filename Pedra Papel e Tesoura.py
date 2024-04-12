from random import randint
from time import sleep

jogadas = ["Pedra", "Papel", "Tesoura"]
print("-="*20)
print("Pedra, Papel & Tesoura!!")
print("-="*20)
contPC = 0
contJog = 0
while True:
    pc = randint(0,2)
    print("[0] Pedra [1] Papel [2] Tesoura")
    usuario_jogada = int(input("Digite sua jogada: "))
    while usuario_jogada < 0 or usuario_jogada > 2:
        print("Erro! Digite entre 0 e 2!")
        usuario_jogada = int(input("Digite seu jogada: "))
    print("JO")
    sleep(0.8)
    print("KEN")
    sleep(0.8)
    print("PO!!!")

    print("-="* 20)
    print(f"Você jogou {jogadas[usuario_jogada]}.")
    print(f"O computador jogou {jogadas[pc]}.")
    print("-="*20)

    if usuario_jogada == 0:
        if pc == 1:
            print("O computador ganhou!")
            contPC += 1
            print("-="*20)
        elif pc == 2:
            print("Você ganhou!")
            contJog+= 1
            print("-="*20)
    elif usuario_jogada == 1:
        if pc == 0:
            print("Você ganhou!")
            contJog+= 1
            print("-="*20)
        elif pc == 2:
            print("O computador ganhou!")
            contPC+=1
            print("-="*20)
    elif usuario_jogada == 2:
        if pc == 0:
            print("O computador ganhou!")
            contPC+=1
            print("-="*20)
        elif pc == 1:
            print("Você ganhou!")
            contJog+=1
            print("-="*20)
    if usuario_jogada == pc:
        print("Empate!")
        print("-="*20)

    resp = str(input("Mais uma vez?[S]/[N]")).upper().strip()[0]
    while resp != "S" and resp != "N":
        print("Erro! Digite somente Sim ou Não.")
        resp = str(input("Mais uma vez?[S]/[N]")).upper().strip()[0]
    if resp == "N":
        break

print("-="*20)
print("Placar Final!!")
print(f"Você ganhou {contJog} veze(s).")
print(f"O computador ganhou {contPC} veze(s).")