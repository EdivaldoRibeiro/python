def exibe(lista, seq):
    print('')
    print(f'---Teste{seq}----------')
    for item in lista:
        print(item)

lista=[1,2,3,'hello', 'word', True, False, 1.2, 3.14, ('a','b',1), ['c','d',2], {'e','f',3}]
exibe(lista, 1)

for index, item in enumerate(lista):
    if isinstance(item, bool) and item == True:
        lista[index]='False'
    elif isinstance(item, bool) and item == False:
        lista[index]='True'
    elif isinstance(item, list):
        item.append(3)
    elif isinstance(item, set):
        item.add(4)
    elif isinstance(item, str):
        lista[index]=item.upper()
    elif isinstance(item, int):
        lista[index]=item*10
    elif isinstance(item, float):
        lista[index]=item*1.5

 
exibe(lista, 2)


"""
Exibe ao executar


---Teste1----------
1
2
3
hello
word
True
False
1.2
3.14
('a', 'b', 1)
['c', 'd', 2]
{'f', 3, 'e'}

---Teste2----------
10
20
30
HELLO
WORD
False
True
1.7999999999999998
4.71
('a', 'b', 1)
['c', 'd', 2, 3]
{'f', 3, 4, 'e'}
"""
