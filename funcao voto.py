from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade <= 65:
        sit = "Voto obrigatório"
    elif 16 <= idade < 18 or idade > 65:
        sit = "Voto Opcional"
    elif idade < 16:
        sit = "Voto Negado"
    return f"Com {idade} anos: {sit}"
        
ano_nascimento = int(input("Ano de nascimento: "))
sit = voto(ano_nascimento)
print(sit)