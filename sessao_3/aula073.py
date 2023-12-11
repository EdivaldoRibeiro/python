def exibir(msg):
    print(f'-->{msg}')

def exibir_texto(funcao, *args):
    print('----texto-----------------------------------')
    for str in args:
        funcao(str)


print('===========================================')
texto='Bom dia', 'hello word', 'São Paulo','11-nov-2023', '11:27'
exibir_texto(exibir,*texto)

"""
Exibe ao executar:

===========================================
----texto-----------------------------------
-->Bom dia
-->hello word
-->São Paulo
-->11-nov-2023
-->11:27
"""
