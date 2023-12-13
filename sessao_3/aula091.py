def generator1(n=0):
    yield 1
    print('continuando 1')
    yield 2
    print('continuando 2')
    yield 3
    print('Terminou...')

def generator2(n=0, maximum=15):
    seq=0
    while seq<maximum:
        yield seq
        seq+=1
    
gen=generator1(n=0)

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print('Acabou, não insista...')

print()
print('Exemplo usando for - generator1')
gen=generator1(n=0)
for n in gen:
    print(f'-->{n}')

print()
print('Exemplo usando for - generator2')
gen=generator2(n=0)
for n in gen:
    print(f'-->{n}')

"""
Exibe ao executar:

1
continuando 1
2
continuando 2
3
Terminou...
Acabou, não insista...

Exemplo usando for - generator1
-->1
continuando 1
-->2
continuando 2
-->3
Terminou...

Exemplo usando for - generator2
-->0
-->1
-->2
-->3
-->4
-->5
-->6
-->7
-->8
-->9
-->10
-->11
-->12
-->13
-->14
"""
