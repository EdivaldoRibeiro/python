MAX_TST=10
contador=MAX_TST
condicao=contador>=0
seq=0
calc=1
while condicao:
    calc*=2
    seq+=1
    print(f'Continua loop enquanto ({contador:02d} >= 0) - {condicao} (2^{seq}={calc:04d})')
    contador-=1
    condicao=contador>=0

"""
Exibe ao executar:

Continua loop enquanto (10 >= 0) - True (2^1=0002)
Continua loop enquanto (09 >= 0) - True (2^2=0004)
Continua loop enquanto (08 >= 0) - True (2^3=0008)
Continua loop enquanto (07 >= 0) - True (2^4=0016)
Continua loop enquanto (06 >= 0) - True (2^5=0032)
Continua loop enquanto (05 >= 0) - True (2^6=0064)
Continua loop enquanto (04 >= 0) - True (2^7=0128)
Continua loop enquanto (03 >= 0) - True (2^8=0256)
Continua loop enquanto (02 >= 0) - True (2^9=0512)
Continua loop enquanto (01 >= 0) - True (2^10=1024)
Continua loop enquanto (00 >= 0) - True (2^11=2048)
"""
