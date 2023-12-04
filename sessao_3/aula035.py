MAX_LOOP=12
contador=0
condicao=True
while condicao:
    contador+=1
    print(f'Seq.{contador:02d} vai parar em {MAX_LOOP:02d} - {condicao}')
    condicao=contador < MAX_LOOP


"""
Exibe ao executar:

Seq.01 vai parar em 12 - True
Seq.02 vai parar em 12 - True
Seq.03 vai parar em 12 - True
Seq.04 vai parar em 12 - True
Seq.05 vai parar em 12 - True
Seq.06 vai parar em 12 - True
Seq.07 vai parar em 12 - True
Seq.08 vai parar em 12 - True
Seq.09 vai parar em 12 - True
Seq.10 vai parar em 12 - True
Seq.11 vai parar em 12 - True
Seq.12 vai parar em 12 - True
"""
