from defs import *
from time import sleep
while True:
    layout_menu("Menu de Jogos")
    layout_opcoes(["Adivinhação", "Par ou Impar", "Pedra, Papel e Tesoura", "Sair do menu"])
    resp = escolherOpcao()
    if resp == 1:
        sleep(0.3)
        jogoAdivinhacao()
    elif resp == 2:
        sleep(0.3)
        jogoParOuImpar()
    elif resp == 3:
        sleep(0.3)
        JogoJokenpo()
    elif resp == 4:
        sleep(0.3)
        print("Finalizando", end="")
        for ponto in "....":
            print(ponto, end="", flush=True)
            sleep(0.5)
        break
    else:
        print("Por favor, digite um valor válido.")
print("\nVolte sempre!")
