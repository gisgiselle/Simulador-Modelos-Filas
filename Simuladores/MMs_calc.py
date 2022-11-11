from math import factorial
import pprint

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 0,
    "n": 0,
    "rho": 0.0,
    "pn": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}

# NUMEROS ENTEROS POSITIVOS NO CADENAS

def calcular_Po(tasa_llegadas, tasa_servicios, servidores):
    suma = 0.0
    for i in range(servidores):
        suma += ((tasa_llegadas / tasa_servicios) ** i) / factorial(i)

    po = suma + ((tasa_llegadas / tasa_servicios) ** servidores) / factorial(servidores) * \
                (1/(1-(tasa_llegadas/(servidores * tasa_servicios))))

    po = po ** (-1)
    return po

def calcular_Pn(tasa_llegadas, tasa_servicios, servidores, max_clientes,p0):
    results["n"] = max_clientes
    results["s"] = servidores
    results["p0"] = p0
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    pn = 0
    if results["n"] < results["s"] or results["n"] >= 0:
        pn = ((results["lambda"] / results["miu"]) ** results["n"])\
                        / factorial(results["n"])  * results["p0"]
    elif results["n"] >= results["s"]:
        pn = ((results["lambda"] / results["miu"]) ** results["n"]) \
             / (factorial(results["s"]) * results["s"] ** (results["n"] -
                                                           results["s"])) * results["p0"]
    return pn
def calcular_Lq(tasa_llegadas, tasa_servicios, servidores):
    lq = (results["p0"] * ((tasa_llegadas/tasa_servicios)**servidores) * results["rho"])\
         / (factorial(servidores) * ((1-results["rho"])**2))
    return lq

def calcular(tasa_llegadas, tasa_servicios, servidores,n):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = servidores
    results["n"] = n

    # RO: fact de utilizacion de instalacion
    # del servicio
    results["rho"] = results["lambda"] / (results["s"] * results["miu"])

    #probabilidad de que no haya clientes
    results["p0"] = calcular_Po(results["lambda"], results["miu"], results["s"])

    #probabilidad de que haya n clientes en el sistema
    results["pn"] = calcular_Pn(results["lambda"], results["miu"], results["s"], results["n"], results["p0"])

    #Lq: Promedio de clientes en la cola
    results["Lq"] = calcular_Lq(tasa_llegadas,tasa_servicios,servidores)

    #L: Promedio de clientes en el sistema
    results["L"] = results["Lq"] + (results["lambda"]/results["miu"])

    #Tiempo esperado en la cola
    results["Wq"] = results["Lq"] / results["lambda"]

    #Tiempo promedio en el sistema
    results["W"] = results["Wq"] + (1/results["miu"])

    return results


pprint.pprint(calcular(2,3,2,100))