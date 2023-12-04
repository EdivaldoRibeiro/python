numero=input("Digite um valor: ")

try:
    print(f'[{numero}] é um digito: {numero.isdigit()}')
    print(f'[{numero}] é um numero: {numero.isnumeric()}')

    dobro=float(numero)*2
    print(f'O dobro de [{numero}] é [{dobro:.2f}]')
except:
    print(f'[{numero}] não é numero válido')

"""
Exibe ao executar:

Digite um valor: 5.5
[5.5] é um digito: False
[5.5] é um numero: False
O dobro de [5.5] é [11.00]
"""
