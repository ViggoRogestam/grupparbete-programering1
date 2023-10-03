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
"""from Time_zone import TimeConverter"""


while True:
    clear_screen()
    ui = Ui(30)
    ui.print_header('hej')
    ui.print_choices('volymer', 'längder', 'tidzoner')
    ui.print_dot()
# User Choice
    choice = input('Enter choice >')
    # TODO: ge error vid felaktig inmatning:
    if choice == '1':
        clear_screen()
        print_menu()
        choice = input('Enter choice >')
        calculate_volume(choice, volume_calculator)
        input()
        if __name__ == "__main__":
            volume_calculator = Volume()
            while True:
                print_menu()
                val = input("Välj ett av alternativen ovan genom att ange dess siffra!\n> ")
                if not calculate_volume(val, volume_calculator):
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
        if choice == '1':
            print(f'{length} equals {(l1.to_milimeter())} milimeter')
            input()
        elif choice == '2':
            print(f'{length} equals {(l1.to_centimeter())} centimeter')
            input()
        elif choice == '3':
            print(f'{length} equals {(l1.to_meter())} meter')
            input()
        elif choice == '4':
            print(f'{length} equals {(l1.to_kilometer())} kilometer')
            input()
        elif choice == '5':
            print(f'{length} equals {(l1.to_inches())} inches')
            input()
        elif choice == '6':
            print(f'{length} equals {(l1.to_feet())} feet')
            input()
        else:
            input('Error: no valid input.\n Press Enter to continue...')

    # TODO: obejkt-orientera koden sedan importera den:
    elif choice == '3':
        clear_screen()
        pass
    else:
        input('\nNo valid choice. Press enter to continue...')
        continue
