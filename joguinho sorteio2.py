from random import randint
from time import sleep

def titulo(txt):
    tmnh = len(txt) + 4
    print("="*tmnh)
    print("  ", end="")
    for l in txt:
        print(f"{l}", end="", flush=True)
        sleep(0.2)
    print()
    print("="*tmnh)

def sorteioNumero():
    num_sorteado = randint(0, 100)
    return num_sorteado

def respUsuario():
    chute = input("Digite aqui o seu chute: ")
    while chute.isnumeric() == False:
        print("Digite apenas números.")
        chute = input("Digite aqui o seu chute: ")
    while 0 < int(chute) > 100:
        print("Apenas números entre 0 e 100.")
        chute = input("Digite aqui o seu chute: ")
    if chute.isnumeric():
        return int(chute)
    
def analiseJogo(numero_sorteado):
    cont = 0
    while True:
        chute_usuario = respUsuario()
        if chute_usuario == numero_sorteado:
            print("Parabéns, Você acertou!")
            print(f"Você chutou {cont} veze(s)")
            break
        else:
            if chute_usuario > numero_sorteado:
                print("Chute um número menor...")
            elif chute_usuario < numero_sorteado:
                print("Chute um número maior...")
        cont+=1


titulo("Jogo da Adivinhação!")
analiseJogo(numero_sorteado = sorteioNumero())