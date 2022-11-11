#ERRORES NO ENCONTRADOS AUN EN P0

from math import factorial
import pprint

results = {
    "lambda": 0.0,
    "miu": 0.0,
    "s": 0,
    "n":0,
    "k": 0.0,
    "rho": 0.0,
    "pn":0.0,
    "p0": 0.0,
    "Lq": 0.0,
    "lambdaE": 0.0,
    "tasaUtil": 0.0,
    "L": 0.0,
    "Wq": 0.0,
    "W": 0.0,
}

def calcular_pn(lmbda,miu,s,p0, n,k):
    pn = 0
    if n > k:
        part2 = 0

    elif n <= s:
       part2=  (((lmbda / miu) ** n) / factorial(n)) * p0

    elif n > s:
        part2 =(((lmbda / miu) ** n) / (factorial(s) * s ** (n-s))) * p0



    return part2

def calcular_po(lmbda, miu, s, k):
    sum_s = 0
    sum_k = 0
    j = s + 1

    for i in range(j):
        sum_s += ((lmbda / miu) ** i) / factorial(i)

    for j in range(k+1):
        sum_k += (lmbda / s * miu) ** (j - s)

    sum_k = sum_k * ((lmbda / miu) ** s) / factorial(s)

    sum_tot = 1 / (sum_s + sum_k)
    return sum_tot


def calcular_lq(p0, lmbda, miu, s, rho):
    first = p0 * ((lmbda / miu) ** s) * rho / (factorial(s) * (1 - rho) ** 2)
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

    results["rho"] = results["lambda"] / (results["s"] * results["miu"])

    results["p0"] = calcular_po(results["lambda"], results["miu"], results["s"], results["k"])

    results["pn"] = calcular_pn(results["lambda"], results["miu"], results["s"],results["p0"], results["n"], results["k"])


    results["pk"] = ((results["lambda"] / results["miu"]) ** results["k"]) \
                    / (factorial(results["s"]) * (results["s"] ** (results["k"] - results["s"]))) * results["p0"]

    results["Lq"] = calcular_lq(results["p0"], results["lambda"], results["miu"], results["s"], results["rho"])

    results["lambdaE"] = results["lambda"] * (1 - results["pk"])

    results["Wq"] = results["Lq"] / results["lambdaE"]

    results["W"] = results["Wq"] + (1 / results["miu"])

    results["L"] = results["lambdaE"] * results["W"]

    results["tasaUtil"] = 1 - results["p0"]


    #MAKING RESULTS USER FRIENDLY

    return results

print(calcular(2, 3, 1,50,20))
