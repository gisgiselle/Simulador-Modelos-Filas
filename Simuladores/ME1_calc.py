import pprint


results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 0,
    "k": 0.0,
    "rho": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}

def calcular(tasa_llegada, tasa_servicios, k):
    results["lambda"] = tasa_llegada
    results["miu"] = tasa_servicios
    results["k"] = k
    results["s"] = 1

    results["rho"] = results["lambda"] / (results["s"]*results["miu"])

    results["p0"] = 1 - results["rho"]

    results["Lq"] = ((1+results["k"]) / (2 * results["k"])) * (results["lambda"])**2 / \
                    (results["miu"] * (results["miu"]-results["lambda"]))

    results["Wq"] = results["Lq"] / results["lambda"]

    results["W"] = results["Wq"] + (1 / results["miu"])

    results["L"] = results["lambda"] * results["W"]

    return results

pprint.pprint(calcular(3,2,1))