divida = int(input())
parcela = int(input())

menos = divida
qtd = 0

for i in range(divida, 0, -parcela):
    qtd += 1
    print(f'pagamento: {qtd}')
    print(f'antes = {i}')
    menos -= parcela
    if menos < 0:
        print('depois = 0')
    else:
        print(f'depois = {menos}')
    print('-----')