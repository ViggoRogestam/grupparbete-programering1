class Length:

    def __init__(self, value: int, unit: str):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        if self.unit == "centimeter":
            return self.value / 100
        elif self.unit == "milimeter":
            return self.value / 1000
        elif self.unit == "inches":
            return self.value * 0.0254
        elif self.unit == "feet":
            return self.value * 0.3048
        elif self.unit == "kilometer":
            return self.value / 1000
        else:
            return self.value


    def to_centimeter(self):
        if self.unit == "meter":
            return self.value / 100
        elif self.unit == 'milimeter':
            return self.value * 0.1
        elif self.unit == "inches":
            return self.value * 2.54
        elif self.unit == "feet":
            return self.value * 30.48
        elif self.unit == "kilometer":
            return self.value * 100000
        else:
            return self.value


    def to_kilometer(self):
        if self.value ==

    def to_inches(self):


    def to_feet(self):



def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def
