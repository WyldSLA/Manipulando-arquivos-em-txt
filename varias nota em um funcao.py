dic = dict()
def notas(*n, sit=False):
    dic["Total"] = len(n)
    dic["Maior"] = max(n)
    dic["Menor"] = min(n)
    dic["Média"] = sum(n) / len(n)
    if sit:
        if dic["Média"] > 7.5:
            dic["Situação"] = "Boa"
        elif 5.5 >= dic["Média"] < 7.5:
            dic["Situação"] = "Mediana"
        else:
            dic["Situação"] = "Péssima"
    return dic
resp = notas(4, 5, 6, 7, sit=True)
print(resp)