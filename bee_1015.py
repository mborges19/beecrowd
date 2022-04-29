# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula

from math import sqrt

x1, y1 = list(map(float,input().split()))
x2, y2 = list(map(float,input().split()))

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'{distancia:.4f}')