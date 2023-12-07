import decimal

print("Estranho...")
numero_1=0.1
numero_2=0.7
numero_3=numero_1+numero_2
print(f'numero_3={numero_3}')
print(f'numero_3={numero_3:.2f}')
print(f'numero_3={round(numero_3,3)}')

print("")
print("Usando decimal.Decimal")
numero_1=decimal.Decimal('0.')
numero_2=decimal.Decimal('0.7')
print(f'numero_3={numero_3:.2f}')


"""
Exibe ao executar:

Estranho...
numero_3=0.7999999999999999
numero_3=0.80
numero_3=0.8

Usando decimal.Decimal
numero_3=0.80
"""
