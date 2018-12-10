from Resultado import Resultado
from Simulacion import Simulacion

simulacion = Simulacion()

print('Simulacion de la segunda política, desde el numero inicial de revistas x hasta y: \n')
revistaInicial = int(input('Ingrese mínimo de número de revistas inicial:'))
revistaFinal = int(input('Ingrese el máximo de revistas iniciales:'))

def CalculoSimulacion(rangoIni, rangoFinal):
    for mes in range(1,31):
        for revista in range(rangoIni, rangoFinal+1):
            resultado = Resultado(mes, revista)
            simulacion.AgregarResultado(resultado)

    simulacion.Imprimir()

if revistaFinal < revistaInicial:
    print('Ingrese un rango valido.')
else:
    CalculoSimulacion(revistaInicial, revistaFinal)