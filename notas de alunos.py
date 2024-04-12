alunos_e_notas = []
cadastro = []

while True:
    nome = str(input("Nome do aluno: ")).strip().capitalize()
    cadastro.append(nome)
    nota1 = float(input("Nota 1: "))
    cadastro.append(nota1)
    nota2 = float(input("Nota 2: "))
    cadastro.append(nota2)
    media = (nota1 + nota2) / 2
    cadastro.append(media)
    alunos_e_notas.append(cadastro[:])
    cadastro.clear()
    resp = str(input("Mais uma vez?[S]/[N]")).upper().strip()[0]
    while resp != "S" and resp != "N":
        print("Erro! Digite somente Sim ou Não.")
        resp = str(input("Mais uma vez?[S]/[N]")).upper().strip()[0]
    if resp == "N":
        break
print("-=" * 20)

print("No. Nome    Média")
print("-"*20)
for pos, aluno_e_media in enumerate(alunos_e_notas):
    print("{:<3} {:<8} {}".format(pos, aluno_e_media[0], aluno_e_media[3]))
print("-"*20)


while True:
    op = int(input("Mostrar notas de qual aluno? (999 para encerrar) "))
    for pos, notas_aluno in enumerate(alunos_e_notas):
        if op == pos:
            print(f"Notas de {notas_aluno[0]} foram {notas_aluno[1], notas_aluno[2]}")
            print("-"*20)
    if op == 999:
        print("Finalizando...")
        break
print("Volte sempre!")
