_NOME='nome'
_SOBRENOME='sobrenome'
_PROFISSAO='profissao'
_IDADE='idade'
_ALTURA='altura'

def exibe(lista, seq):
    print('')
    print(f'---Teste{seq}----------')
    for obj in lista:
        print(obj)

def argumentos_nomeados(*args, **wkargs):
    print('NAO NOMEADOS:', args)
    print(wkargs)
    for chave, valor in wkargs.items():
        print(chave, valor)

lista=[]

pessoa1={_NOME:'Edivaldo',
        _SOBRENOME:'Ribeiro'}

pessoa2={_NOME:'Jonata',
        _SOBRENOME:'Miller'}

pessoa3={_NOME:'Edgar',
        _SOBRENOME:'Burrougst'}

complemento1={_PROFISSAO:'Programador pl/sql',
              _IDADE:60,
              _ALTURA:1.72}

#Teste1
lista.append(pessoa1)
lista.append(pessoa2)
lista.append(pessoa3)
exibe(lista, 1)

a, b=pessoa1
print()
print('indices')
print(f'a={a}, b={b}')

a, b=pessoa1.values()
print()
print('valores')
print(f'a={a}, b={b}')

a, b=pessoa1.items()
print()
print('tuplas')
print(f'a={a}, b={b}')

(a1,a2), (b1, b2)=pessoa1.items()
print()
print('tuplas')
print(f'a=[{a1}, {a2}] b=[{b1}, {b2}]')

print()
print('Usando for')
for val in pessoa1:
    print(val)

print()
print('Usando items()')
for chave, valor in pessoa1.items():
    print(chave, valor)

print()
print('Adicionando ao dicionario')
completo={**pessoa1, **complemento1}
print(completo)

print()
print('Testando argumentos nomeados')
argumentos_nomeados('mane', 'zé', nome='Jonata', sobrenome='Miller')
argumentos_nomeados(**completo)

"""
Exibe ao executar:


---Teste1----------
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro'}
{'nome': 'Jonata', 'sobrenome': 'Miller'}
{'nome': 'Edgar', 'sobrenome': 'Burrougst'}

indices
a=nome, b=sobrenome

valores
a=Edivaldo, b=Ribeiro

tuplas
a=('nome', 'Edivaldo'), b=('sobrenome', 'Ribeiro')

tuplas
a=[nome, Edivaldo] b=[sobrenome, Ribeiro]

Usando for
nome
sobrenome

Usando items()
nome Edivaldo
sobrenome Ribeiro

Adicionando ao dicionario
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador pl/sql', 'idade': 60, 'altura': 1.72}

Testando argumentos nomeados
NAO NOMEADOS: ('mane', 'zé')
{'nome': 'Jonata', 'sobrenome': 'Miller'}
nome Jonata
sobrenome Miller
NAO NOMEADOS: ()
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador pl/sql', 'idade': 60, 'altura': 1.72}
nome Edivaldo
sobrenome Ribeiro
profissao Programador pl/sql
idade 60
altura 1.72
"""
