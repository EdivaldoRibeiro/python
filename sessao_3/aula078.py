def exibe(lista, seq):
    print('')
    print(f'---Teste{seq}---------------------')
    for str in lista:
        print(f'{str}')

#Teste1
l1=[1,2,3,4,3,2,1,1,2,3,4]
exibe(l1, 1)

#Teste2
s1=set(l1)
l2=list(s1)
print(l1, type(l1))
print(s1, type(s1))
print(l2, type(l2))
exibe(l2,2)

#Teste3
s2=set()
s2.add('Antonio')
s2.add('Josefa')
s2.add('Helio')
exibe(s2, 3)

#Teste4
s3=set()
s3.add('Edivaldo')
s3.add('Ribeiro')
s3.update(('Edivaldo2','Ribeiro2'))
exibe(s3, 4)

#Teste5
s2.clear()
s2.add('Joao')
s2.add('Maria')
s2.add('Jose')
s2.update(('Jose','Tiago'))
exibe(s2, 5)

#Teste6
s2.discard('Joao')
s2.discard('Maria')
exibe(s2, 6)

#Teste7
s1={1,2,3,4,5}
s2={2,4,6}
s3=s1.union(s2)
exibe(s3, 7)

#Teste8
s3=s1 | s2
exibe(s3, 8)

#Teste9
s3=s1.intersection(s2)
exibe(s3, 9)

#Teste10
s3=s1 & s2
exibe(s3, 10)

#Teste11
s3=s1 - s2
exibe(s3, 11)

#Teste12
s3=s2 - s1
exibe(s3, 12)

#Teste13
s3=s1 ^ s2
exibe(s3, 13)

"""
Exibe ao executar:


---Teste1---------------------
1
2
3
4
3
2
1
1
2
3
4
[1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4] <class 'list'>
{1, 2, 3, 4} <class 'set'>
[1, 2, 3, 4] <class 'list'>

---Teste2---------------------
1
2
3
4

---Teste3---------------------
Antonio
Helio
Josefa

---Teste4---------------------
Edivaldo
Edivaldo2
Ribeiro
Ribeiro2

---Teste5---------------------
Maria
Tiago
Joao
Jose

---Teste6---------------------
Tiago
Jose

---Teste7---------------------
1
2
3
4
5
6

---Teste8---------------------
1
2
3
4
5
6

---Teste9---------------------
2
4

---Teste10---------------------
2
4

---Teste11---------------------
1
3
5

---Teste12---------------------
6

---Teste13---------------------
1
3
5
6
"""
