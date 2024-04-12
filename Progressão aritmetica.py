c = 0
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
total = 0
n = 10
while n != 0:
    total = total + n
    while c <= total:
        print("{}-> ".format(termo), end="")
        termo+= razao 
        c+=1
    print("Pausa")
    n = int(input("Quantos termos você quer mostrar mais? "))

    

    