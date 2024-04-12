def tela():
    print("-"*20)
    print("Terrenos Fodas!")
    print("-"*20)

def areaTerreno(comprimento, largura):
    area = comprimento * largura
    print(f"Seu terreno de {comprimento}x{largura} M mede {area} M².")

tela()
comprimento = int(input("Comprimento do Terreno: "))
largura = int(input("Largura do Terreno: "))
areaTerreno(comprimento, largura)