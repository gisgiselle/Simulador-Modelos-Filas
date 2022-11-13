from Simuladores.MDs_calc import calcular as md1_calc
from Simuladores.ME1_calc import calcular as me1_calc
from Simuladores.MM1_calc import calcular as mm1_calc
from Simuladores.MMG1_calc import calcular as mmg1_calc
from Simuladores.MMs_calc import calcular as mms_calc
from Simuladores.MMsK_calc import calcular as mmsk_calc
from Validaciones.Lambda_validation import validate_lambda as validarLambda
from Validaciones.int_float_validation import inputFloat as validar1
from Validaciones.int_float_validation import inputInt as validar2

menu = """
Bienvenido al simulador de modelos de filas de espera

A continuacion seleccione el modelo que desea utilizar:

1. M/D/1
2. M/E/1
3. M/M/1
4. M/M/G/1
5. M/M/s  
6. M/M/s/K
7. Salir del programa

"""
print(menu)

opt = input('Ingresa una opcion: ')

if opt == '1':
    print("Porfavor dame el valor de lambda (double):" )
    inputUsuario = input()
    print(validar1(inputUsuario))
    l = validar1(inputUsuario)
    print("Dame un valor entero: ")
    inputUsuario2 = input()
    print(validar2(inputUsuario2))
    m = validar2(inputUsuario2)
    print("Dame un valor entero: ")
    inputUsuario2 = input()
    print(validar2(inputUsuario2))
    s = validar2(inputUsuario2)
    print("Porfavor dame el valor de rho (double):" )
    inputUsuario = input()
    print(validar1(inputUsuario))
    r = validar1(inputUsuario)
    print(l, m, s, r)
    print(md1_calc(l, m, s, r))
elif opt == '2':
    print(me1_calc(3, 2, 1))
elif opt == '3':
    print(mm1_calc(5, 2))
elif opt == '4':
    print(mmg1_calc(3, 2, 5))
elif opt == '5':
    print(mms_calc(2, 3, 2, 100))
elif opt == '6':
    print(mmsk_calc(2, 3, 1, 50, 20))
elif opt == '7':
    exit()
else:
    print('ERROR Ingresa una opcion valida')
    print('=-=' * 20)

