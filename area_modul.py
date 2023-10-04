from math import pi


class area():

    def area_rektangel(self, längd, bredd):
        area = längd * bredd
        return area

    def area_triangel(self, basen, höjden):
        area = (basen * höjden) / 2
        return area

    def area_cirkel(self, radien):
        area = pi * radien ** 2
        return area

    def area_romb(self, stora_dia, lilla_dia):
        area = (stora_dia * lilla_dia) / 2
        return area

    def area_parallellogram(self, basen, höjden):
        area = basen * höjden
        return area

    def area_parallelltrapets(self, stora_sidan, lilla_sidan, höjden):
        area = (stora_sidan + lilla_sidan) / 2 * höjden
        return area

    def area_kon(self, radien, sträckan):
        area = pi * radien * sträckan
        return area

    def area_klot(self, radien):
        area = 4 * pi * radien ** 2
        return area
