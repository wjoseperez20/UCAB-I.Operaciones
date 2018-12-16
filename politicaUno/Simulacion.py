import time
import Operaciones
import operator
import xlsxwriter

class Simulacion:

    def __init__(self, iterator):
        self.listaResultados = []
        self.listaOrdenada = []
        self.__iterator = iterator
    
    def AgregarResultado(self, resultado):
        self.listaResultados.append(resultado)
    
    def __OrdenarResultados(self):
        self.listaOrdenada = sorted(self.listaResultados, key=lambda x: x.Get_RevistaInicial())

    def __CalcularPromedios(self):
        promediosResultados = {}
        for resultado in self.listaOrdenada:
            if resultado.Get_RevistaInicial() in promediosResultados:
                promediosResultados[resultado.Get_RevistaInicial()] += resultado.Get_Ganancia()
            else:
                promediosResultados[resultado.Get_RevistaInicial()] = resultado.Get_Ganancia()

        for key, value in promediosResultados.items():
            promediosResultados[key] = round(promediosResultados[key]/30,4)

        self.__listaPromedios = Operaciones.OrdenarLista(promediosResultados)
    
    def __CalcularMaximaGanancia(self):
        lista_ganancias = {}
        for resultado in self.__listaPromedios:
            lista_ganancias[resultado[0]] = resultado[1]
        
        self.__gananciaMayor = max(lista_ganancias.items(), key=operator.itemgetter(1))

    def Get_GananciaMayor(self):
        return self.__gananciaMayor

    def Imprimir(self):
        self.__OrdenarResultados()
        self.__CalcularPromedios()
        self.__CalcularMaximaGanancia()

        workbook = xlsxwriter.Workbook("output/PoliticaUno_"+str(self.__iterator)+".xlsx")
        worksheet_corridas = workbook.add_worksheet("Simulaciones")
        worksheet_promedios = workbook.add_worksheet("Promedios")
        worksheet_grafica = workbook.add_worksheet("Grafica")
        
        self.__CrearFormatosExcel(workbook)
        
        self.__CrearTablaCorridasExcel(worksheet_corridas)
        self.__LlenarTablaCorridasExcel(worksheet_corridas)

        self.__CrearTablaPromedioExcel(worksheet_promedios)
        self.__LlenarTablaPromediosExcel(worksheet_promedios)

        self.__CrearGraficaPromedio(worksheet_grafica, workbook)

        workbook.close()

    
    def __CrearFormatosExcel(self, workbook):
        self.__cell_format_header = workbook.add_format({'center_across':True, 'bold':True, 'border':True})
        self.__cell_format_header.set_border(style=2)
        self.__cell_format = workbook.add_format({'center_across':True, 'border':True})
        self.__cell_format_max = workbook.add_format({'center_across':True, 'border':True})
        self.__cell_format_max.set_bg_color('#6fdc6f')

    def __CrearTablaCorridasExcel(self, worksheet):
        worksheet.set_column('B:I', 16)
        worksheet.write(1, 1, "COMPRA INICIAL", self.__cell_format_header)
        worksheet.write(1, 2, "MES", self.__cell_format_header)
        worksheet.write(1, 3, "ALEATORIO #1", self.__cell_format_header)
        worksheet.write(1, 4, "DEMANDA DIA 10", self.__cell_format_header)
        worksheet.write(1, 5, "ALEATORIO #2", self.__cell_format_header)
        worksheet.write(1, 6, "DEMANDA DIA 20", self.__cell_format_header)
        worksheet.write(1, 7, "SOBRANTE FINAL", self.__cell_format_header)
        worksheet.write(1, 8, "GANANCIA", self.__cell_format_header)
    
    def __LlenarTablaCorridasExcel(self, worksheet):
        row = 2
        for resultado in self.listaOrdenada:
            worksheet.write(row, 1, resultado.Get_RevistaInicial(), self.__cell_format)
            worksheet.write(row, 2, resultado.Get_Mes(), self.__cell_format)
            worksheet.write(row, 3, resultado.Get_Random1(), self.__cell_format)
            worksheet.write(row, 4, resultado.Get_PrimeraDemanda(), self.__cell_format)
            worksheet.write(row, 5, resultado.Get_Random2(), self.__cell_format)
            worksheet.write(row, 6, resultado.Get_SegundaDemanda(), self.__cell_format)
            worksheet.write(row, 7, resultado.Get_SobranteFinal(), self.__cell_format)
            worksheet.write(row, 8, resultado.Get_Ganancia(), self.__cell_format)
            row += 1

    
    def __CrearTablaPromedioExcel(self, worksheet):
        worksheet.set_column('B:C', 20)
        worksheet.write(1, 1, "COMPRA INICIAL", self.__cell_format_header)
        worksheet.write(1, 2, "PROMEDIO MENSUAL ", self.__cell_format_header)

    def __LlenarTablaPromediosExcel(self, worksheet):
        row = 2
        for resultado in self.__listaPromedios:
            
            if self.__gananciaMayor[1] == resultado[1]:
                cell_format = self.__cell_format_max
            else:
                cell_format = self.__cell_format

            worksheet.write(row, 1, resultado[0], cell_format)
            worksheet.write(row, 2, resultado[1], cell_format)
            row += 1

    def __CrearGraficaPromedio(self, worksheet, workbook):
        chart = workbook.add_chart({'type': 'line'})

        chart.add_series({
            'name':'Promedios',
            'categories': ['Promedios', 2, 1, len(self.__listaPromedios)+1, 1],
            'values':     ['Promedios', 2, 2, len(self.__listaPromedios)+1, 2],
            'line':       {'color': 'blue'},
            'marker': {'type': 'diamond','size': 8, 'border': {'color': 'blue'},'fill':{'color': 'blue'}}
        })

        chart.set_title ({'name': 'Promedios de ganancias mensuales'})
        chart.set_size({'x_scale': 2.5, 'y_scale': 1.5})
        chart.set_x_axis({'name': 'Compra inicial de Revistas'})
        chart.set_y_axis({'name': 'Ganancia en $'})

        chart.set_style(1)

        worksheet.insert_chart('B2', chart, {'x_offset': 0, 'y_offset': 0})

