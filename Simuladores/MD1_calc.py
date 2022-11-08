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

    results["rho"] = results["lambda"] / results["miu"]

    results["p0"] = 1 - results["rho"]

    results["Lq"] = (results["rho"] ** 2) / (2 * (1 - results["rho"]))

    results["Wq"] = results["Lq"] / results["lambda"]

    results["W"] = results["Wq"] + (1 / results["miu"])

    return results
