def responsavel(cat):
    r = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']
    return r[feedback-1]


qtd_dias = int(input())

for i in range(qtd_dias):
    qtd_feedbacks = int(input())
    for j in range(qtd_feedbacks):
        feedback = int(input())
        print(responsavel(feedback))
