adicao=1+3
subtracao=adicao-1.5
multiplicacao=adicao*subtracao
divisao=multiplicacao/adicao
divisao_inteira=multiplicacao//adicao
exponenciacao=2**16
modulo=exponenciacao%5

print("adicao:",adicao)
print("subtracao:",subtracao)
print("multiplicacao:",multiplicacao)
print("divisao:", divisao, type(divisao))
print("divisao_inteira:", divisao_inteira, type(divisao_inteira))
print("exponenciacao:", exponenciacao)
print("modulo:", modulo)

print("32 é multiplo de 16:", 32%16==0)

"""
Exibe ao executar:

adicao: 4
subtracao: 2.5
multiplicacao: 10.0
divisao: 2.5 <class 'float'>
divisao_inteira: 2.0 <class 'float'>
exponenciacao: 65536
modulo: 1
32 é multiplo de 16: True
"""
