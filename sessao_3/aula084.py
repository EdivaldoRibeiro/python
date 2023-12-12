import pprint

#List coprehension
_NOME='nome'
_SOBRENOME='sobrenome'

def p(v, seq):
    print('')
    print(f'---Teste{seq}----------')
    pprint.pprint(v, sort_dicts=False, width=60)

def exibe(lista, seq):
    print('')
    print(f'---Teste{seq}----------')
    print(*lista, sep='\n')
    
lista1=[val%5 for val in range(15)]
print(lista1)

lista2=['Joao','Jose','Maria','Madalena']
lista3=[nome for nome in lista2]
print(lista3)

pessoa1={_NOME:'Edivaldo',
        _SOBRENOME:'Ribeiro'}

pessoa2={_NOME:'Jonata',
        _SOBRENOME:'Miller'}

pessoa3={_NOME:'Edgar',
        _SOBRENOME:'Burrougst'}

#Teste1
lista=[]
lista.append(pessoa1)
lista.append(pessoa2)
lista.append(pessoa3)
exibe(lista, 1)

lista4=[item[_NOME] for item in lista]
exibe(lista4, 2)

lista4=[item[_SOBRENOME] for item in lista]
exibe(lista4, 3)

lista4=[{_NOME:item[_NOME],_SOBRENOME:item[_SOBRENOME]} for item in lista]
exibe(lista4, 4)

lista4=[{**item} for item in lista]
exibe(lista4, 5)

lista4=[{**item, _SOBRENOME:item[_SOBRENOME]+'__'} for item in lista]
exibe(lista4, 6)

lista4=[{**item, _SOBRENOME:item[_SOBRENOME]+'_DEL'} if item[_NOME] != 'Edivaldo' else {**item, _NOME:item[_NOME]+'_DEL'} for item in lista]
exibe(lista4, 7)

lista4=[{**item} if item[_NOME] != 'Edivaldo' else {**item, _NOME:item[_NOME]+'_DEL'} for item in lista if item[_NOME] != 'Edivaldo']
p(lista4, 8)

lista5=[n for n in range(15)]
p(lista5, 9)

lista5=[n for n in range(15) if n%2==0]
p(lista5, 10)

"""
Exibe ao executar:

[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
['Joao', 'Jose', 'Maria', 'Madalena']

---Teste1----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}

---Teste2----------
Edivaldo
Jonata
Edgar

---Teste3----------
Ribeiro
Miller
Burrougst

---Teste4----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}

---Teste5----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}

---Teste6----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro__'}
{'nome': 'Jonata', 'sobrenome': 'Miller__'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst__'}

---Teste7----------
{'nome': 'Edivaldo_DEL', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller_DEL'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst_DEL'}

---Teste8----------
[{'nome': 'Jonata', 'sobrenome': 'Miller'},
 {'nome': 'Edgar', 'sobrenome': 'Burrougst'}]

---Teste9----------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

---Teste10----------
[0, 2, 4, 6, 8, 10, 12, 14]
"""
