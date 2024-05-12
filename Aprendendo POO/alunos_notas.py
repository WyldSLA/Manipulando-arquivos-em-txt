class Aluno:
    def __init__(self, nome="<desconhecido>", idade=0, nota1=0, nota2=0, nota3=0,nota4=0):
        self.nome = nome
        self.idade = idade
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.nota4 = float(nota4)
    
    def media(self):
        self.med = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        print(f"A média do aluno {self.nome} ficou {self.med:.2f}")
    
    def situacao(self):
        if self.med > 7.0:
            return "Aprovado"
        elif self.med > 5.0:
            return "Recuperação"
        else:
            return "Reprovado"
    
aluno1 = Aluno("Matheus", 15, 3, 4, 9, 6)
aluno1.media()
sit = aluno1.situacao()
print(sit)