import os
import math
from class_volume import Volume


# Funktion för att rensa skärmen beroende på operativsystem
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_menu():
    # Funktion för att skriva ut huvudmenyn
    clear_screen()
    print("-" * 30)
    print("Här kan du räkna ut volymer!")
    print(" ")
    print("Du kan välja mellan att räkna\nut volymen på")
    print("-" * 5)
    print("1: Kub\n2: Rätblock\n3: Prisma\n4: Cylinder\n5: Exit")
    print("-" * 5)


def inmatning(felhantering):
    # Funktion för att hantera användarinmatning med felhantering
    while True:
        try:
            värde = float(input(felhantering))
            return värde
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")


def calculate_volume(val, volume_calculator):
    # Funktion för att räkna ut volymen baserat på användarens val
    if val == "1":
        print("-" * 30)
        print("Här kan du se formeln för hur\nman räknar ut volymen av en kub!")
        print("-" * 5)
        print("Volym = a ⋅ a ⋅ a = a**3")
        print("-" * 5)
        print("Annars kan du mata in sidornas längd för att få det uträknat")

        # Kub: Ange längden på en sida för att beräkna volymen
        sida = inmatning("Ange längd på sida  > ")
        volym = volume_calculator.kub_volym(sida) # Beräkna volymen på en kub med sidolängden 'sida' och tilldela resultatet till variabeln 'volym'
        print(f"Volymen på kuben är {volym}")
        print("-" * 5)

    elif val == "2":
        print("-" * 30)
        print("Här kan du se formeln för hur\nman räknar ut volymen av ett rätblock!")
        print("-" * 5)
        print("Volym = b ⋅ d ⋅ h")
        print("-" * 5)
        print("Annars kan du mata in längd, bredden och höjden för att få det uträknat")

        # Rätblock: Ange längd, bredd och höjd för att beräkna volymen
        längd = inmatning("Ange längden  > ")
        bredd = inmatning("Ange bredden > ")
        höjd = inmatning("Ange Höjden > ")

        volym = volume_calculator.rectangular_block_volym(längd, bredd, höjd)
        print(f"Volymen på rätblocket är {volym}")
        print("-" * 5)

    elif val == "3":
        print("Här kan du se formeln för hur\nman räknar ut volymen av en prisma!")
        print("-" * 5)
        print("Volym = B ⋅ h där B är basytans area.")
        print("-" * 5)
        print("Annars kan du mata in längd, bredden och höjden för att få det uträknat")

        # Prisma: Ange längd, bredd och höjd för att beräkna volymen
        längd = inmatning("Ange längden  > ")
        bredd = inmatning("Ange bredden > ")
        area = längd * bredd
        print("Arean på prisman är ", area)
        höjd = inmatning("Ange Höjden > ")

        volym = volume_calculator.prism_volym(längd, bredd, höjd)
        print(f"Volymen på prisman är {volym}")
        print("-" * 5)

    elif val == "4":
        print("Här kan du se formeln för hur\nman räknar ut volymen av en cylinder!")
        print("-" * 5)
        print("Volym = πr**2 ⋅ h.")
        print("-" * 5)
        print("Annars kan du mata in cylinders radie och höjd för att få det uträknat")

        # Cylinder: Ange radie och höjd för att beräkna volymen
        radie = inmatning("Ange radien  > ")
        area = radie**2 * math.pi
        print("Arean på culindern är", area)
        höjd = inmatning("Ange Höjden > ")

        # Hämtar formeln för uträkning av cylinder från klassen
        volym = volume_calculator.cylinder_volym(radie, höjd)
        print(f"Volymen på culindern är {volym}")
        print("-" * 5)
    
    elif val == "5":
        return False

    # Loopa tills användaren ger ett giltigt svar (j eller n)
    while True:
        fortsätt = input("Vill du forsätta till nästa? J/N > ").lower()
        if fortsätt == "j":
            return True
        elif fortsätt == "n":
            return False
        else:
            # Om användaren ger ett ogiltigt svar, visa felmeddelande och fortsätt loopa
            print("-" * 5)
            print("Fel: Ogiltigt val! Vänligen ange J/N")


if __name__ == "__main__":
    volume_calculator = Volume() # Skapar en instans av klassen Volume för att beräkna volymer
    while True:
        # Visa huvudmenyn för volymberäkning
        print_menu()
        val = input("Välj ett av alternativen ovan genom att ange dess siffra!\n> ").lower()
        if val not in ['1', '2', '3', '4', '5']:
            input("Fel: Ogiltigt val\nTryck enter för att fortsätta...")
            continue
        if not calculate_volume(val, volume_calculator):
            break
