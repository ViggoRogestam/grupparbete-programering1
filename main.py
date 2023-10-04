from pytz.exceptions import UnknownTimeZoneError

import Lenght_converter
from Lenght_converter import Length
from Lenght_converter import celsius_to_fahrenheit
from Lenght_converter import fahrenheit_to_celsius
from ui import Ui
from volym import print_menu
from volym import clear_screen
from volym import calculate_volume
from class_volume import Volume
volume_calculator = Volume()
from time_converter import TidszonsOmvandlare
from time_converter import omvandla_tidszon
import pytz


while True:
    clear_screen()
    ui = Ui(30)
    ui.print_header('hej')
    ui.print_choices('volymer', 'längder', 'tidzoner')
    ui.print_dot()
    # User Choice
    choice = input('Enter choice >')

    if choice == '1':
        clear_screen()
        print_menu()
        choice = input('Välj ett av alternativen ovan genom att ange dess siffra! >')
        calculate_volume(choice, volume_calculator)
        input()
        if __name__ == "__main__":
            volume_calculator = Volume()
            while True:
                print_menu()
                val = input("Välj ett av alternativen ovan genom att ange dess siffra!\n> ")

                if not calculate_volume(val, volume_calculator):
                    break

                fortsätt = input("Vill du forsätta till nästa? J/N > ").lower()
                fortsätt_till_nästa = fortsätt == "j"
                if not fortsätt_till_nästa:
                    break

    elif choice == '2':
        clear_screen()
        ui.print_header('Lenght Converter')
        ui.print_line()
        length = input('Enter lenght and unit >')
        value, unit = length.split()
        float(value)
        str(unit)
        l1 = Length(value, unit)
        # Ui
        clear_screen()
        ui.print_header('Choose unit to convert to')
        ui.print_line()
        ui.print_choices('Milimeter', 'Centimeter', 'Meter', 'Kilometer', 'Inches', 'Feet')
        ui.print_dot()
        choice = input('>')
        ui.print_line()

        #  if milimeter
        # TODO: fix print if no valid unit is provieded
        if choice == '1':
            print(f'{length} equals {(l1.to_milimeter())} milimeter')
            input()
            continue
        elif choice == '2':
            print(f'{length} equals {(l1.to_centimeter())} centimeter')
            input()
            continue
        elif choice == '3':
            print(f'{length} equals {(l1.to_meter())} meter')
            input()
            continue
        elif choice == '4':
            print(f'{length} equals {(l1.to_kilometer())} kilometer')
            input()
            continue
        elif choice == '5':
            print(f'{length} equals {(l1.to_inches())} inches')
            input()
            continue
        elif choice == '6':
            print(f'{length} equals {(l1.to_feet())} feet')
            input()
            continue
        else:
            input('Error: no valid input.\n Press Enter to continue...')
            continue

    # TODO: fixa try except
    # TODO: Bugg att program forstätter till choice 3 om man gör invalid input på lenght converter

    # TODO: obejkt-orientera koden sedan importera den:
    elif choice == '3':
        clear_screen()
        ui.print_header('Tidszonomvandlare')
        ui.print_line()
        while True:
            try:
                fran_tidszon_input = input(
                    "Ange kontinent/huvudstad du vill konvertera från: (t.ex. 'Europe/Stockholm') eller 'avsluta' för att avsluta: ")
                if fran_tidszon_input == 'avsluta':
                    break
                fran_tidszon_strang = fran_tidszon_input or "Europe/Stockholm"
                fran_tidszon = pytz.timezone(fran_tidszon_strang)

                till_tidszon_input = input(
                    "Ange kontinent/huvudstad du vill konvertera till: (t.ex. 'Europe/London') eller 'avsluta' för att avsluta: ")
                if till_tidszon_input == 'avsluta':
                    break
                till_tidszon_strang = till_tidszon_input or "Europe/London"
                till_tidszon = pytz.timezone(till_tidszon_strang)

                omvandlare = TidszonsOmvandlare(fran_tidszon, till_tidszon)
                omvandlad_tid = omvandlare.omvandla_tidszon()
                print(f"\nOmvandlad tid från {fran_tidszon_strang} till {till_tidszon_strang}: {omvandlad_tid}\n")

            except UnknownTimeZoneError as e:
                print(f"{e} är inte en giltig tidszon.")
            break
    if __name__ == "__main__":
        omvandla_tidszon()

    else:
        input('\nNo valid choice. Press enter to continue...')
        continue
