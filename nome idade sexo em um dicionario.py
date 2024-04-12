pessoas = list()
cadastro = dict()
somaIdade = 0 
while True:
    cadastro["Nome"] = str(input("Nome: ")).capitalize().strip()
    cadastro["Sexo"] = str(input("Sexo: [M/F] ")).upper().strip()[0]
    while cadastro["Sexo"] != "F" and cadastro["Sexo"] != "M":
        print("Erro.")
        cadastro["Sexo"] = str(input("Sexo: [M/F] ")).upper().strip()[0]
    cadastro["Idade"] = int(input("Idade: "))
    somaIdade+= cadastro["Idade"]
    pessoas.append(cadastro.copy())
    resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    while resp != "S" and resp != "N":
        resp = str(input("Continuar?[S]/[N] ")).strip().upper()[0]
    if resp == "N":
        break
print("-="*30)
media = somaIdade / len(pessoas)
print(f"- Total de pessoas cadastradas: {len(pessoas)}")
print(f"- Média das idades: {media:.1f}")
print(f"- Mulheres cadastradas foram: ", end="")
for p in pessoas:
    if p["Sexo"] == "F":     
        print(f"[{p["Nome"]}]", end=" ")
print()
print("- Lista de pessoas com idade acima da média:")
for p in pessoas:
    if p["Idade"] > media:
        print(f"Nome: {p["Nome"]}; Sexo: {p["Sexo"]}; Idade: {p["Idade"]}.")



