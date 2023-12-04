#Exercicio 1
entrada=input("Digite um numero: ")

try:
    inteiro=int(entrada)
    par=inteiro%2==0
    if par:
        print(f'O número {inteiro} é par')
    else:
        print(f'O número {inteiro} é impar')
except:
    print(f'{entrada} não é um inteiro')

#Exercicio 2
hora=input("Digite um horario (hh:mm): ")

if len(hora) != 5:
    print(f'Horário {hora} no formato invalido...')
else:
    hora_ok=False
    minuto_ok=False
    try:
        hh=int(hora[:2])
        mm=int(hora[3:])
        if hh >= 0 and hh <= 23:
            hora_ok=True
        if mm >= 0 and mm <= 59:
            minuto_ok=True
        
        bom_dia   = hora_ok and (hh >= 0  and hh <= 11)
        boa_tarde = hora_ok and (hh >= 12 and hh <= 17)
        boa_noite = hora_ok and (hh >= 18 and hh <= 23)

        #now=f'{hh}:{mm}'
        now='%02d:%02d' % (hh, mm)
        if bom_dia and minuto_ok:
            print(f'Bom dia {now}')
        elif boa_tarde and minuto_ok:
            print(f'Boa tarde {now}')
        elif boa_noite and minuto_ok:
            print(f'Boa noite {now}')
        else:
            print(f'{now} não é um horário válido')
    except:
        print(f'{hora} não é um horario válido')

#Exercicio 3
nome=input("Nome: ")
size=len(nome)
nome_curto = size <= 4
nome_normal = size >= 5 and size <= 6
nome_grande = size > 6
if nome_curto:
    print(f'{nome} é tamanho curto')
elif nome_normal:
    print(f'{nome} tem tamanho normal')
else:
    print(f'{nome} é tamanho grande')

"""
Exibe ao executar:

Digite um numero: 7
O número 7 é impar
Digite um horario (hh:mm): 07:20
Bom dia 07:20
Nome: Edivaldo
Edivaldo é tamanho grande
"""
