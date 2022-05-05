nota_trabalho = float(input())
nota_prova = float(input())
media = (nota_prova + nota_trabalho) / 2

if media >= 6 and (nota_prova >= 6 or nota_prova >= 2):
    print('aprovado')

elif 6 > nota_trabalho >= 6 or nota_trabalho >= 2:
    print('talvez com a sub')

else:
    print('reprovado')