import pprint

def p(v, seq):
    print('')
    print(f'---Teste{seq}----------')
    pprint.pprint(v, sort_dicts=False, width=60)

lista=[]
for x in range(3):
    for y in range(3):
        lista.append((x,y))
p(lista, 1)

lista2=[(x,y) 
        for x in range(3) 
        for y in range(3)]
p(lista2, 2)

"""
Exibe ao executar:


---Teste1----------
[(0, 0),
 (0, 1),
 (0, 2),
 (1, 0),
 (1, 1),
 (1, 2),
 (2, 0),
 (2, 1),
 (2, 2)]

---Teste2----------
[(0, 0),
 (0, 1),
 (0, 2),
 (1, 0),
 (1, 1),
 (1, 2),
 (2, 0),
 (2, 1),
 (2, 2)]
"""
