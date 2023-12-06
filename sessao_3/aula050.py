lista=['Edivaldo']
lista.append('Jose')
lista.append('Maria')
lista.append('Madalena')

print("Sugestao usando idx")
idx=0
for nome in lista:
    print(f'{idx:02d} - {nome}')
    idx+=1

print("")
print("Sugestao usando range")
index=range(0,len(lista))
for i  in index:
    print(f'{i:02d} - {lista[i]}')

"""
Exibe ao executar:

Sugestao usando idx
00 - Edivaldo
01 - Jose
02 - Maria
03 - Madalena

Sugestao usando range
00 - Edivaldo
01 - Jose
02 - Maria
03 - Madalena
"""
