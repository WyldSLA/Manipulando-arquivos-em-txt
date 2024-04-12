dados_jogador = {}

dados_jogador["Nome"] = str(input("Nome do jogador: ")).capitalize()
partidas = int(input(f"Quantas partidas {dados_jogador['Nome']} jogou? "))
gols = []
for c in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
print("-="* 30)
dados_jogador["Gols"] = gols
dados_jogador["Total"] = sum(gols)
print(dados_jogador)
print("-="*30)
for k, v in dados_jogador.items():
    print(f"{k}: {v}")
print("-="*30)
print(f"O jogador {dados_jogador['Nome']} jogou {partidas} partidas.")
for pos, g in enumerate(gols):
    print(f"    => Na partida {pos + 1}, fez {g} gols.")
print(f"Foi um total de {dados_jogador['Total']} gols.")
