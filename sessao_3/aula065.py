import random

def calculo(VALS, digitos):
    soma=0
    for i in range(len(VALS)):
        valor=int(VALS[i])
        digito=int(digitos[i])
        calc=valor*digito
        soma+=calc
        print(f'{valor:02d}*{digito:02d}={calc:03d} - total={soma:03d}')

    soma_tot=soma*10
    calc=soma_tot%11
    calc=calc if calc<10 else 0

    return calc

D1_VALS=[10,9,8,7,6,5,4,3,2]
D2_VALS=[11,10,9,8,7,6,5,4,3,2]

# cpf=input('Fabricar um cpf [999.999.999]: ')

cpf=''
for i in range(9):
    cpf+=str(random.randint(0,9))
    if i in (2,5):
        cpf+='.'
print(f'cpf randomico: {cpf}')

valido=False
if len(cpf) == 11:
    valido=True
    try:

        digitos=[]
        for i in range(len(cpf)):
            if i not in (3,7):
                char=cpf[i]
                digitos.append(int(char))

#Calculando digito 1
        print("")
        print("Calculando digito1 de controle")
        dig1_calc=calculo(D1_VALS, digitos)

# Calculando digito 2

        print("")
        print("Calculando digito2 de controle")
        digitos.append(dig1_calc)
        dig2_calc=calculo(D2_VALS, digitos)

#Criando novo cpf
        novo_cpf=f"{cpf}-{dig1_calc}{dig2_calc}"
        print(f'Novo cpf criado é {novo_cpf}')
    except:
        valido=False

if not valido:
    print(f'Cpf digitado [{cpf}] não esta formatado corretamente...')

"""
Exibe ao executar;

cpf randomico: 774.799.000

Calculando digito1 de controle
10*07=070 - total=070
09*07=063 - total=133
08*04=032 - total=165
07*07=049 - total=214
06*09=054 - total=268
05*09=045 - total=313
04*00=000 - total=313
03*00=000 - total=313
02*00=000 - total=313

Calculando digito2 de controle
11*07=077 - total=077
10*07=070 - total=147
09*04=036 - total=183
08*07=056 - total=239
07*09=063 - total=302
06*09=054 - total=356
05*00=000 - total=356
04*00=000 - total=356
03*00=000 - total=356
02*06=012 - total=368
Novo cpf criado é 774.799.000-66
"""
