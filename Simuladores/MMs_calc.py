from math import factorial

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 0,
    "rho": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}


def calcular_Po(tasa_llegadas, tasa_servicios, servidores):
    suma = 0.0
    for i in range(servidores):
        suma += ((tasa_llegadas / tasa_servicios) ** i) / factorial(i)

    po = suma + ((tasa_llegadas / tasa_servicios) ** servidores) / factorial(servidores) * \
                (1/(1-(tasa_llegadas/(servidores * tasa_servicios))))

    po = po ** (-1)
    return po

def calcular_Lq(tasa_llegadas, tasa_servicios, servidores):
    lq = (results["p0"] * ((tasa_llegadas/tasa_servicios)**servidores) * results["rho"])\
         / (factorial(servidores) * ((1-results["rho"])**2))
    return lq

def calcular(tasa_llegadas, tasa_servicios, servidores):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = servidores

    # RO: fact de utilizacion de instalacion
    # del servicio
    results["rho"] = results["lambda"] / (results["s"] * results["miu"])
    if(results["rho"] > 1):
        print(" rho: "+str(results["rho"]) + " > " + "1")
        return "Condicion de estado no estable, verifique sus datos!!!!!!!!"

    results["p0"] = calcular_Po(results["lambda"], results["miu"], results["s"])

    #Lq: Promedio de clientes en la cola
    results["Lq"] = calcular_Lq(tasa_llegadas,tasa_servicios,servidores)

    #L: Promedio de clientes en el sistema
    results["L"] = results["Lq"] + (results["lambda"]/results["miu"])

    #Tiempo esperado en la cola
    results["Wq"] = results["Lq"] / results["lambda"]

    #Tiempo promedio en el sistema
    results["W"] = results["Wq"] + (1/results["miu"])

    return results

#print(calcular(100,60,2))