
while True:
    c = 1
    num = int(input("Qual valor você quer ver a tabuada? "))
    print("-"*20)
    if num < 0:
        print("PROGRAMA ENCERRADO!")
        break
    while c <= 10:
        res = num * c
        print(num, " x ", c, " = ", res)
        c+=1 
    print("-"*20)  
