class Length:

    def __init__(self, value: float, unit: str):
        """

        :param value: Enter lenght
        :param unit: Enter Unit
        """
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        if self.unit == "centimeter":
            return float(self.value) / 100
        elif self.unit == "milimeter":
            return float(self.value) / 1000
        elif self.unit == "inches":
            return float(self.value) * 0.0254
        elif self.unit == "feet":
            return float(self.value) * 0.3048
        elif self.unit == "kilometer":
            return float(self.value) * 1000
        elif self.unit == 'meter':
            return float(self.value)

    def to_centimeter(self):
        if self.unit == "meter":
            return float(self.value) * 100
        elif self.unit == 'milimeter':
            return float(self.value) * 0.1
        elif self.unit == "inches":
            return float(self.value) * 2.54
        elif self.unit == "feet":
            return float(self.value) * 30.48
        elif self.unit == "kilometer":
            return float(self.value) * 100000
        elif self.unit == 'centimeter':
            return float(self.value)

    def to_kilometer(self):
        if self.unit == "meter":
            return float(float(self.value)) * 0.001
        elif self.unit == "milimeter":
            return float(self.value) * 0.000001
        elif self.unit == "inches":
            return float(self.value) * 0.0000254
        elif self.unit == "feet":
            return float(self.value) * 0.0003048
        elif self.unit == "centimeter":
            return float(self.value) * 0.00001
        elif self.unit == 'kilometer':
            return float(self.value)

    def to_inches(self):
        if self.unit == 'meter':
            return float(self.value) * 39.3701
        elif self.unit == 'centimeter':
            return float(self.value) * 0.393701
        elif self.unit == 'feet':
            return float(self.value) * 12
        elif self.unit == 'milimeter':
            return float(self.value) * 0.0393701
        elif self.unit == 'kilometer':
            return float(self.value) * 39370.1
        elif self.unit == 'inches':
            return float(self.value)

    def to_feet(self):
        if self.unit == 'meter':
            return float(self.value) * 3.28084
        elif self.unit == 'centimeter':
            return float(self.value) * 0.0328084
        elif self.unit == 'milimeter':
            return float(self.value) * 0.00328084
        elif self.unit == 'kilomteter':
            return float(self.value) * 3280.84
        elif self.unit == 'inches':
            return float(self.value) * 0.0833333
        elif self.unit == 'feet':
            return float(self.value)

    def to_milimeter(self):
        if self.unit == 'meter':
            return float(float(self.value)) * 1000
        elif self.unit == 'centimeter':
            return float(self.value) * 10
        elif self.unit == 'kilometer':
            return float(self.value) * 1000000
        elif self.unit == 'inches':
            return float(self.value) * 25.4
        elif self.unit == 'feet':
            return float(self.value) * 304.8
        elif self.unit == 'milimeter':
            return float(self.value)
