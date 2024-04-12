exp = str(input("Digite a expressão: "))
cont_aberto = 0
cont_fechado = 0
for simb in exp:
    if simb == "(":
        cont_aberto += 1
    elif simb == ")":
        cont_fechado += 1
if cont_aberto == cont_fechado:
    print("Expressão válida.")
else:
    print("Expressão inválida.")