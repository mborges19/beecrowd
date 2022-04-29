# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

a = int(input()) % 2
b = int(input()) % 2
c = int(input()) % 2
d = int(input()) % 2
e = int(input()) % 2

valores = [a, b, c, d, e]
valores = valores.count(0)
print(f'{valores} valores pares')