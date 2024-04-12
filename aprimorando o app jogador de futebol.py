jogador = dict()
gols = list()
jogadores = list()
while True:
    jogador["Nome"] = str(input("Nome do Jogador: ")).capitalize().strip()
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for c in range(0, partidas):
        gols.append(int(input(f"    Quantos gols na partida {c+1} ?")))
    jogador["Gols"] = gols[:]
    jogador["Total de Gols"] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    resp = str(input("Continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break
print("-="*30)
print("Cod Nome     Gols      TotGols")
for pos, j in enumerate(jogadores):
    print(f"{pos:<3} {j["Nome"]:<8} {j["Gols"]!s:<13s} {j["Total de Gols"]}")
print("-="*30)
while True:
    op = int(input("Qual jogador você quer mostrar? (999 para parar) "))
    print("-"*30)
    if op == 999:
        print("Finalizando...")
        break
    while op >= len(jogadores):
        op = int(input("Qual jogador você quer mostrar? (999 para parar) "))
        print("-"*30)
    for pos, j in enumerate(jogadores):
        if op == pos:
            print(f"Levatamento do Jogador {j["Nome"]}.")
            for p, g in enumerate(j["Gols"]):
                print(f"    No jogo {p+1} fez {g} gol(s).")
            print("-"*30)
print("Volte sempre!")


    
