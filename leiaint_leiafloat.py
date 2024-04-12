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
    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(TypeError, ValueError):
            print("ERRO: Digite apenas um valor inteiro! ")
            continue
        except(KeyboardInterrupt):
            print("\nEntrada de dados interrompida pela usuário.")
            return 0
        else:
            return n

inteiro = leiaInt("Digite um valor Inteiro: ")
real = leiaFloat("Digite um valor Decimal: ")

print(f"Valor inteiro: {inteiro}\nValor Real: {real}")