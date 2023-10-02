import os
import math
from class_volume import Volume

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    clear_screen()
    print("-" * 30)
    print("Här kan du räkna ut volymer!")
    print(" ")
    print("Du kan välja mellan att räkna\nut volymen på")
    print("-" * 5)
    print("1: Kub\n2: Rätblock\n3: Prisma\n4: Cylinder\n")
    print("-" * 5)

def calculate_volume(val, volume_calculator):
    if val == "1":
        print("-" * 30)
        print("Här kan du se formeln för hur\nman räknar ut volymen av en kub!")
        print("-" * 5)
        print("Volym = a ⋅ a ⋅ a = a**3")
        print("-" * 5)
        print("Annars kan du mata in sidornas längd för att få det uträknat")
        try:
            sida = float(input("Ange längd på sida  > "))
            volym = volume_calculator.kub_volym(sida)
            print(f"Volymen på kuben är {volym}")
            print("-" * 5)
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")

    elif val == "2": 
        print("-" * 30)
        print("Här kan du se formeln för hur\nman räknar ut volymen av ett rätblock!")
        print("-" * 5)
        print("Volym = b ⋅ d ⋅ h")
        print("-" * 5)
        print("Annars kan du mata in längd, bredden och höjden för att få det uträknat")
        try:
            längd = float(input("Ange längden  > "))
            bredd = float(input("Ange bredden > "))
            höjd = float(input("Ange Höjden > "))
            volym = volume_calculator.rectangular_block_volym(längd, bredd, höjd )
            print(f"Volymen på rätblocket är {volym}")
            print("-" * 5)
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")

    elif val == "3":
        print("Här kan du se formeln för hur\nman räknar ut volymen av en prisma!")
        print("-" * 5)
        print("Volym = B ⋅ h där B är basytans area.")
        print("-" * 5)
        print("Annars kan du mata in längd, bredden och höjden för att få det uträknat")
        try:
            längd = float(input("Ange längden  > "))
            bredd = float(input("Ange bredden > "))
            area = längd * bredd
            print("Arean på prisman är ", area)
            höjd = float(input("Ange Höjden > "))
            volym = volume_calculator.prism_volym(längd, bredd, höjd)
            print(f"Volymen på prisman är {volym}")
            print("-" * 5)
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")

    elif val == "4":
        print("Här kan du se formeln för hur\nman räknar ut volymen av en cylinder!")
        print("-" * 5)
        print("Volym = πr**2 ⋅ h.")
        print("-" * 5)
        print("Annars kan du mata in cylinders radie och höjd för att få det uträknat")
        try:
            radie = float(input("Ange radien  > "))
            area = radie**2 * math.pi
            print("Arean på culindern är", area)
            höjd = float(input("Ange Höjden > "))
            volym = volume_calculator.cylinder_volym(radie, höjd)
            print(f"Volymen på culindern är {volym}")
            print("-" * 5)
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")

    fortsätt = input("Vill du forsätta till nästa? J/N > ").lower()
    return fortsätt == "j"

if __name__ == "__main__":
    volume_calculator = Volume()
    while True:
        print_menu()
        val = input("Välj ett av alternativen ovan genom att ange dess siffra!\n> ")
        if not calculate_volume(val, volume_calculator):
            break


