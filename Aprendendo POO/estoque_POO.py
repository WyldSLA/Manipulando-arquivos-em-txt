class Produto:
    def __init__(self, nome_produto="<desconhecido>", preco=0, tot_estoque=0):
        self.nome_produto = str(nome_produto)
        self.preco = float(preco)
        self.tot_estoque = int(tot_estoque)
    
    def exibir_dados(self):
        print(f"Nome: {self.nome_produto}")
        print(f"Valor: R${self.preco}")
        print(f"Estoque: {self.tot_estoque}")
    
    def controle_estoque(self, novo_estoque=0):
        self.tot_estoque += novo_estoque
        print(f"Novo estoque: {self.tot_estoque}")
               
    def faturamento(self):
        return f"R${self.tot_estoque * self.preco}"

nome = str(input("Nome do Produto: ")).capitalize().strip()
preco = float(input("Preço: R$"))
estoque = int(input("Total no estoque: "))

p1 = Produto(nome, preco, estoque)
p1.controle_estoque()
print(p1.faturamento())

