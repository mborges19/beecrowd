# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

n = int(input())
h = int(input())
v = float(input())

salario = h * v
print(f'NUMBER = {n}\nSALARY = U$ {salario:.2f}')