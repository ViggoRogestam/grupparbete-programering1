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
from time_converter import omvandla_tidszon


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
    # TODO: fixa ui, låt andändaren välja vad längden ska konverteras till
    elif choice == '2':
        length = input('Enter lenght and unit >')
        value, unit = length.split()
        float(value)
        str(unit)
        l1 = Lenght_converter.Length(value, unit)
        print(l1.to_kilometer())
        input()
    # TODO: obejkt-orientera koden sedan importera den:
    elif choice == '3':
        omvandla_tidszon()
    else:
        input('\nNo valid choice. Press enter to continue...')
        continue
