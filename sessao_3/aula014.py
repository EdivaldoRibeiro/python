a="abacaxi"
b="tomate"
val1=5.5
val2=6.6
val3=7.7
formato1="formato1 a={} b={} val={:.2f}"
formato2="formato2 a={1} b={0} val={2:.2f}"
formato3="formato3 a={1} b={0} val={param3:.2f}"
formatado=formato1.format(a,b,val1)
print(formatado)
formatado=formato1.format(b,a,val2)
print(formatado)
formatado=formato2.format(a,b,val2)
print(formatado)
formatado=formato2.format(b,a,val2)
print(formatado)
formatado=formato3.format(b,a,param3=val3)
print(formatado)

"""
Exibe ao executar:

formato1 a=abacaxi b=tomate val=5.50
formato1 a=tomate b=abacaxi val=6.60
formato2 a=tomate b=abacaxi val=6.60
formato2 a=abacaxi b=tomate val=6.60
formato3 a=abacaxi b=tomate val=7.70
"""
