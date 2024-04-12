opcao = 0
import time
primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))
print("-=" * 15)
while opcao != 5:
    time.sleep(0.6)
    print("[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do Menu")
    opcao = int(input("Opção: "))
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print("A soma entre {} + {} = {}".format(primeiro_valor, segundo_valor, soma))
    elif opcao == 2:
        mult = primeiro_valor * segundo_valor
        print("O produto entre {} x {} = {}".format(primeiro_valor, segundo_valor, mult))
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print("Entre {} e {} o maior é {}".format(primeiro_valor, segundo_valor, primeiro_valor))
        else:
            print("Entre {} e {} o maior é {}".format(primeiro_valor, segundo_valor, segundo_valor)) 
    elif opcao == 4:
        print("Informe os novos valores: ")
        primeiro_valor = int(input("Primeiro valor: "))
        segundo_valor = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção Invalida. Tente novamente!")
    print("-=" * 15)
time.sleep(0.6)
print("Fim do Programa! Volte sempre :D")

