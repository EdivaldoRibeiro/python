valor1=input("digite primeiro valor (2 caracteres): ")
valor2=input("digite segundo valor (2 caracteres): ")

if valor1 == valor2:
    print(f'{valor1} igual {valor2}')
elif valor1 >= valor2:
    print(f'{valor1} maior ou igual {valor2}')
elif valor1 > valor2:
    print(f'{valor1} maior que {valor2}')
elif valor1 < valor2:
    print(f'{valor1} menor que {valor2}')
elif valor1 <= valor2:
    print(f'{valor1} menor ou igual {valor2}')
else:
    print("ferrou a lógica...")

"""
Exibe ao executar:

(2 caracteres)
"""
