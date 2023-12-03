valor1=input("digite valor1: ")
valor2=input("digite valor2: ")

num1=-1
if valor1.isnumeric:
    num1=int(valor1)

num2=-1
if valor2.isnumeric:
    num2=int(valor2)

maior=num1>num2
maior_igual=num1>=num2
menor=num1<num2
menor_igual=num1<=num2

print(f'{num1} é maior que {num2} {maior}')
print(f'{num1} é maior_igual que {num2} {maior_igual}')
print(f'{num1} é menor que {num2} {menor}')
print(f'{num1} é menor_igual que {num2} {menor_igual}')

"""
Exibe ao executar:

digite valor1: 5
digite valor2: 5
5 é maior que 5 False
5 é maior_igual que 5 True
5 é menor que 5 False
5 é menor_igual que 5 True
"""
