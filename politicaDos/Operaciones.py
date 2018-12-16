import random
import time
import xlsxwriter

def GenerarRandom():
    numero = round(random.random(),4)
    return numero

def OrdenarLista(diccionario):
    return [(k, diccionario[k]) for k in sorted(diccionario)]

def ImprimirGanancias(listaGanancias):
    timestamp = int(round(time.time() * 1000))
    workbook = xlsxwriter.Workbook("output/GananciasTotales_PoliticaDos.xlsx")
    worksheet_corridas = workbook.add_worksheet("Ganancias Totales")
    cell_format_header = workbook.add_format({'center_across':True, 'bold':True, 'border':True})
    cell_format_header.set_border(style=2)
    cell_format = workbook.add_format({'center_across':True, 'border':True})
    cell_format_max = workbook.add_format({'center_across':True, 'border':True})
    cell_format_max.set_bg_color('#6fdc6f')

    worksheet_corridas.set_column('B:C', 16)
    worksheet_corridas.write(1, 1, "COMPRA INICIAL", cell_format_header)
    worksheet_corridas.write(1, 2, "GANANCIA", cell_format_header)

    row = 2
    for resultado in listaGanancias:
        worksheet_corridas.write(row, 1, resultado[0], cell_format)
        worksheet_corridas.write(row, 2, resultado[1], cell_format)
        row += 1

    workbook.close()