from Simuladores.MDs_calc import calcular as md1_calc
from Simuladores.MEk1_calc import calcular as me1_calc
from Simuladores.MM1_calc import calcular as mm1_calc
from Simuladores.MMG1_calc import calcular as mmg1_calc
from Simuladores.MMs_calc import calcular as mms_calc
from Simuladores.MMsK_calc import calcular as mmsk_calc

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
    print(md1_calc(1, 2))
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

