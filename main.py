import urllib.request

url = 'https://raw.githubusercontent.com/ViggoRogestam/grupparbete-programering1/main/Lenght_converter.py'
filename = 'Lenght_converter.py'
urllib.request.urlretrieve(url, filename)

from Lenght_converter import Length
from Lenght_converter import celsius_to_fahrenheit
from Lenght_converter import fahrenheit_to_celsius

url = 'https://raw.githubusercontent.com/ViggoRogestam/grupparbete-programering1/main/ui.py'
filename = 'ui.py'
urllib.request.urlretrieve(url, filename)

from ui import Ui

ui = Ui(60)
ui.print_header('Rubrik')
ui.print_line()
ui.print_choices('test1','test2', 'test3')
ui.print_dot()
