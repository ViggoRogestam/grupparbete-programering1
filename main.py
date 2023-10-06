from pytz.exceptions import UnknownTimeZoneError
from Lenght_converter import Length
from ui import Ui
from volym import print_menu
from volym import clear_screen
from volym import calculate_volume
from class_volume import Volume
from time_converter import TidszonsOmvandlare
from time_converter import omvandla_tidszon
import area_modul
import pytz

#Variables
volume_calculator = Volume()

while True:
    clear_screen()
    # Prints user intefrance
    ui = Ui(30)
    ui.print_header('Omvandlaren')
    ui.print_choices('volymer', 'längder', 'tidzoner', 'areor', 'exit')
    ui.print_dot()
    # User Choice
    choice = input('Enter choice > ')

    if choice == '1':
        if __name__ == "__main__":
            volume_calculator = Volume()
            while True:
                print_menu()
                val = input("Välj ett av alternativen ovan genom att ange dess siffra!\n> ").lower()
                if val not in ['1', '2', '3', '4', '5']:
                    input("Fel: Ogiltigt val\nTryck enter för att fortsätta...")
                    continue
                if not calculate_volume(val, volume_calculator):
                    break
            continue

    elif choice == '2':
        clear_screen()
        # Print User Interface
        ui.print_header('Lenght Converter')
        ui.print_line()
        # Ask user for input
        length = input('Enter lenght and unit >')
        # Try to split input to get value and unit separate
        try:
            value, unit = length.split()
            float(value)
            str(unit)
        except ValueError:
            ui.print_line()
            input('ValueError: Enter valid lenght and unit.\n\nPress Enter to continue')
            continue
        # Crate object of lenght class
        l1 = Length(value, unit)
        # Ui
        clear_screen()
        ui.print_header('Choose unit to convert to')
        ui.print_line()
        ui.print_choices('Milimeter', 'Centimeter', 'Meter', 'Kilometer', 'Inches', 'Feet')
        ui.print_dot()
        choice = input('>')
        ui.print_line()

        if unit in ['milimeter', 'centimeter', 'meter', 'kilometer', 'inches', 'feet']:

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
                input('Error: no valid input.\n\n Press Enter to continue...')
        else:
            ui.print_line()
            input(f'Error: {unit} is not valid\n\n Press Enter to continue...')
            continue

    elif choice == '3':
        while True:
            clear_screen()
            ui.print_header('Tidszonomvandlare')
            ui.print_line()
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
    elif choice == '4':
        ui_width = 30
        while True:
            clear_screen()
            print("----- Area -----".center(ui_width))
            print("-" * ui_width)
            print("| 1\t| Rektangel/Kvadrat")
            print("| 2\t| Triangel")
            print("| 3\t| Cirkel")
            print("| 4\t| Romb")
            print("| 5\t| Parallellogram")
            print("| 6\t| Parallelltrapets")
            print("| 7\t| Kon")
            print("| 8\t| Klot")
            print("-" * ui_width)
            print("| Exit\t| Avslutar programmet ")
            print("-" * ui_width)

            # Användarinmatning
            choice = input("Ange val: ").lower()

            if choice == "1":
                try:
                    while True:
                        längd = float(input("Ange längd: "))
                        bredd = float(input("Ange bredd: "))
                        figurens_area = area_modul.area().area_rektangel(längd, bredd)
                        ui.print_line()
                        print("Rektangeln/kvadratens area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                except ValueError:
                    print("Fel inmatning, ange ett tal...")
                    input('\nTryck enter för att forstätta...')

            elif choice == "2":
                try:
                    while True:
                        basen = float(input("Ange basen: "))
                        höjden = float(input("Ange höjden: "))
                        figurens_area = area_modul.area().area_triangel(basen, höjden)
                        ui.print_line()
                        print("Triangels area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                except ValueError:
                    print("Fel inmatning, ange ett tal...")
                    input('\nTryck enter för att forstätta...')

            elif choice == "3":
                while True:
                    try:
                        radien = float(input("Ange radie: "))
                        figurens_area = area_modul.area().area_cirkel(radien)
                        ui.print_line()
                        print("Cirkelns area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        ui.print_line()
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')

            elif choice == "4":
                while True:
                    try:
                        stora_dia = float(input("Ange stora diagonalen: "))
                        lilla_dia = float(input("Ange lilla diagonalen: "))
                        figurens_area = area_modul.area().area_romb(stora_dia, lilla_dia)
                        ui.print_line()
                        print("Rombens area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        ui.print_line()
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')

            elif choice == "5":
                while True:
                    try:
                        basen = float(input("Ange basen: "))
                        höjden = float(input("Ange höjden: "))
                        figurens_area = area_modul.area().area_parallellogram(basen, höjden)
                        ui.print_line()
                        print("Parallellogrammets area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        ui.print_line()
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')

            elif choice == "6":
                while True:
                    try:
                        stora_sidan = float(input("Ange längden på stora sidan: "))
                        lilla_sidan = float(input("Ange längden på lilla sidan: "))
                        höjden = float(input("Ange höjden: "))
                        figurens_area = area_modul.area().area_parallelltrapets(stora_sidan, lilla_sidan, höjden)
                        ui.print_line()
                        print("Parallelltrapetsens area är:", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        ui.print_line()
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')

            elif choice == "7":
                while True:
                    try:
                        radien = float(input("Ange radie: "))
                        sträckan = float(input("Ange sträcka: "))
                        figurens_area = area_modul.area().area_kon(radien, sträckan)
                        ui.print_line()
                        print("Konens area är", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        ui.print_line()
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')
            elif choice == "8":
                while True:
                    try:
                        radien = float(input("Ange radie: "))
                        figurens_area = area_modul.area().area_cirkel(radien)
                        ui.print_line()
                        print("Klotets area är", figurens_area, "a.e")
                        input('\nTryck enter för att forstätta...')
                        break
                    except ValueError:
                        print("Fel inmatning, ange ett tal...")
                        input('\nTryck enter för att forstätta...')

            elif choice == "exit":
                ui.print_line()
                print("Avslutar programmet")
                from time import sleep

                sleep(3)
                break

            else:
                print('*' * ui_width)
                input('*Fel inmatning, ange ett tal mellan 1-8 eller "exit" för att gå ut')
        continue
    elif choice == '5':
        ui.print_line()
        print('Program closed')
        exit()

    else:
        ui.print_line()
        input('No valid choice.\n\nPress enter to continue...')
        continue
    if __name__ == "__main__":
        omvandla_tidszon()
