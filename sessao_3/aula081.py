#lambda
_NOME='nome'
_SOBRENOME='sobrenome'

def exibe(lista, seq):
    print('')
    print(f'---Teste{seq}----------')
    for obj in lista:
        print(obj)

def compare_nome(item):
    return item[_NOME]

def compare_sobrenome(item):
    return item[_SOBRENOME]

lista=[]

pessoa1={_NOME:'Edivaldo',
        _SOBRENOME:'Ribeiro'}

pessoa2={_NOME:'Jonata',
        _SOBRENOME:'Miller'}

pessoa3={_NOME:'Edgar',
        _SOBRENOME:'Burrougst'}

#Teste1
lista.append(pessoa1)
lista.append(pessoa2)
lista.append(pessoa3)
exibe(lista, 1)

#Teste2
lista.sort(key=compare_nome)
exibe(lista, 2)

#Teste3
lista.sort(key=compare_sobrenome)
exibe(lista, 3)

#Teste4
lista.sort(key=lambda item:item['nome'])
exibe(lista, 4)

#Teste5
lista2=sorted(lista, key=lambda item:item['sobrenome'])
exibe(lista2, 5)

"""
Exibe ao executar:

---Teste1----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}

---Teste2----------
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}

---Teste3----------
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}

---Teste4----------
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}

---Teste5----------
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
"""
