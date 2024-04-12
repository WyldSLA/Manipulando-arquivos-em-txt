from time import sleep
def identificarMaior(* valores):
    print("Analisando os valores passado...")
    maior = 0
    for p, n in enumerate(valores):
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
        if p == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print(f"Foram analisados {len(valores)} númueros")
    print(f"O maior valor informado foi {maior}")
    print("-="*20)

identificarMaior(2, 4, 5, 9, 7, 1)
identificarMaior(1, 2)
identificarMaior()



