_NOME='nome'
_SOBRENOME='sobrenome'
_PROFISSAO='profissao'
_IDADE='idade'
_ALTURA='altura'
_ENDERECOS='enderecos'
_RUA='rua'
_NUMERO='numero'

pessoa1={_NOME:'Edivaldo',
        _SOBRENOME:'Ribeiro',
        _PROFISSAO:'Programador',
        _IDADE:60,
        _ALTURA:1.72,
        _ENDERECOS: [
            {_RUA:'tucumare', 
             _NUMERO:100},
            {_RUA:'tucumare2',
             _NUMERO:101}
        ]
        }

pessoa2=dict(nome='Edivaldo',
             sobrenome='Ribeiro',
             profissao='Programador',
             idade=60,
             altura=1.72,
             enderecos=[dict(rua='tucumare',numero=100),
                        dict(rua='tucumare2',numero=101)]
             )

pessoa3={}
pessoa3[_NOME]='Edivaldo'
pessoa3[_SOBRENOME]='Ribeiro'
pessoa3[_PROFISSAO]='Programador'
pessoa3[_IDADE]=60
pessoa3[_ALTURA]=1.72
pessoa3[_ENDERECOS]=[dict(rua='tucumare',numero=100),
                        dict(rua='tucumare2',numero=101)]

print('----Testando pessoa1')
print(pessoa1, type(pessoa1))
print("")
print(pessoa1.values())
print("")
print(pessoa1[_NOME], pessoa1[_PROFISSAO])
print("")
print("Chave=Valor")
for chave in pessoa1:
    print(f"pessoa1['{chave}']={pessoa1[chave]}")

print("")
print('----Testando pessoa2')
print(pessoa2, type(pessoa2))
print("")
print(pessoa2.values())
print("")
print("Chave=Valor")
print(pessoa2[_NOME], pessoa2[_PROFISSAO])
for chave in pessoa2:
    print(f"pessoa2['{chave}']={pessoa2[chave]}")

print("")
print('----Testando pessoa3')
print(pessoa3, type(pessoa3))
print("")
print(pessoa3.values())
print("")
print("Chave=Valor")
print(pessoa3[_NOME], pessoa3[_PROFISSAO])
for chave in pessoa3:
    print(f"pessoa3['{chave}']={pessoa3[chave]}")
print("")
print('----Testando pessoa3 - deletando enderecos')
del pessoa3[_ENDERECOS]
for chave in pessoa3:
    print(f"pessoa3['{chave}']={pessoa3[chave]}")

"""
Exibe ao executar:

----Testando pessoa1
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador', 'idade': 60, 'altura': 1.72, 'enderecos': [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]} <class 'dict'>

dict_values(['Edivaldo', 'Ribeiro', 'Programador', 60, 1.72, [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]])

Edivaldo Programador

Chave=Valor
pessoa1['nome']=Edivaldo
pessoa1['sobrenome']=Ribeiro
pessoa1['profissao']=Programador
pessoa1['idade']=60
pessoa1['altura']=1.72
pessoa1['enderecos']=[{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]

----Testando pessoa2
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador', 'idade': 60, 'altura': 1.72, 'enderecos': [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]} <class 'dict'>

dict_values(['Edivaldo', 'Ribeiro', 'Programador', 60, 1.72, [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]])

Chave=Valor
Edivaldo Programador
pessoa2['nome']=Edivaldo
pessoa2['sobrenome']=Ribeiro
pessoa2['profissao']=Programador
pessoa2['idade']=60
pessoa2['altura']=1.72
pessoa2['enderecos']=[{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]

----Testando pessoa3
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador', 'idade': 60, 'altura': 1.72, 'enderecos': [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]} <class 'dict'>

dict_values(['Edivaldo', 'Ribeiro', 'Programador', 60, 1.72, [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]])

Chave=Valor
Edivaldo Programador
pessoa3['nome']=Edivaldo
pessoa3['sobrenome']=Ribeiro
pessoa3['profissao']=Programador
pessoa3['idade']=60
pessoa3['altura']=1.72
pessoa3['enderecos']=[{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]

----Testando pessoa3 - deletando enderecos
pessoa3['nome']=Edivaldo
pessoa3['sobrenome']=Ribeiro
pessoa3['profissao']=Programador
pessoa3['idade']=60
pessoa3['altura']=1.72
"""
