import pprint
from math import factorial

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "rho": 0.0,
    "pn": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0
}
def calcular(tasa_servicios, tasa_llegadas,n):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = 1
    # RO: fact de utilizacion de instalacion
    # del servicio
    results["rho"] = tasa_llegadas / (results["s"]*results["miu"])

    results["p0"] = 1 - results["rho"]

    #Probabilidad de n clientes en la cola
    results["pn"] = (1 - results["rho"])*results["rho"]**n

    #Lq: Promedio de clientes en la cola
    results["Lq"] = (tasa_llegadas ** 2) / (tasa_servicios * (tasa_servicios - tasa_llegadas))
    #Promedio de clientes en el sistema
    results["L"] = tasa_llegadas / (tasa_servicios - tasa_llegadas)
    #Tiempo esperado en la cola
    results["Wq"] = results["Lq"] / tasa_llegadas
    #Tiempo promedio en el sistema
    results["W"] = results["L"] / tasa_llegadas

    return results

