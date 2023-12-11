import copy

_NOME='nome'
_SOBRENOME='sobrenome'
_PROFISSAO='profissao'
_IDADE='idade'
_ALTURA='altura'
_ENDERECOS='enderecos'
_RUA='rua'
_NUMERO='numero'
_ID='id'
_TIPO='tipo'

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
pessoa1.setdefault(_ID, 1)
pessoa1.setdefault(_TIPO, 'pf')

#copia raza
pessoa2=pessoa1.copy()
pessoa2[_ID]=2
pessoa2[_TIPO]='pj'
pessoa2[_ENDERECOS]=pessoa1[_ENDERECOS][0][_RUA]='ponhangaba'

#copia profunda
pessoa3=copy.deepcopy(pessoa1)
pessoa3[_ID]=3
pessoa3[_TIPO]='pf'
pessoa3[_ENDERECOS]=pessoa1[_ENDERECOS][0][_RUA]='pocahontas'

print('teste1:', pessoa1.__len__())
print('teste2:', len(pessoa1))
print('teste3:', pessoa1.keys())
for chave in pessoa1.keys():
    print(f"teste4: pessoa1['{chave}']={pessoa1[chave]}")
print("")
print('----Testando pessoa1')
for chave, valor in pessoa1.items():
    print(f'teste5: {chave}={valor}')

print("")
print('----Testando pessoa2')
for chave, valor in pessoa2.items():
    print(f'teste6: {chave}={valor}')

print("")
print('----Testando pessoa3')
for chave, valor in pessoa3.items():
    print(f'teste7: {chave}={valor}')

"""
Exibe ao executar:

teste1: 8
teste2: 8
teste3: dict_keys(['nome', 'sobrenome', 'profissao', 'idade', 'altura', 'enderecos', 'id', 'tipo'])
teste4: pessoa1['nome']=Edivaldo
teste4: pessoa1['sobrenome']=Ribeiro
teste4: pessoa1['profissao']=Programador
teste4: pessoa1['idade']=60
teste4: pessoa1['altura']=1.72
teste4: pessoa1['enderecos']=[{'rua': 'pocahontas', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]
teste4: pessoa1['id']=1
teste4: pessoa1['tipo']=pf

----Testando pessoa1
teste5: nome=Edivaldo
teste5: sobrenome=Ribeiro
teste5: profissao=Programador
teste5: idade=60
teste5: altura=1.72
teste5: enderecos=[{'rua': 'pocahontas', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]
teste5: id=1
teste5: tipo=pf

----Testando pessoa2
teste6: nome=Edivaldo
teste6: sobrenome=Ribeiro
teste6: profissao=Programador
teste6: idade=60
teste6: altura=1.72
teste6: enderecos=ponhangaba
teste6: id=2
teste6: tipo=pj

----Testando pessoa3
teste7: nome=Edivaldo
teste7: sobrenome=Ribeiro
teste7: profissao=Programador
teste7: idade=60
teste7: altura=1.72
teste7: enderecos=pocahontas
teste7: id=3
teste7: tipo=pf
"""
