salas=[
    ['Maria', 'Jose', 'Madalena'],
    ['Pedro', 'Tiago', 'Joao'],
    ['Edivaldo', 'Genivaldo', 'Messias']
]

for sala, alunos in enumerate(salas):
    print(f'sala {sala}')
    for aluno, nome in enumerate(alunos):
        print(f'\t{aluno} - {nome}')

"""
Exibe ao executar:
sala 0
        0 - Maria
        1 - Jose
        2 - Madalena
sala 1
        0 - Pedro
        1 - Tiago
        2 - Joao
sala 2
        0 - Edivaldo
        1 - Genivaldo
        2 - Messias
"""
