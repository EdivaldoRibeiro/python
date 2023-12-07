cpf=input('Digite cpf [999.999.999-99]: ')

valido=False
if len(cpf) == 14:
    valido=True
    try:

        dig1_controle=int(cpf[12])
        dig2_controle=int(cpf[13])

        valores=[10,9,8,7,6,5,4,3,2]
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

        tot1_soma=0
        for i in range(len(valores)):
            valor=int(valores[i])
            digito=int(digitos[i])
            calc=valor*digito
            tot1_soma+=calc
            print(f'{valor:02d}*{digito:02d}={calc:03d} - total={tot1_soma:03d}')

        tot2_soma=tot1_soma*10
        dig_calculado=tot2_soma%11
        dig_calculado=dig_calculado if dig_calculado<10 else 0

        if dig1_controle == dig_calculado:
            print(f'Cpf válido - bate primeiro digito de controle -{dig1_controle}{dig2_controle} com controle calculado {dig_calculado}')
        else:
            print(f'Cpf inválido - Não bate primeiro digito de controle -{dig1_controle}{dig2_controle} com controle calculado {dig_calculado}')
    except:
        valido=False
if not valido:
    print(f'Cpf digitado [{cpf}] não esta formatado corretamente...')

"""
Exibe ao executar;

Digite cpf [999.999.999-99]: 746.824.890-70
10*07=070 - total=070
09*04=036 - total=106
08*06=048 - total=154
07*08=056 - total=210
06*02=012 - total=222
05*04=020 - total=242
04*08=032 - total=274
03*09=027 - total=301
02*00=000 - total=301
Cpf válido - bate primeiro digito de controle -70 com controle calculado 7

"""
