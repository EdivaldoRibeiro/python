import pprint

_NOME='nome'
_SOBRENOME='sobrenome'
_IDADE='idade'
_ALTURA='altura'

def p(v, seq):
    print('')
    print(f'---Teste{seq}----------')
    pprint.pprint(v, sort_dicts=False, width=60)

pessoa1={_NOME:'Edivaldo',
        _SOBRENOME:'Ribeiro',
        _IDADE: 60,
        _ALTURA: 1.72}

pessoa2={
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in pessoa1.items()
}

pessoa3={
    key: value if isinstance(value, (int, float)) else value.upper()+'__'
    for key, value in pessoa1.items()
}

pessoa4={
    key: '['+value.upper()+']' if isinstance(value, str) else value
    for key, value in pessoa1.items()
    if key != _IDADE
}

p(pessoa1, 1)
p(pessoa2, 2)
p(pessoa3, 3)
p(pessoa4, 4)

"""
Exibe ao executar:


---Teste1----------
{'nome': 'Edivaldo',
 'sobrenome': 'Ribeiro',
 'idade': 60,
 'altura': 1.72}

---Teste2----------
{'nome': 'EDIVALDO',
 'sobrenome': 'RIBEIRO',
 'idade': 60,
 'altura': 1.72}

---Teste3----------
{'nome': 'EDIVALDO__',
 'sobrenome': 'RIBEIRO__',
 'idade': 60,
 'altura': 1.72}

---Teste4----------
{'nome': '[EDIVALDO]',
 'sobrenome': '[RIBEIRO]',
 'altura': 1.72}
"""
