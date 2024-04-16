def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO ao criar o arquivo.")
    else:
        print(f"O arquivo {nome} foi criado.")

def lerArquivo(nome):
    try:
        a = open(nome, "rt", encoding="utf-8")
    except:
        print("ERRO ao ler o arquivo.")
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastroArquivo(arq, nome="<desconhecido>", idade=0):
    try:
        a = open(arq, "a+", encoding="utf-8")
    except:
        print("Erro no cadastro.")
    else:
        try:
            a.write(f"\n{nome};{idade}")
        except:
            print("Erro na hora do cadastro dos dados.")
        else:
            print(f"O registro de {nome} foi adicionado.")
            a.close()