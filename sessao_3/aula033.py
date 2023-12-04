nome1='edivaldo ribeiro'
nome2=nome1
print(f'Id para nome1={id(nome1)} Id para nome2={id(nome2)}')

nome2=nome1.capitalize()
print(f'Id para nome1={id(nome1)} Id para nome2={id(nome2)} - {nome2}')

"""
Exibe ao executar:

Id para nome1=140196201917424 Id para nome2=140196201917424
Id para nome1=140196201917424 Id para nome2=140196201920816 - Edivaldo ribeiro
"""
