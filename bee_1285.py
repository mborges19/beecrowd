n = int(input())

while n >= 10:
    dmd = n % 10
    n = n // 10
    copia = n
    
    while n > 0:
        dmd2 = n % 10
        if dmd2 == dmd:
            print('Tem dígitos repetidos')
            break
        n = n // 10
    n = copia
