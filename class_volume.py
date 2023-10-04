import math

class Volume:

    # Funktion för att beräkna volymen av en kub
    @staticmethod
    def kub_volym(sida):
        sida = float(sida)
        volym = sida ** 3
        return volym

    # Funktion för att beräkna volymen av ett rätblock (rektangelbaserat prisma)
    @staticmethod
    def rectangular_block_volym(längd, bredd, höjd):
        längd = float(längd)
        bredd = float(bredd)
        höjd = float(höjd)
        volym = längd * bredd * höjd
        return volym

    # Funktion för att beräkna volymen av ett prisma
    @staticmethod
    def prism_volym(längd, bredd, höjd):
        längd = float(längd)
        bredd = float(bredd)
        höjd = float(höjd)
        volym = (längd*bredd) * höjd
        return volym

    # Funktion för att beräkna volymen av en cylinder
    @staticmethod
    def cylinder_volym(radie, höjd):
        radie = float(radie)
        höjd = float(höjd)
        volym = math.pi * radie**2 * höjd
        return volym




