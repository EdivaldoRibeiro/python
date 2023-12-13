def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    if gen is not None:
        yield from gen1()
    yield 4
    yield 5
    yield 6

def gen3(gen=None):
    if gen is not None:
        yield from gen()
    yield 41
    yield 51
    yield 61

print('Teste gen1()')
gen=gen1()
for n in gen:
    print(n)

print()
print('Teste gen2')
gen=gen2()
for n in gen:
    print(n)

print()
print('Teste gen3')
gen=gen3(gen1)
for n in gen:
    print(n)

print()
print('Teste gen4')
gen=gen3(gen2)
for n in gen:
    print(n)

"""
Exibe ao executar:

Teste gen1()
1
2
3

Teste gen2
4
5
6

Teste gen3
1
2
3
41
51
61

Teste gen4
4
5
6
41
51
61
"""
