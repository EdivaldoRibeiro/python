import sys

iterable=['Nem','por','serem','descendência','de','Abraão']
iter1=iterable.__iter__()
iter2=iter(iterable)

item=next(iter1)
while item:
    print(item)
    try:
        item=next(iter1)
    except StopIteration:
        break

lista = [ n for n in range(1000)]
generator = ( n for n in range(1000))

print(f'Tamanho em memoria de lista={sys.getsizeof(lista)}')
print(f'Tamanho em memoria de lista={sys.getsizeof(generator)}')

"""
Exibe ao executar:

Nem
por
serem
descendência
de
Abraão
Tamanho em memoria de lista=8856
Tamanho em memoria de lista=192
"""
