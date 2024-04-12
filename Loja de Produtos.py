print("{:=^40}".format("Loja"))
valor = float(input("Digite o valor da compra R$"))
print("FORMAS DE PAGAMENTO")
print("[1] à vista em dinheiro/cheque.")
print("[2] à vista cartão.")
print("[3] 2x no cartão.")
print("[4] 3x ou mais no cartão.")
opcao = int(input("Qual a sua opção? "))
while opcao > 4 or opcao < 1:
    print("ERRO!")
    opcao = int(input("Qual a sua opção? "))
if opcao == 1:
    valorfinal = valor - (valor * 0.10) 
    print("Valor final com à vista em dinheiro/cheque desconto de 10%: R${}".format(valorfinal))
elif opcao == 2:
    valorfinal = valor - (valor * 0.05)
    print("Valor final à vista no cartão com desconto de 5%: R${}".format(valorfinal))
elif opcao == 3:
    valorparcelado = valor / 2
    print("Preço em 2x parcelas: R${}".format(valorparcelado))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    valorfinal = (valor + (valor * 0.20)) 
    valorparcelado = valorfinal / parcelas
    print("Preço dividido em {}x com preço de R${}".format(parcelas, valorparcelado))
    print("Preço Total com JUROS: R${}".format(valorfinal))