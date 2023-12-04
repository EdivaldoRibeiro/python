v1='a'
v2='a'
print(f'Identidade de v1={id(v1)} Identidade de v2={id(v2)}')
v2='b'
print(f'Identidade de v1={id(v1)} Identidade de v2={id(v2)}')


condicao=True
flag=None
if condicao:
    print("atende o if")
    flag=True
else:
    print("Nao atendeu o if")

if flag is None:
    print(f'flag none {flag is None}')
else:
    print(f'flag não é none {flag is not None}')

"""
Exibe ao executar:

Identidade de v1=140377976048336 Identidade de v2=140377976048336
Identidade de v1=140377976048336 Identidade de v2=140377976049392
atende o if
flag não é none True
"""
