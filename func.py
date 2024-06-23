""" O sinal 4 a 20 mA 
você deve informar qual é o percentual dentre 
o intervalo 4 a 20
"""

def sinalQuatroV(a,b, c,d,e,f,g):
    vl1 = (a - b) 
    vl2 = vl1 * g
    vl3 = ((e - f )* (c-d)) 
    sinal =  ((vl3 + vl2) / vl1)
    return sinal 
    

def calcularPercnetual(a,b,c,d,e):
    vl1 = a*d
    vl2 = a * e
    perc =( vl2 - vl1) / (b-c)   
    return perc
    