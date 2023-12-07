cpf=input('Digite cpf [999.999.999-99]: ')

valido=False
if len(cpf) == 14:
    valido=True
    try:

#Calculando digito 1
        dig1_ctrl=int(cpf[12])
        dig2_controle=int(cpf[13])

        d1_valores=[10,9,8,7,6,5,4,3,2]
        d2_valores=[11,10,9,8,7,6,5,4,3,2]
        digitos=[]
        # if len(cpf) == 14:
        digitos.append(cpf[0])
        digitos.append(cpf[1])
        digitos.append(cpf[2])
        digitos.append(cpf[4])
        digitos.append(cpf[5])
        digitos.append(cpf[6])
        digitos.append(cpf[8])
        digitos.append(cpf[9])
        digitos.append(cpf[10])
        digitos.append(cpf[12])
        digitos.append(cpf[13])

        print("Calculando digito1 de controle")
        d1_soma_tot1=0
        for i in range(len(d1_valores)):
            valor=int(d1_valores[i])
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
        d2_valores=[11,10,9,8,7,6,5,4,3,2]
        digitos.append(dig1_calc)
        d2_soma_tot1=0
        for i in range(len(d2_valores)):
            valor=int(d2_valores[i])
            digito=int(digitos[i])
            calc=valor*digito
            d2_soma_tot1+=calc
            print(f'{valor:02d}*{digito:02d}={calc:03d} - total={d2_soma_tot1:03d}')

        d2_soma_tot2=d2_soma_tot1*10
        dig2_calc=d2_soma_tot2%11
        dig2_calc=dig2_calc if dig2_calc<10 else 0

#Conferindo digitos calculados
        if dig1_ctrl == dig1_calc and dig2_controle == dig2_calc:
            print(f'Cpf válido - confere digitos de controle -{dig1_ctrl}{dig2_controle} com controle calculado {dig1_calc}{dig2_calc}')
        else:
            print(f'Cpf inválido - Não confere digitos de controle -{dig1_ctrl}{dig2_controle} com controle calculado {dig1_calc}{dig2_calc}')
    except:
        valido=False
if not valido:
    print(f'Cpf digitado [{cpf}] não esta formatado corretamente...')

"""
Exibe ao executar;

Digite cpf [999.999.999-99]: 746.824.890-70
Calculando digito1 de controle
10*07=070 - total=070
09*04=036 - total=106
08*06=048 - total=154
07*08=056 - total=210
06*02=012 - total=222
05*04=020 - total=242
04*08=032 - total=274
03*09=027 - total=301
02*00=000 - total=301

Calculando digito2 de controle
11*07=077 - total=077
10*04=040 - total=117
09*06=054 - total=171
08*08=064 - total=235
07*02=014 - total=249
06*04=024 - total=273
05*08=040 - total=313
04*09=036 - total=349
03*00=000 - total=349
02*07=014 - total=363
Cpf válido - confere digitos de controle -70 com controle calculado 70
"""
