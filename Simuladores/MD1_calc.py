import pprint

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 1,
    "rho": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}

def calcular(tasa_llegadas,tasa_servicios):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios

    results["rho"] = results["lambda"] / results["s"]*results["miu"]

    results["p0"] = 1 - results["rho"]

    results["Lq"] = (results["rho"] ** 2) / (2 * (1 - results["rho"]))

    results["L"] = results["rho"]  + results["Lq"]
    results["Wq"] = (results["rho"]**2) / ((2 * results["lambda"])*(1-results["rho"]))

    results["W"] = results["Wq"] + (1 / results["miu"])


    return results

pprint.pprint(calcular(3,2))