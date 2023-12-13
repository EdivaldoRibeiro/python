lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not value else 'truthy'

def exibe(valor, titulo):
    print(f'{titulo:.<12}: {valor}')

exibe('TESTE','TESTE')
exibe(lista, 'lista')
exibe(dicionario, 'dicionario')
exibe(conjunto, 'conjunto')
exibe(tupla,'tupla')
exibe(string, 'string')
exibe(inteiro, 'inteiro')
exibe(flutuante, 'flutuante')
exibe(nada, 'nada')
exibe(falso, 'falso')
exibe(intervalo, 'intervalo')

"""
Exibe ao executar:

TESTE.......: TESTE
lista.......: []
dicionario..: {}
conjunto....: set()
tupla.......: ()
string......: 
inteiro.....: 0
flutuante...: 0.0
nada........: None
falso.......: False
intervalo...: range(0, 0)
"""
