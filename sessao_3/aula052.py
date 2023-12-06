#Tuplas são listas imutáveis
nomes='Edivaldo', 'Joao', 'Maria'

for str in nomes:
    print(f'-->{str}')

print(nomes)

print("")
print("Convertendo uma lista numa tupla")
cidades=['Maua', 'Curitiba', 'Juazeiro']

t_cidades=tuple(cidades)
for str in t_cidades:
    print(f'-->{str}')

print("")
print("Convertendo uma tupla para lista")
t_paises=['Brasil', 'Rusia', 'India', 'China', 'South Africa']

paises=list(t_paises)
for str in t_paises:
    print(f'-->{str}')

"""
Exibe ao executar:
-->Edivaldo
-->Joao
-->Maria
('Edivaldo', 'Joao', 'Maria')

Convertendo uma lista numa tupla
-->Maua
-->Curitiba
-->Juazeiro

Convertendo uma tupla para lista
-->Brasil
-->Rusia
-->India
-->China
-->South Africa
"""
