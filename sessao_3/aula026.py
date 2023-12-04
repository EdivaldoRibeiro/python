valor="ABC"
print(f'original:{valor} LDAP com espacos (10 caracteres) a esquerda [{valor: >10}]')
print(f'original:{valor} LDAP com pontos  (10 caracteres) a esquerda [{valor:.>10}]')
print(f'original:{valor} RDAP com espaços (10 caracteres) a direita  [{valor: <10}]')
print(f'original:{valor} RDAP com pontos  (10 caracteres) a direita  [{valor:.<10}]')
print(f'original:{valor} CENTRO com espacos (10 caracteres)          [{valor: ^10}]')
print(f'original:{valor} CENTRO com pontos (10 caracteres)           [{valor:.^10}]')
number=-1778.8917170
print(f'numero:{number} LDAP com zeros (15 caracteres) a esquerda [{number:0>-15,.2f}]')
print(f'numero:{number} LDAP com zeros (15 caracteres) a direita  [{number:0<+15,.2f}]')
print(f'numero:{number} LDAP com zeros (15 caracteres) corrindo   [{number:0=+15,.2f}]')


"""
Exibe ao executar:

original:ABC LDAP com espacos (10 caracteres) a esquerda [       ABC]
original:ABC LDAP com pontos  (10 caracteres) a esquerda [.......ABC]
original:ABC RDAP com espaços (10 caracteres) a direita  [ABC       ]
original:ABC RDAP com pontos  (10 caracteres) a direita  [ABC.......]
original:ABC CENTRO com espacos (10 caracteres)          [   ABC    ]
original:ABC CENTRO com pontos (10 caracteres)           [...ABC....]
numero:-1778.891717 LDAP com zeros (15 caracteres) a esquerda [000000-1,778.89]
numero:-1778.891717 LDAP com zeros (15 caracteres) a direita  [-1,778.89000000]
numero:-1778.891717 LDAP com zeros (15 caracteres) corrindo   [-000,001,778.89]
"""
