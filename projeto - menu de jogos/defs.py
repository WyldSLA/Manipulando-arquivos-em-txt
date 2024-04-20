from random import randint
from time import sleep
def linha(tm=21):
    return "-="*tm

def layout_menu(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def layout_opcoes(ops, num=1):
    for n, i in enumerate(ops):
        print(f"{n+num} - {i}")
    print(linha())

def escolherOpcao():
    while True:
        try:
            opc = int(input("Sua Opção: "))
        except(TypeError, ValueError):
            print("ERRO: Digite um valor válido.")
        except(KeyboardInterrupt):
            print("\nERRO: O usuário preferiu não digitar")
            return ""
        else:
            return opc

def jogoAdivinhacao():
    layout_menu("Jogo da Adivinhação")
    numero_sorteado = randint(1, 100)
    contJogadas = 0
    while True:
        try:
            numero_jogador = int(input("Digite seu chute: "))
            while 0 < numero_jogador > 100:
                print("ERRO: Digite somente valores entre 0 e 100.")
                numero_jogador = int(input("Digite seu chute: "))
        except(TypeError, ValueError):
            print("ERRO: Digite um valor válido.")
        except(KeyboardInterrupt):
            print("\nERRO: O usuário preferiu não digitar")
            break
        else:
            contJogadas+=1
            if numero_jogador == numero_sorteado:
                sleep(0.3)
                print(linha())
                print("Parabéns, você acertou o número sorteado! :D")
                print(f"Você chutou {contJogadas} veze(s).")
                resp = analiseResposta()
                print(linha())
                if resp == False:
                    print("Finalizando", end="")
                    for ponto in "....":
                        print(ponto, end="", flush=True)
                        sleep(0.5)
                    print()
                    break
                else:
                    numero_sorteado = randint(1, 100)
                    contJogadas = 0
            else:
                    if numero_jogador > numero_sorteado:
                        sleep(0.3)
                        print(f"Tente um número menor que {numero_jogador}.")
                    elif numero_jogador < numero_sorteado:
                        sleep(0.3)
                        print(f"Tente um número maior que {numero_jogador}.")
        
def jogoParOuImpar():
    layout_menu("Par ou Ímpar")
    somaValores = contVitoria =0
    resultado = ""
    while True:
        try:
            pc_valor = randint(0, 10)
            usuario_valor = int(input("Digite um valor: "))
            usuario_jogada = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
            while usuario_jogada != "P" and usuario_jogada != "I":
                print("ERRO: Valor inválido.")
                usuario_jogada = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
        except(TypeError, ValueError):
            print("ERRO: Digite um valor válido.")
        except(KeyboardInterrupt):
            print("\nERRO: O usuário preferiu não digitar")
            break
        else:
            somaValores = usuario_valor + pc_valor
            if somaValores % 2 == 0:
                resultado = "PAR"
            else:
                resultado = "ÍMPAR"
            print(linha())
            print(f"O jogador escolheu {usuario_valor} e o computador escolheu {pc_valor}. ")
            print(f"O resultado foi {somaValores}. Deu {resultado}")
            print(linha())
            if resultado == "PAR":
                if usuario_jogada == "P":
                    print("Você ganhou!")
                    print(linha())
                    contVitoria+= 1
                else:
                    print("Você perdeu!")
            elif resultado == "ÍMPAR":
                if usuario_jogada == "I":
                    print("Você ganhou!")
                    print(linha())
                    contVitoria+= 1
                else:
                    print("Você perdeu!")
            resp = analiseResposta()
            print(linha())
            if resp == False:
                print(f"GAME OVER! Você venceu {contVitoria} vez(es)")
                print(linha())
                print("Finalizando", end="")
                for ponto in "....":
                    print(ponto, end="", flush=True)
                    sleep(0.5)
                print()
                break

def JogoJokenpo():
    layout_menu("Pedra, Papel & Tesoura")
    jogadas = ["Pedra", "Papel", "Tesoura"]
    contJog = contPC = 0
    while True:
        try:
            layout_opcoes(jogadas, num=0)
            jogador = int(input("Escolha sua jogada: "))
            pc = randint(0, 2)
            while 0 < jogador > 2:
                print("ERRO: Digite entre 0 e 2.")
                jogador = int(input("Escolha sua jogada: "))
        except(TypeError, ValueError):
            print("ERRO: Digite um valor válido.")
        except(KeyboardInterrupt):
            print("\nERRO: O usuário preferiu não digitar")
            break
        else:
            print(linha())
            print("JO!")
            sleep(0.8)
            print("KEN!")
            sleep(0.8)
            print("PO!")
            sleep(0.8)
            print(f"Você escolheu {jogadas[jogador]}")
            print(f"O computador escolheu {jogadas[pc]}")
            print(linha())
            if jogador == 0:
                if pc == 1:
                    print("O computador ganhou!")
                    contPC += 1
                    print(linha())
                elif pc == 2:
                    print("Você ganhou!")
                    contJog+= 1
                    print(linha())
            elif jogador == 1:
                if pc == 0:
                    print("Você ganhou!")
                    contJog+= 1
                    print(linha())
                elif pc == 2:
                    print("O computador ganhou!")
                    contPC+=1
                    print(linha())
            elif jogador == 2:
                if pc == 0:
                    print("O computador ganhou!")
                    contPC+=1
                    print(linha())
                elif pc == 1:
                    print("Você ganhou!")
                    contJog+=1
                    print(linha())
            if jogador == pc:
                print("Empate!")
                print(linha())
            resp = analiseResposta()
            print(linha())
            if resp == False:
                print("Placar Final!!")
                print(f"Você ganhou {contJog} veze(s).")
                print(f"O computador ganhou {contPC} veze(s).")
                print(linha())
                print("Finalizando", end="")
                for ponto in "....":
                    print(ponto, end="", flush=True)
                    sleep(0.5)
                print()
                break

def analiseResposta():
    while True:
        try:
            per = str(input("Deseja jogar mais uma vez? ")).strip().upper()[0]
            while per != "S" and per != "N":
                print("ERRO: Digite somente Sim ou Não.")
                per = str(input("Jogar mais uma vez?")).strip().upper()[0]
        except(TypeError, ValueError, IndexError):
            print("ERRO: Digite um valor válido.")
        except(KeyboardInterrupt):
            print("\nERRO: O usuário preferiu não digitar")
            break
        else:
            if per == "S":
                return True
            if per == "N":
                return False