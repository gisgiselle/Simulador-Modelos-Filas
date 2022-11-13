def validate_lambda(lmbda, s, miu):
    if lmbda >= (s * miu):
        print("la tasa de llegadas o lambda: "+str(lmbda) +" es menor o igual a la multiplicacion del numero de servidores: "
                                                           "" +str(s)+" y la tasa de servicios o miu: "+str(miu))
        return False
    return True

