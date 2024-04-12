print("="*20)
print("Banco!")
print("="*20)
# O Valor for maior q tal nota, ele vai subtrair com essa nota e vai contar quantas vezes ele fez isso!
saque = int(input("Valor do Saque: R$"))
totced = 0
ced = 50
while True:
    if saque >= ced:
        saque -= ced
        totced+=1
    else:
        if totced > 0:
            print(f" O Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            break


