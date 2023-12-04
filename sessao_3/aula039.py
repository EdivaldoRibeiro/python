nome='Edivaldo Ribeiro'
size=len(nome)
idx=0
while idx<size:
    caracter=nome[idx]
    v_asc=ord(caracter) # Devolve o valor correspondente em ASCII
    print(f'{caracter} - ascii={v_asc:03d} hexa={v_asc:2x}')
    idx+=1

idx=0
novo_nome=''
while idx<size:
    novo_nome=novo_nome+nome[idx]+"_"
    idx+=1
print(f'Novo nome: {novo_nome}')

"""
Exibe ao executar:

E - ascii=069 hexa=45
d - ascii=100 hexa=64
i - ascii=105 hexa=69
v - ascii=118 hexa=76
a - ascii=097 hexa=61
l - ascii=108 hexa=6c
d - ascii=100 hexa=64
o - ascii=111 hexa=6f
  - ascii=032 hexa=20
R - ascii=082 hexa=52
i - ascii=105 hexa=69
b - ascii=098 hexa=62
e - ascii=101 hexa=65
i - ascii=105 hexa=69
r - ascii=114 hexa=72
o - ascii=111 hexa=6f
Novo nome: E_d_i_v_a_l_d_o_ _R_i_b_e_i_r_o_
"""
