nomes=['Edivaldo', 'Helio', 'Janete', 'Gilza']
my_enum=enumerate(nomes)

print("Jeito feio com while")
id, nome=my_enum.__next__()
while True:
    print(f'idx={id:02d} - {nome}')
    try:
        sel=my_enum.__next__()
    except StopIteration:
        break

print("")
print("Jeito bonito com for")
my_enum=enumerate(nomes)
for id, nome in my_enum:
    print(f'idx={id:02d} - {nome}')


print("")
print("Outra maneira de usar o enumerate")
my_enum=enumerate(nomes, start=100)
for id, nome in my_enum:
    print(f'idx={id:03d} - {nome}')

"""
Jeito feio com while
idx=00 - Edivaldo
idx=00 - Edivaldo
idx=00 - Edivaldo
idx=00 - Edivaldo

Jeito bonito com for
idx=00 - Edivaldo
idx=01 - Helio
idx=02 - Janete
idx=03 - Gilza

Outra maneira de usar o enumerate
idx=100 - Edivaldo
idx=101 - Helio
idx=102 - Janete
idx=103 - Gilza

"""
