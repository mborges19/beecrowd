a = int(input())
b = int(input())

if (a > b):
    print('Nenhuma tabuada no intervalo!')
else:
    for intervalo in range(a, b + 1):
        for i in range(1, 11):
            print(f'{intervalo} x {i} = {intervalo * i}')
        print('----------')
