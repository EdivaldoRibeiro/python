def confere(variavel, metodo):
    if hasattr(variavel, metodo):
        print(f'"{nome}" tem o método lower() - "{getattr(variavel, metodo)()}"')
    else:
        print(f'"{nome}" nao tem o método {metodo}')

nome='   Edivaldo Ribeiro  '

confere(nome, 'lower')
confere(nome, 'upper')
confere(nome, 'lower1')
confere(nome, 'strip')

"""
Exibe ao executar:

"   Edivaldo Ribeiro  " tem o método lower() - "   edivaldo ribeiro  "
"   Edivaldo Ribeiro  " tem o método lower() - "   EDIVALDO RIBEIRO  "
"   Edivaldo Ribeiro  " nao tem o método lower1
"   Edivaldo Ribeiro  " tem o método lower() - "Edivaldo Ribeiro"
"""
