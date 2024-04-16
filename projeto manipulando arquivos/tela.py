def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print("ERRO: Digite apenas um valor inteiro! ")
            continue
        except(KeyboardInterrupt):
            print("\nEntrada de dados interrompida pela usuário.")
            return 0
        else:
            return n

def linha(tm=42):
    return "-"*tm

def layout_tela(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    c = 0
    for item in lista:
        print(f"{c + 1} - {item}")
        c+=1
    linha()
    opc = leiaInt("Opção: ")
    return opc