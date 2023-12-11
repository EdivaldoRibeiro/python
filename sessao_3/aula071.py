x,y,*args=1,2,3,4,5,6,7,8,9,10
print(x,y,args)

def soma(*args):
    total=0.0
    for val in args:
        calc=total+val
        print(f'{val:.02f} + {total:.02f} = {calc:.02f}')
        total=calc
    return total

numeros=1,2,3,4,5,6
print(f'retornou {soma(*numeros):.02f}')

#Usando função nativa do python
somando=sum(numeros)
print(f'retorno da função nativa python {somando:05d}')

"""
Exibe ao executar:

1 2 [3, 4, 5, 6, 7, 8, 9, 10]
1.00 + 0.00 = 1.00
2.00 + 1.00 = 3.00
3.00 + 3.00 = 6.00
4.00 + 6.00 = 10.00
5.00 + 10.00 = 15.00
6.00 + 15.00 = 21.00
retornou 21.00
retorno da função nativa python 00021
"""
