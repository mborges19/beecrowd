def primo(n):
    qtd = 0
    divisor = 1
    while divisor <= x:
        if x % divisor == 0:
            qtd += 1
        divisor += 1
    return qtd == 2


n = int(input())
cont = 0

while cont < n:
    x = int(input())
    print(x, 'eh primo' if primo(x) else 'nao eh primo')
    # if primo(x):
    #     print(f'{x} eh primo')
    # else:
    #     print(f'{x} nao eh primo')
    cont += 1