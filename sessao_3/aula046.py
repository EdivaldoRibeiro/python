LINHAS=10
COLUNAS=3
ABORTAR=(LINHAS-2)+2

for linha in range(LINHAS):
    if linha in (2,4,6,7):
        print(f"Saltando linha {linha}...")
        continue
    
    for coluna in range(1,4):
        if coluna % 2 == 0:
            continue
        
        pos=linha*LINHAS+coluna
        print(f'linha={linha} coluna={coluna} calculando posicao={pos}')
else:
    print("Terminou o for...")

"""
Exibe ao executar:

linha=0 coluna=1 calculando posicao=1
linha=0 coluna=3 calculando posicao=3
linha=1 coluna=1 calculando posicao=11
linha=1 coluna=3 calculando posicao=13
Saltando linha 2...
linha=3 coluna=1 calculando posicao=31
linha=3 coluna=3 calculando posicao=33
Saltando linha 4...
linha=5 coluna=1 calculando posicao=51
linha=5 coluna=3 calculando posicao=53
Saltando linha 6...
Saltando linha 7...
linha=8 coluna=1 calculando posicao=81
linha=8 coluna=3 calculando posicao=83
linha=9 coluna=1 calculando posicao=91
linha=9 coluna=3 calculando posicao=93
Terminou o for...
"""
