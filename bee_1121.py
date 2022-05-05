preco = float(input())
quantidade = int(input())
preco_total = preco * quantidade
desconto = 10 + quantidade
valor_desconto = preco_total * (desconto/100)
preco_final = preco_total - valor_desconto
print(f'{preco_total:.2f}')
print(f'{preco_final:.2f}')