import Operaciones


class Resultado:
    def __init__(self, mes, inicial):
        self.__mes = mes
        self.__revistaInicial = inicial
        self.__numeroRadom1 = Operaciones.GenerarRandom()
        self.__numeroRadom2 = Operaciones.GenerarRandom()
        self.__ObtenerPrimeraDemanda()
        self.__ObtenerSegundaDemanda()
        self.__sobranteFinal = 0
        self.__compraDia10 = 0
        self.__CalcularGanancia()

    def Get_Random1(self):
        return self.__numeroRadom1

    def Get_Random2(self):
        return self.__numeroRadom2

    def Get_PrimeraDemanda(self):
        return self.__primeraDemanda

    def Get_SegundaDemanda(self):
        return self.__segundaDemanda

    def Get_Mes(self):
        return self.__mes

    def Get_RevistaInicial(self):
        return self.__revistaInicial

    def Get_Ganancia(self):
        return self.__ganancia

    def Get_SobranteFinal(self):
        return self.__sobranteFinal

    def Get_CompraDia10(self):
        return self.__compraDia10

    def __ObtenerPrimeraDemanda(self):
        random = self.__numeroRadom1
        if random < 0.05:
            self.__primeraDemanda = 5
        elif random >= 0.05 and random < 0.10:
            self.__primeraDemanda = 6
        elif random >= 0.10 and random < 0.20:
            self.__primeraDemanda = 7
        elif random >= 0.20 and random < 0.35:
            self.__primeraDemanda = 8
        elif random >= 0.35 and random < 0.60:
            self.__primeraDemanda = 9
        elif random >= 0.60 and random < 0.85:
            self.__primeraDemanda = 10
        else:
            self.__primeraDemanda = 11

    def __ObtenerSegundaDemanda(self):
        random = self.__numeroRadom2
        if random < 0.15:
            self.__segundaDemanda = 4
        elif random >= 0.15 and random < 0.35:
            self.__segundaDemanda = 5
        elif random >= 0.35 and random < 0.65:
            self.__segundaDemanda = 6
        elif random >= 0.65 and random < 0.85:
            self.__segundaDemanda = 7
        else:
            self.__segundaDemanda = 8

    def __CalcularGanancia(self):
        inversion = self.__revistaInicial * 1.5
        montoVendido = 0
        montoSobrante = 0

        if self.__revistaInicial >= self.__primeraDemanda:
            montoVendido = self.__primeraDemanda * 2
            revistaRestante = self.__revistaInicial - self.__primeraDemanda
            if revistaRestante < 8:
                self.__compraDia10 = 8 - revistaRestante
                inversion += self.__compraDia10 * 1.2

            totalRevistas10 = revistaRestante + self.__compraDia10

            if totalRevistas10 >= self.__segundaDemanda:
                montoVendido += self.__segundaDemanda * 2
                self.__sobranteFinal = totalRevistas10 - self.__segundaDemanda
            else:
                montoVendido += totalRevistas10 * 2
        else:
            montoVendido += self.__revistaInicial * 2
            self.__compraDia10 = 8
            inversion += self.__compraDia10 * 1.2

            if self.__compraDia10 >= self.__segundaDemanda:
                montoVendido += self.__segundaDemanda * 2
                self.__sobranteFinal = self.__compraDia10 - self.__segundaDemanda
            else:
                montoVendido += self.__compraDia10 * 2

        montoSobrante = self.__sobranteFinal * 0.60
        self.__ganancia = montoVendido + montoSobrante - inversion

    def __str__(self):
        return 'ini=' + str(self.__revistaInicial) + ';mes=' + str(self.__mes) + ';rand1=' + str(
            self.__numeroRadom1) + ';demanda10=' + str(self.__primeraDemanda) + ';compra10=' + str(
            self.__compraDia10) + ';rand2=' + str(self.__numeroRadom2) + ';demanda20=' + str(
            self.__segundaDemanda) + ';sobrante=' + str(self.__sobranteFinal) + ';ganancia=' + str(
            self.__ganancia) + ";"
