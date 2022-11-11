def validate_lambda(lmbda, s, miu):
    if lmbda >= (s * miu):
        print("la tasa de llegadas o lambda: "+str(lmbda) +" es menor o igual a la multiplicacion del numero de servidores: "
                                                           "" +str(s)+" y la tasa de servicios o miu: "+str(miu))
    return "Por favor valida tus datos ingresados"

#validate_lambda(2,1,1)