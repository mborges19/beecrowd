vc = 2.5
real = 0

while True:
    n = float(input())
    if n == -1.0:
        break
    real += n
doacao = real*vc

print(f'VC$ {real:.2f}')
print(f'R$ {doacao:.2f}')