from Resultado import Resultado
from Simulacion import Simulacion
import Operaciones
import os
import shutil

mayoresGanancias = []


def CalculoSimulacion(rangoIni, rangoFinal, iteraciones):
    for i in range(1,iteraciones+1):
        simulacion = Simulacion(i)
        for mes in range(1,31):
            for revista in range(rangoIni, rangoFinal+1):
                resultado = Resultado(mes, revista)
                simulacion.AgregarResultado(resultado)

        simulacion.Imprimir()
        mayoresGanancias.append(simulacion.Get_GananciaMayor())

    Operaciones.ImprimirGanancias(mayoresGanancias)
    
def IniciarPrograma():
    try:
        print('Simulacion de la segunda política, desde el numero inicial de revistas x hasta y: \n')
        iteraciones = int(input('Ingrese el número de simulaciones que deseas realizar:'))
        revistaInicial = int(input('Ingrese mínimo de número de revistas inicial:'))
        revistaFinal = int(input('Ingrese el máximo de revistas iniciales:'))

        if revistaFinal < revistaInicial:
            print('Ingrese un rango valido.')
        else:
            CalculoSimulacion(revistaInicial, revistaFinal, iteraciones)
    except Exception as e: 
        print("Ha ocurrido un error por favor intente nuevamente")
        print("Detalle del error:", e)

error = False
folder = 'output/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception:
        if error is False:
            print("El programa no ha podido eliminar todos los archivos excel, por favor cierrelos e intente nuevamente.")
        error = True
        
if error is False:
    IniciarPrograma()



