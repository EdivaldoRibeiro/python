lista=['Maria', 'Jose', 1,2,3,4,5,'Moises','Tiago']

primeiro, *_, penultimo, ultimo=lista
print(f'primeiro={primeiro} - penultimo:{penultimo} - último={ultimo}')

for str in lista:
    print(str, end='_')

print("")
print('lista:', *lista)

eu='Edivaldo'
print('eu:', *eu)

tupla='Edivaldo Ribeiro'
print('tupla:', *tupla)

salas=[
    ['Maria', 'Jose', 'Madalena'],
    ['Pedro', 'Tiago', 'Joao'],
    ['Edivaldo', 'Genivaldo', 'Messias']
]

print(*salas, sep='\n')

"""
Exibe ao executar:

primeiro=Maria - penultimo:Moises - último=Tiago
Maria_Jose_1_2_3_4_5_Moises_Tiago_
lista: Maria Jose 1 2 3 4 5 Moises Tiago
eu: E d i v a l d o
tupla: E d i v a l d o   R i b e i r o
['Maria', 'Jose', 'Madalena']
['Pedro', 'Tiago', 'Joao']
['Edivaldo', 'Genivaldo', 'Messias']
"""
