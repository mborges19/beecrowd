peca1 = input().split()
peca2 = input().split()

codigo_p1 = int(peca1[0])
quantidade_p1 = int(peca1[1])
valor_p1 = float(peca1[2])

codigo_p2 = int(peca2[0])
quantidade_p2 = int(peca2[1])
valor_p2 = float(peca2[2])

valor_total = (quantidade_p1 * valor_p1) + (quantidade_p2 * valor_p2)
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')