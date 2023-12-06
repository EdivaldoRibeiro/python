nomes=['Joao','Maria','Jose','Leopoldina']

print("Nomes inicial")
for str in nomes:
    print(f'-->{str}')

nome1, nome2, nome3, nome4 = nomes
print(f'-nome1={nome1}')
print(f'-nome2={nome2}')
print(f'-nome3={nome3}')
print(f'-nome4={nome4}')

print("")
print("Novos nomes")
nomes.clear()
nomes.append('Edivaldo')
nomes.append('Helio')
nomes.append('Gedalva')
nomes.append('Creusa')
for str in nomes:
    print(f'-->{str}')

nome1, nome2, *resto = nomes
print(f'-nome1={nome1}')
print(f'-nome2={nome2}')
print(f'-resto={resto}')

print("")
print("Novo jeito")
_, nome2, *resto = nomes
print(f'-nome2={nome2}')
print(f'-resto={resto}')

print("")
print("Outro jeito")
_, _, _, nome4, *resto = nomes
print(f'-nome4={nome4}')
print(f'-resto={resto}')

"""
Exibe ao executar:

Nomes inicial
-->Joao
-->Maria
-->Jose
-->Leopoldina
-nome1=Joao
-nome2=Maria
-nome3=Jose
-nome4=Leopoldina

Novos nomes
-->Edivaldo
-->Helio
-->Gedalva
-->Creusa
-nome1=Edivaldo
-nome2=Helio
-resto=['Gedalva', 'Creusa']

Novo jeito
-nome2=Helio
-resto=['Gedalva', 'Creusa']

Outro jeito
-nome4=Creusa
-resto=[]
"""
