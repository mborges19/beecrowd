ano_inicio = int(input())
ano_fim = int(input())
cont = 0
for i in range(ano_inicio, ano_fim+1):
    if i % 4 == 0 and not i % 100 == 0 or i % 400 == 0:
        cont += 1
        print(i)
print(f'bissextos: {cont}')