def impar(n):
    return n % 2 == 1


def soma_impares(x, y):
    if x > y:
        t = x
        x = y
        y = t

    i = x + 1
    soma = 0
    while i < y:
        if impar(i):
            soma += i
        i += 1
    return soma


x = int(input())
y = int(input())

print(soma_impares(x, y))
