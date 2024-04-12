aluno = {}

aluno["Nome"] = str(input("Nome do aluno: ")).capitalize().strip()
aluno["Media"] = float(input(f"Nota de {aluno['Nome']}: "))
if aluno["Media"] >= 7.0:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")