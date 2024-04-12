frase = str(input("Digite uma frase: ")).upper().strip().split()
junto = "".join(frase)
inverso = ""
for letra in range(len(junto) -1, -1, -1 ):
    inverso+= junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if junto == inverso:
    print("Esta frase é um palíndromo!")
else:
    print("Esta frase não é um palíndromo!")
