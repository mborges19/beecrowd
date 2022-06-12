n = int(input())

def obter_notas():
  notas = []

  for _ in range(n):
    notas.append(float(input()))

  return notas

def obter_notas_finais(notas_originais, novas_notas):
  qtd_notas_alteradas = 0

  for i in range(len(notas_originais)):
    if (novas_notas[i] == 10 and notas_originais[i] < 10):
      novas_notas[i] = min(notas_originais[i] + 2, 10)
      qtd_notas_alteradas += 1
    else:
      novas_notas[i] = notas_originais[i]

  return qtd_notas_alteradas

def exibir_notas_alteradas(notas_originais, notas_finais, qtd_notas_alteradas):
  print(f'NOTAS ALTERADAS: {qtd_notas_alteradas}')
  for i in range(n):
    nota_alterada = ('*' if notas_originais[i] != notas_finais[i] else '-')
    print(f'{nota_alterada}({i+1:03}) original: {notas_originais[i]:05.2f} | final: {notas_finais[i]:05.2f}')

if (1 <= n <= 999):
  notas_originais = obter_notas()
  novas_notas = obter_notas()
  qtd_notas_alteradas = obter_notas_finais(notas_originais, novas_notas)
  exibir_notas_alteradas(notas_originais, novas_notas, qtd_notas_alteradas)