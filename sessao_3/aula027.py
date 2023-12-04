nome="Edivaldo Ribeiro"
length=len(nome)
print(f'de [{nome}] obter substring depois do indice 0 ate 8 salto 1    [{nome[0:8]}]')
print(f'de [{nome}] obter substring depois do indice 9 salto 1          [{nome[9:]}]')
print(f'de [{nome}] obter substring depois do indice 7 ate {length} salto 1   [{nome[7:10]}]')
print(f'de [{nome}] obter substring depois do indice 0 ate {length} salto 1   [{nome[::1]}]')
print(f'de [{nome}] obter substring depois do indice 0 ate {length} salto 2   [{nome[::2]}]')
print(f'de [{nome}] obter substring depois do indice 0 ate {length} invertido [{nome[::-1]}]')


"""
Exibe ao executar:

de [Edivaldo Ribeiro] obter substring depois do indice 0 ate 8 salto 1    [Edivaldo]
de [Edivaldo Ribeiro] obter substring depois do indice 9 salto 1          [Ribeiro]
de [Edivaldo Ribeiro] obter substring depois do indice 7 ate 16 salto 1   [o R]
de [Edivaldo Ribeiro] obter substring depois do indice 0 ate 16 salto 1   [Edivaldo Ribeiro]
de [Edivaldo Ribeiro] obter substring depois do indice 0 ate 16 salto 2   [Eiad ier]
de [Edivaldo Ribeiro] obter substring depois do indice 0 ate 16 invertido [oriebiR odlavidE]
"""
