import random

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
        d1_soma_tot1=0
        for i in range(len(D1_VALS)):
            valor=int(D1_VALS[i])
            digito=int(digitos[i])
            calc=valor*digito
            d1_soma_tot1+=calc
            print(f'{valor:02d}*{digito:02d}={calc:03d} - total={d1_soma_tot1:03d}')

        d1_soma_tot2=d1_soma_tot1*10
        dig1_calc=d1_soma_tot2%11
        dig1_calc=dig1_calc if dig1_calc<10 else 0

# Calculando digito 2

        print("")
        print("Calculando digito2 de controle")
        digitos.append(dig1_calc)
        d2_soma_tot1=0
        for i in range(len(D2_VALS)):
            valor=int(D2_VALS[i])
            digito=int(digitos[i])
            calc=valor*digito
            d2_soma_tot1+=calc
            print(f'{valor:02d}*{digito:02d}={calc:03d} - total={d2_soma_tot1:03d}')

        d2_soma_tot2=d2_soma_tot1*10
        dig2_calc=d2_soma_tot2%11
        dig2_calc=dig2_calc if dig2_calc<10 else 0

#Criando novo cpf
        novo_cpf=f"{cpf}-{dig1_calc}{dig2_calc}"
        print(f'Novo cpf criado é {novo_cpf}')
    except:
        valido=False

if not valido:
    print(f'Cpf digitado [{cpf}] não esta formatado corretamente...')

"""
Exibe ao executar;

cpf randomico: 413.710.925

Calculando digito1 de controle
10*04=040 - total=040
09*01=009 - total=049
08*03=024 - total=073
07*07=049 - total=122
06*01=006 - total=128
05*00=000 - total=128
04*09=036 - total=164
03*02=006 - total=170
02*05=010 - total=180

Calculando digito2 de controle
11*04=044 - total=044
10*01=010 - total=054
09*03=027 - total=081
08*07=056 - total=137
07*01=007 - total=144
06*00=000 - total=144
05*09=045 - total=189
04*02=008 - total=197
03*05=015 - total=212
02*07=014 - total=226
Novo cpf criado é 413.710.925-75
"""
