dia_da_semana = input()

dia_para_entrega = int(input())

if dia_para_entrega == 0:
    print('chega hoje!')

if dia_da_semana == 'domingo':
    if dia_para_entrega == 1:
        print('sera entregue segunda')
    elif dia_para_entrega == 2:
        print('sera entregue terca')
    elif dia_para_entrega == 3:
        print('sera entregue quarta')
    elif dia_para_entrega == 4:
        print('sera entregue quinta')
    elif dia_para_entrega == 5:
        print('sera entregue sexta')
    elif dia_para_entrega == 6:
        print('sera entregue sabado')

if dia_da_semana == 'segunda':
    if dia_para_entrega == 1:
        print('sera entregue terca')
    elif dia_para_entrega == 2:
        print('sera entregue quarta')
    elif dia_para_entrega == 3:
        print('sera entregue quinta')
    elif dia_para_entrega == 4:
        print('sera entregue sexta')
    elif dia_para_entrega == 5:
        print('sera entregue sabado')
    elif dia_para_entrega == 6:
        print('sera entregue domingo')

if dia_da_semana == 'terca':
    if dia_para_entrega == 1:
        print('sera entregue quarta')
    elif dia_para_entrega == 2:
        print('sera entregue quinta')
    elif dia_para_entrega == 3:
        print('sera entregue sexta')
    elif dia_para_entrega == 4:
        print('sera entregue sabado')
    elif dia_para_entrega == 5:
        print('sera entregue domingo')
    elif dia_para_entrega == 6:
        print('sera entregue segunda')

if dia_da_semana == 'quarta':
    if dia_para_entrega == 1:
        print('sera entregue quinta')
    elif dia_para_entrega == 2:
        print('sera entregue sexta')
    elif dia_para_entrega == 3:
        print('sera entregue sabado')
    elif dia_para_entrega == 4:
        print('sera entregue domingo')
    elif dia_para_entrega == 5:
        print('sera entregue segunda')
    elif dia_para_entrega == 6:
        print('sera entregue terca')

if dia_da_semana == 'quinta':
    if dia_para_entrega == 1:
        print('sera entregue sexta')
    elif dia_para_entrega == 2:
        print('sera entregue sabado')
    elif dia_para_entrega == 3:
        print('sera entregue domingo')
    elif dia_para_entrega == 4:
        print('sera entregue segunda')
    elif dia_para_entrega == 5:
        print('sera entregue terca')
    elif dia_para_entrega == 6:
        print('sera entregue quarta')

if dia_da_semana == 'sexta':
    if dia_para_entrega == 1:
        print('sera entregue sabado')
    elif dia_para_entrega == 2:
        print('sera entregue domingo')
    elif dia_para_entrega == 3:
        print('sera entregue segunda')
    elif dia_para_entrega == 4:
        print('sera entregue terca')
    elif dia_para_entrega == 5:
        print('sera entregue quarta')
    elif dia_para_entrega == 6:
        print('sera entregue quinta')

if dia_da_semana == 'sabado':
    if dia_para_entrega == 1:
        print('sera entregue domingo')
    elif dia_para_entrega == 2:
        print('sera entregue segunda')
    elif dia_para_entrega == 3:
        print('sera entregue terca')
    elif dia_para_entrega == 4:
        print('sera entregue quarta')
    elif dia_para_entrega == 5:
        print('sera entregue quinta')
    elif dia_para_entrega == 6:
        print('sera entregue sexta')