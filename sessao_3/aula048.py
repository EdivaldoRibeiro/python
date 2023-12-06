lista=[123, '456', 789.1, ['a','b','c'], 'Edivaldo']

print(f'lista[0] é do tipo {type(lista[0])}')
print(f'lista[1] é do tipo {type(lista[1])}')
print(f'lista[2] é do tipo {type(lista[2])}')
print(f'lista[3] é do tipo {type(lista[3])}')
print(f'lista[4] é do tipo {type(lista[4])}')
print("")
for i in lista:
    print(f'{i} é do tipo {type(i)}')

lista[0]=lista[0]*100
lista[1]=lista[1]+'Hello Word'
lista[2]=lista[2]*100
lista[3][0]='abc'
lista[4]='Edivaldo Ribeiro'

print("")
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
print("Apagando lista[3]")
del lista[3]
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
print("Adicionando novo elemento no fim da lista")
lista.append('Laranja')
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
last_remove=lista.pop()
print(f"Removendo ultimo elemento da lista [{last_remove}]")
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
removido=lista.pop(1)
print(f"Removendo lista[1] usando lista.pop(1) da lista [{removido}]")
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
print(f"Inserindo novo valor na lista no indice=1")
lista.insert(1, 'Manoel')
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')


print("")
print(f"Concatenacao de listas")
lista_b=['eu', 'e', 'o', 'mundo']
lista+=lista_b
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
print(f"Extend de listas")
lista_c=[100,200]
lista.extend(lista_c)
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')

print("")
print(f"Copiando listas")
lista=lista_c.copy()
print(f'tamanho da lista={len(lista)}')
for i in lista:
    print(f'{i} é do tipo {type(i)}')


print("")
print(f"Limpando a lista")
lista.clear()
print(f'tamanho da lista={len(lista)}')


"""
Exibe ao executar:

lista[0] é do tipo <class 'int'>
lista[1] é do tipo <class 'str'>
lista[2] é do tipo <class 'float'>
lista[3] é do tipo <class 'list'>
lista[4] é do tipo <class 'str'>

123 é do tipo <class 'int'>
456 é do tipo <class 'str'>
789.1 é do tipo <class 'float'>
['a', 'b', 'c'] é do tipo <class 'list'>
Edivaldo é do tipo <class 'str'>

tamanho da lista=5
12300 é do tipo <class 'int'>
456Hello Word é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
['abc', 'b', 'c'] é do tipo <class 'list'>
Edivaldo Ribeiro é do tipo <class 'str'>

Apagando lista[3]
tamanho da lista=4
12300 é do tipo <class 'int'>
456Hello Word é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>

Adicionando novo elemento no fim da lista
tamanho da lista=5
12300 é do tipo <class 'int'>
456Hello Word é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>
Laranja é do tipo <class 'str'>

Removendo ultimo elemento da lista [Laranja]
tamanho da lista=4
12300 é do tipo <class 'int'>
456Hello Word é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>

Removendo lista[1] usando lista.pop(1) da lista [456Hello Word]
tamanho da lista=3
12300 é do tipo <class 'int'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>

Inserindo novo valor na lista no indice=1
tamanho da lista=4
12300 é do tipo <class 'int'>
Manoel é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>

Concatenacao de listas
tamanho da lista=8
12300 é do tipo <class 'int'>
Manoel é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>
eu é do tipo <class 'str'>
e é do tipo <class 'str'>
o é do tipo <class 'str'>
mundo é do tipo <class 'str'>

Extend de listas
tamanho da lista=10
12300 é do tipo <class 'int'>
Manoel é do tipo <class 'str'>
78910.0 é do tipo <class 'float'>
Edivaldo Ribeiro é do tipo <class 'str'>
eu é do tipo <class 'str'>
e é do tipo <class 'str'>
o é do tipo <class 'str'>
mundo é do tipo <class 'str'>
100 é do tipo <class 'int'>
200 é do tipo <class 'int'>

Copiando listas
tamanho da lista=2
100 é do tipo <class 'int'>
200 é do tipo <class 'int'>

Limpando a lista
tamanho da lista=0
"""
