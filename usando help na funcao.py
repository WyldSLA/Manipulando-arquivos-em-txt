def ajuda(op):
    help(op)

def titulo(txt):
    tmnh = len(txt) + 4
    print("~"*tmnh)
    print(f"  {txt}")
    print("~"*tmnh)

titulo("Sistema de Ajuda PyHelp")
while True:
    op = str(input("Função ou Bilioteca >> "))
    if op.upper() == "FIM":
        break
    titulo(f"Acessando o manual de comando '{op}'")
    ajuda(op)
print("Até logo!")
        

