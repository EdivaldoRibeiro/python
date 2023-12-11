pessoa1={'nome':'Edivaldo',
        'sobrenome':'Ribeiro',
        'profissao':'Programador',
        'idade':60,
        'altura':1.72,
        'enderecos': [
            {'rua':'tucumare', 
             'numero':100},
            {'rua':'tucumare2',
             'numero':101}
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

print('----Testando pessoa1')
print(pessoa1, type(pessoa1))
print("")
print(pessoa1.values())
print("")
print(pessoa1['nome'], pessoa1['profissao'])
print("")
print("Chaves:")
for chave in pessoa1:
    print(chave)

print('----Testando pessoa2')
print(pessoa2, type(pessoa2))
print("")
print(pessoa2.values())
print("")
print("Chaves:")
print(pessoa2['nome'], pessoa2['profissao'])
for chave in pessoa2:
    print(chave)

"""
Exibe ao executar:

----Testando pessoa1
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador', 'idade': 60, 'altura': 1.72, 'enderecos': [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]} <class 'dict'>

dict_values(['Edivaldo', 'Ribeiro', 'Programador', 60, 1.72, [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]])

Edivaldo Programador

Chaves:
nome
sobrenome
profissao
idade
altura
enderecos
----Testando pessoa2
{'nome': 'Edivaldo', 'sobrenome': 'Ribeiro', 'profissao': 'Programador', 'idade': 60, 'altura': 1.72, 'enderecos': [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]} <class 'dict'>

dict_values(['Edivaldo', 'Ribeiro', 'Programador', 60, 1.72, [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]])

Chaves:
Edivaldo Programador
nome
sobrenome
profissao
idade
altura
enderecos
"""
