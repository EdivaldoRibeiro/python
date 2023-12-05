nome='Edivaldo Ribeiro'

print("Usando for...")
iterator1=iter(nome)
for caracter in iterator1:
    print(caracter)
print("")
print("Usando while...")
iterator2=iter(nome)
while True:
    try:
        caracter=next(iterator2)
        print(caracter)
    except StopIteration:
        break

"""
Exibe ao executar:

Usando for...
E
d
i
v
a
l
d
o
 
R
i
b
e
i
r
o

Usando while...
E
d
i
v
a
l
d
o
 
R
i
b
e
i
r
o
"""
