nome=input("Digite nome: ")
encontrar=input("O que encontrar: ")

if(encontrar in nome) :
    print(f'Encontrou {encontrar} em {nome}')
else:
    print(f'Nao encontrou {encontrar} em {nome}')

nome="Edivaldo"
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])
print(nome[7])

print(f'\'l\' in nome       ->{'l' in nome}')
print(f'\'X\' in nome       ->{'X' in nome}')
print(f'\'Edi\' in nome     ->{'Edi' in nome}')
print(f'\'Edi\' not in nome ->{'Edi' not in nome}')

"""
Exibe ao executar:

Digite nome: abacaxi
O que encontrar: caxi
Encontrou caxi em abacaxi
E
d
i
v
a
l
d
o
'l' in nome       ->True
'X' in nome       ->False
'Edi' in nome     ->True
'Edi' not in nome ->False
"""
