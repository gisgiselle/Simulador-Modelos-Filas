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
    "sigma":0.0
}

#QUE ES SIGMA??
def calcular(tasa_servicios, tasa_llegadas, sigma):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["sigma"] = sigma
    results["s"] = 1

    results["rho"] = results["lambda"] / results["s"]*results["miu"]

    results["p0"] = 1-results["rho"]

    results["Lq"] = ((results["lambda"]**2)*results["sigma"]**2) + (results["rho"]**2) / (2 * (1-results["rho"]))

    results["L"] = results["rho"] + results["Lq"]

    results["Wq"] = results["Lq"] / results["lambda"]

    results["W"] = results["Wq"] + (1/results["miu"])

    return results

