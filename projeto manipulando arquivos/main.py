from time import sleep
from tela import *
from arquivo import *

arq = "arquivo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    layout_tela("Menu Principal")
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        layout_tela("Pessoas cadastradas")
        lerArquivo(arq)
    elif resposta == 2:
        layout_tela("Cadastro de nova pessoa")
        nome = str(input("Digite o nome: ")).capitalize().strip()
        idade = str(leiaInt(f"Digite a idade de {nome}: "))
        cadastroArquivo(arq, nome, idade)
    elif resposta == 3:
        layout_tela("Finalizando...")
        break
    else:
        print("ERRO: Digite uma opção válida.")
print("Volte sempre!")