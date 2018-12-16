from Resultado import Resultado
from Simulacion import Simulacion
import Operaciones
import os
import shutil

mayoresGanancias = []

def CalculoSimulacion(rangoIni, rangoFinal, iteraciones):
    for i in range(1, iteraciones+1):
        simulacion = Simulacion(i)
        for mes in range(1,31):
            for revista in range(rangoIni, rangoFinal+1):
                for compra in range(4,9):
                    resultado = Resultado(mes, revista, compra)
                    simulacion.AgregarResultado(resultado)

        simulacion.Imprimir()
        mayoresGanancias.append(simulacion.Get_GananciaMayor())

    Operaciones.ImprimirGanancias(mayoresGanancias)

def IniciarPrograma():
    try:
        print('Simulacion de la tercera política, desde el numero inicial de revistas x hasta y: \n')
        iteraciones = int(input('Ingrese el número de simulaciones que deseas realizar:'))
        revistaInicial = int(input('Ingrese mínimo de número de revistas inicial:'))
        revistaFinal = int(input('Ingrese el máximo de revistas iniciales:'))

        if revistaFinal < revistaInicial:
            print('Ingrese un rango valido.')
        else:
            CalculoSimulacion(revistaInicial, revistaFinal, iteraciones)
    except: 
        print("Ha ocurrido un error por favor intente nuevamente")

try:
    shutil.rmtree("output")
except:
    os.mkdir("output")
    print("Por favor cierra todos los archivos excel antes de ejecutar nuevamente el programa y asegurese que exista la carpeta output")
else:
    os.mkdir("output")
    IniciarPrograma()





