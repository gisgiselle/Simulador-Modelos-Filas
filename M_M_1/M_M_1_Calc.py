def calcular_po(fact_util):
    p_o = 1 - fact_util
    return p_o

def calcular(miu, lamb,n):
    #RO: fact de utilizacion de instalacion
    #del servicio
    fact_utilizacion = lamb / miu
    p_o = calcular_po(fact_utilizacion)
    p_n = (fact_utilizacion ** n) * p_o



calcular(3,2)