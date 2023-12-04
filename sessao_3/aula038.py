MAX1=101
MAX2=102 
contador1=0
condicao1=contador1 < MAX1
while condicao1:
    contador1+=1
    condicao1=contador1 < MAX1
    multiplo_cinco=contador1%5==0
    print(f'Loop principal continua enquanto {contador1:02d} < {MAX1} - {condicao1}')
    if multiplo_cinco:
        print(f'Terminando forcado loop principal porque é multiplo de cinco')
        break

    contador2=0
    condicao2=contador2 < MAX2
    while condicao2:
        contador2+=1
        condicao2=contador2 < MAX2
        multiplo_tres=contador2%3==0
        print(f'\tLoop secundario continua enquanto {contador2:02d} < {MAX2} - {condicao2}')
        if multiplo_tres:
            print(f'\tTerminando forcado loop secundario porque é multiplo de tres')
            break

"""
Exibe ao executar:

Loop principal continua enquanto 01 < 101 - True
        Loop secundario continua enquanto 01 < 102 - True
        Loop secundario continua enquanto 02 < 102 - True
        Loop secundario continua enquanto 03 < 102 - True
        Terminando forcado loop secundario porque é multiplo de tres
Loop principal continua enquanto 02 < 101 - True
        Loop secundario continua enquanto 01 < 102 - True
        Loop secundario continua enquanto 02 < 102 - True
        Loop secundario continua enquanto 03 < 102 - True
        Terminando forcado loop secundario porque é multiplo de tres
Loop principal continua enquanto 03 < 101 - True
        Loop secundario continua enquanto 01 < 102 - True
        Loop secundario continua enquanto 02 < 102 - True
        Loop secundario continua enquanto 03 < 102 - True
        Terminando forcado loop secundario porque é multiplo de tres
Loop principal continua enquanto 04 < 101 - True
        Loop secundario continua enquanto 01 < 102 - True
        Loop secundario continua enquanto 02 < 102 - True
        Loop secundario continua enquanto 03 < 102 - True
        Terminando forcado loop secundario porque é multiplo de tres
Loop principal continua enquanto 05 < 101 - True
Terminando forcado loop principal porque é multiplo de cinco
"""
