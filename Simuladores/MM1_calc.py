

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "ro": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}
def calcular(tasa_servicios, tasa_llegadas):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    # RO: fact de utilizacion de instalacion
    # del servicio
    results["ro"] = tasa_llegadas / tasa_servicios
    results["p0"] = 1 - results["ro"]
    #Lq: Promedio de clientes en la cola
    results["Lq"] = (tasa_llegadas ** 2) / (tasa_servicios * (tasa_servicios - tasa_llegadas))
    #Promedio de clientes en el sistema
    results["L"] = tasa_llegadas / (tasa_servicios - tasa_llegadas)
    #Tiempo esperado en la cola
    results["Wq"] = results["Lq"] / tasa_llegadas
    #Tiempo promedio en el sistema
    results["W"] = results["L"] / tasa_llegadas

    return results

print(calcular(3,2))