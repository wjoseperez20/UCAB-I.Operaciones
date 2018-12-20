import random
import xlsxwriter
import matplotlib.pyplot as plt

def GenerarRandom():
    numero = round(random.random(),4)
    return numero

def OrdenarLista(diccionario):
    return [(k, diccionario[k]) for k in sorted(diccionario)]


def ImprimirGanancias(listaGanancias):
    workbook = xlsxwriter.Workbook("output/ListaGanancias_PoliticaTres.xlsx")
    worksheet_corridas = workbook.add_worksheet("Ganancias Totales")
    cell_format_header = workbook.add_format({'center_across':True, 'bold':True, 'border':True})
    cell_format_header.set_border(style=2)
    cell_format = workbook.add_format({'center_across':True, 'border':True})
    cell_format_max = workbook.add_format({'center_across':True, 'border':True})
    cell_format_max.set_bg_color('#6fdc6f')

    worksheet_corridas.set_column('B:D', 16)
    worksheet_corridas.write(1, 1, "COMPRA INICIAL", cell_format_header)
    worksheet_corridas.write(1, 2, "COMPRA DIA 10", cell_format_header)
    worksheet_corridas.write(1, 3, "GANANCIA", cell_format_header)

    row = 2
    for resultado in listaGanancias:
        worksheet_corridas.write(row, 1, resultado[0][0], cell_format)
        worksheet_corridas.write(row, 2, resultado[0][1], cell_format)
        worksheet_corridas.write(row, 3, resultado[1], cell_format)
        row += 1

    workbook.close()
    ImprimirBoxPlot(listaGanancias)

def ImprimirBoxPlot(listaGanancias):
    data = []
    for resultado in listaGanancias:
        data.append(resultado[1])
    fig, ax = plt.subplots()
    titulo = "Politica 3 - "+str(len(listaGanancias))+" Simulaciones"
    ax.set_title(titulo)
    ax.boxplot([data])
    fig.savefig("output/BoxPlot-Politica3.png")   # save the figure to file
    plt.close(fig)
    print('Simulación de la politica 3 finalizada con éxito, los resultados se encuentran en la carpeta output.')       