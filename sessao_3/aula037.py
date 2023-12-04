MAX_LOOP=500
contador=0
condicao = contador < MAX_LOOP
while condicao:
    contador+=1
    multiplo_dois = contador%2 == 0 
    multiplo_sete = contador%7 == 0 
    multiplo_dezessete = contador%17 == 0
    condicao = contador < MAX_LOOP

    if not (multiplo_dois or multiplo_sete or multiplo_dezessete) :
        continue;

    if multiplo_dois:
        print(f'Loop termina quando {contador:02d} < {MAX_LOOP} - {condicao} é multiplo de dois')
    
    if multiplo_sete:
        print(f'Loop termina quando {contador:02d} < {MAX_LOOP} - {condicao} é multiplo de sete')
    
    if multiplo_dezessete:
        print(f'Forcando terminar o loop {contador:02d} < {MAX_LOOP} - {condicao} é multiplo de dezessete')
        break

"""
Exibe ao executar:

Loop termina quando 02 < 500 - True é multiplo de dois
Loop termina quando 04 < 500 - True é multiplo de dois
Loop termina quando 06 < 500 - True é multiplo de dois
Loop termina quando 07 < 500 - True é multiplo de sete
Loop termina quando 08 < 500 - True é multiplo de dois
Loop termina quando 10 < 500 - True é multiplo de dois
Loop termina quando 12 < 500 - True é multiplo de dois
Loop termina quando 14 < 500 - True é multiplo de dois
Loop termina quando 14 < 500 - True é multiplo de sete
Loop termina quando 16 < 500 - True é multiplo de dois
Forcando terminar o loop 17 < 500 - True é multiplo de dezessete
"""
