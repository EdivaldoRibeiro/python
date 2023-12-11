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

def exibe(estrutura):
    print("")
    for chave in estrutura.keys():
        print(f"'{chave}'={estrutura[chave]}")


exibe(pessoa1)

#remove da estrutura
enderecos=pessoa1.pop(_ENDERECOS)
exibe(pessoa1)
print(f'removeu {enderecos}')

#remove última chave
altura=pessoa1.popitem()
exibe(pessoa1)
print(f'removeu última chave {altura}')

#update da profissao
pessoa1.update({_PROFISSAO:'PROGRAMADOR SENIOR'})
exibe(pessoa1)

#recriando altura
pessoa1.update({_ALTURA: 1.721})
exibe(pessoa1)

#outro jeito de update
pessoa1.update(altura=1.72,profissao='COBOLEIRO')
exibe(pessoa1)

#update usando tupla
tupla=(_ALTURA, 1.722),(_PROFISSAO,'C/C++')
pessoa1.update(tupla)
exibe(pessoa1)

#update usando lista
lista=[[_ALTURA, 1.72],[_PROFISSAO,'PL/SQL']]
pessoa1.update(lista)
exibe(pessoa1)

"""
Exibe ao executar:


'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=Programador
'idade'=60
'altura'=1.72
'enderecos'=[{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=Programador
'idade'=60
'altura'=1.72
removeu [{'rua': 'tucumare', 'numero': 100}, {'rua': 'tucumare2', 'numero': 101}]

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=Programador
'idade'=60
removeu última chave ('altura', 1.72)

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=PROGRAMADOR SENIOR
'idade'=60

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=PROGRAMADOR SENIOR
'idade'=60
'altura'=1.721

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=COBOLEIRO
'idade'=60
'altura'=1.72

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=C/C++
'idade'=60
'altura'=1.722

'nome'=Edivaldo
'sobrenome'=Ribeiro
'profissao'=PL/SQL
'idade'=60
'altura'=1.72
"""
