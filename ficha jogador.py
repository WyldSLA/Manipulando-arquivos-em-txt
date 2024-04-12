def ficha(nome="<desconhecido>", gols=0):
    return f"O jogador {nome.capitalize().strip()} fez {gols} gol(s) no campeonato."

n = str(input("Nome do jogador: "))
g = str(input("Gols marcados: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    resp = ficha(gols=g)
else:
    resp = ficha(n, g)
print(resp)


