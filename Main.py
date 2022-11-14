from Simuladores.MD1_calc import calcular as md1_calc
from Simuladores.MEks_calc import calcular as meks_calc
from Simuladores.MDs_calc import calcular as mds_calc
from Simuladores.MEk1_calc import calcular as mek1_calc
from Simuladores.MM1_calc import calcular as mm1_calc
from Simuladores.MG1 import calcular as mg1_calc
from Simuladores.MMs_calc import calcular as mms_calc
from Simuladores.MMsK_calc import calcular as mmsk_calc
from Validaciones.Lambda_validation import validate_lambda as validarLambda
from Validaciones.int_float_validation import inputFloat as validar_float
from Validaciones.int_float_validation import inputInt as validar_int




opt = ''

while opt != '8':
    menu = """
    Bienvenido al simulador de modelos de filas de espera

    A continuacion seleccione el modelo que desea utilizar:

    1. M/D/1
    2. M/Ek/1
    3. M/Ek/s
    4. M/M/1
    5. M/G/1
    6. M/M/s  
    7. M/M/s/K
    8. Salir del programa

    """
    print(menu)

    opt = input('Ingresa una opcion: ')

    if opt == '1':
        print("****** CALCULANDO M/D/1 ******")
        inputUsuariol = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuariol)

        if not l:
            while not l:
                inputUsuariol = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
                l = validar_float(inputUsuariol)
            else:
                l = True

        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)

        if not m:
            while not m:
                inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
                m = validar_float(inputUsuario)
            else:
                m = True
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)
        s = 1

        if validarLambda(l, s, m):
            md1_calc(l, m, n)

    elif opt == '2':
        print("****** CALCULANDO M/Ek/1 ******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuarioK = input("Ingresa el grado de variabilidad de los tiempos de servicio o K con un numero entero (ejemplo:10): ")
        k = validar_int(inputUsuarioK)
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)
        s = 1
        if validarLambda(l, s, m):
            mek1_calc(l, m, k, n)
    elif opt == '3':
        print("****** CALCULANDO M/Ek/s******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuarioK = input(
            "Ingresa el grado de variabilidad de los tiempos de servicio o K con un numero entero (ejemplo:10): ")
        k = validar_int(inputUsuarioK)
        inputUsuarioS = input("Ingresa el numero de servidores s con un numero entero (ejemplo:2): ")
        s = validar_int(inputUsuarioS)
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)

        if validarLambda(l, s, m):
            meks_calc(l, m, k, s,n)

    elif opt == '4':
        print("****** CALCULANDO M/M/1 ******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)
        s = 1
        if validarLambda(l, s, m):
            mm1_calc(m,l,n)


    elif opt == '5':
        print("****** CALCULANDO M/G/1 ******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuarioSig = input("Ingresa la desviacion estandar sigma con decimales (ejemplo 1.0): ")
        sig = validar_float(inputUsuarioSig)
        s = 1
        if validarLambda(l, s, m):
            mg1_calc(m, l, sig)

    elif opt == '6':
        print("****** CALCULANDO M/M/s   ******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuarios = input("Ingresa el numero de servidores s con un numero entero (ejemplo:4 ): ")
        s = validar_int(inputUsuarios)
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)
        if validarLambda(l, s, m):
            mms_calc(l,m,s,n)

    elif opt == '7':
        print("****** CALCULANDO M / M / s / K   ******")
        inputUsuario = input("Ingresa la tasa de llegadas o lambda con decimales (ejemplo 1.0): ")
        l = validar_float(inputUsuario)
        inputUsuario = input("Ingresa la tasa de servicios o miu con decimales (ejemplo 1.0): ")
        m = validar_float(inputUsuario)
        inputUsuarios = input("Ingresa el numero de servidores s con un numero entero DEBEN SER MENORES O IGUALES AL NUMERO DE CLIENTES MAXIMO K  (ejemplo:4 ): ")
        s = validar_int(inputUsuarios)
        inputUsuarioK = input("Ingresa el numero maximo clientes k con un numero entero (ejemplo:500): ")
        k = validar_int(inputUsuarioK)
        inputUsuario2 = input("Ingresa el numero de clientes n con un numero entero (ejemplo:500): ")
        n = validar_int(inputUsuario2)
        if validarLambda(l, s, m):
            mmsk_calc(l, m, s,k, n)


    elif opt =='8':
        print("Gracias por usar el programa!")
        exit()

    else:
        print('ERROR Ingresa una opcion valida')
        print('=-=' * 20)
