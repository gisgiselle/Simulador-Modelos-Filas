#ERRORES NO ENCONTRADOS AUN EN P0

from math import factorial
import pprint

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 0,
    "n": 0,
    "k": 0.0,
    "rho": 0.0,
    "pn": 0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "lambdaE": 0.0,
    "tasaUtil": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}



def calcular_po(tasa_servicios, tasa_llegadas, s, k):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = s
    results["k"] = k

    sum_s = 0
    sum_k = 0
    j = s + 1

    for i in range(j):
        sum_s += ((results["lambda"] / results["miu"]) ** i) / factorial(i)

    for j in range(results["k"]+1):
        sum_k += (results["lambda"] / results["s"] * results["miu"]) ** (j - s)

    sum_k = sum_k * ((results["lambda"] / results["miu"]) ** results["s"]) / factorial(s)

    sum_tot = 1 / (sum_s + sum_k)
    return sum_tot


def calcular_pn(tasa_servicios, tasa_llegadas, s, n, k):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["n"] = n
    results["s"] = s
    results["k"] = k

    if results["n"] > results["k"]:
        part2 = 0

    elif results["n"] <= results["s"]:
        part2 = (((results["lambda"] / results["miu"]) ** results["n"]) / factorial(results["n"])) * results["p0"]

    elif results["n"] > results["s"]:
        part2 = (((results["lambda"] / results["miu"]) ** results["n"]) /
                 (factorial(s) * results["s"] ** (results["n"] - results["s"]))) * results["p0"]

    return part2

def calcular_lq(tasa_servicios, tasa_llegadas, s):
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = s

    results["rho"] = results["lambda"] / (results["s"] * results["miu"])
    first = results["p0"] * ((results["lambda"] / results["miu"]) ** results["s"]) * results["rho"] / (factorial(results["s"]) * (1 - results["rho"]) ** 2)
    second = 1 - ((2 / 3) ** 2) - (2 * ((2 / 3) ** 2)) * (1 - (2 / 3))

    return first * second


def calcular(tasa_llegadas, tasa_servicios, servidores, max_clientes,n):
    if servidores > max_clientes:
        print("Los servidores deben ser menores o iguales al maximo de clientes")
        return
    results["lambda"] = tasa_llegadas
    results["miu"] = tasa_servicios
    results["s"] = servidores
    results["k"] = max_clientes
    results["n"] = n

    results["p0"] = calcular_po(results["lambda"], results["miu"], results["s"], results["k"])

    results["pn"] = calcular_pn(results["lambda"], results["miu"], results["s"],results["n"], results["k"])


    results["pk"] = ((results["lambda"] / results["miu"]) ** results["k"]) \
                    / (factorial(results["s"]) * (results["s"] ** (results["k"] - results["s"]))) * results["p0"]

    results["Lq"] = calcular_lq(results["lambda"], results["miu"], results["s"])

    results["lambdaE"] = results["lambda"] * (1 - results["pk"])

    results["Wq"] = results["Lq"] / results["lambdaE"]

    results["W"] = results["Wq"] + (1 / results["miu"])

    results["L"] = results["lambdaE"] * results["W"]

    results["tasaUtil"] = 1 - results["p0"]

    return results

