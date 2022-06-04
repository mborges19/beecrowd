inicio = int(input())
fim = int(input())

cont = 0

for i in range(inicio, fim+1):
    divisor = 1
    qtd = 0
    while divisor <= i:
        if i % divisor == 0:
            qtd += 1
        divisor += 1

    if qtd == 2:
        print(i)
        cont += 1
print(f'primos: {cont}')