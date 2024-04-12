import random
print("-=" * 20)
print("Jogo Par ou Ímpar!")
print("-=" * 20)
par_e_impar = ""
contvitorias = 0
while True:
    usuario_valor = int(input("Digite um valor: "))
    usuario_ParImpar = str(input("Par ou Impar? [P]/[I] ")).upper().strip()[0]
    #Erro quando não digita P ou I
    while usuario_ParImpar != "P" and usuario_ParImpar != "I":
        print("Erro!")
        usuario_ParImpar = str(input("Par ou Impar? [P]/[I] ")).upper().strip()[0]
    pc_valor = random.randint(0, 10)
    print("-=" * 20)
    #Analisar se é par ou ímpar
    soma = usuario_valor + pc_valor
    div = soma % 2
    if div == 0:
        par_e_impar = "PAR"
    else:
        par_e_impar = "ÍMPAR"
    print(f"O jogador escolheu {usuario_valor} e o computador {pc_valor}. Total de {soma}, Deu {par_e_impar}")
    print("-=" * 20)
    if par_e_impar == "PAR":
        if usuario_ParImpar == "P":
            print("Você ganhou!")
            print("Vamos jogar novamente...")
            print("-=" * 20)
            contvitorias+=1
        else:
            print("Você perdeu!")
            break
    elif par_e_impar == "ÍMPAR":
        if usuario_ParImpar == "I":
            print("Você ganhou!")
            print("Vamos jogar novamente...")
            print("-=" * 20)
            contvitorias+=1
        else:
            print("Você perdeu!")
            break
print(f"GAME OVER! Você venceu {contvitorias} veze(s).")


    

    
    