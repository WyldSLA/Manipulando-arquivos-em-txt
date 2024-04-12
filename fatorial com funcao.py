def fatorial(num, sit = False):
    """
    -> Calcula o fatorial de um número.
    :para num: O número que será calculado.
    :para sit: (OPCIONAL) Mostrar ou não a conta.
    :return: Retorna o valor fatorial de um número "num".
    """
    f = 1
    for n in range(num, 0, -1):
        f*= n
        if sit:
            if not(n == 1):
                print(f"{n}", end=" x ")
            if n == 1:
                print(f"{n}", end=" = ")
    return f

f = fatorial(6, True)
print(f)