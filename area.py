import os
import area_modul

# Användargränssnitt

while True:
    ui_width = 30
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
    print("| Exit\t| Avsluta programmet")
    print("-" * ui_width)

    # Användarinmatning
    choice = input("Vad vill du beräkna: ")

    if choice == "1":

        längd = float(input("Ange längd: "))
        bredd = float(input("Ange bredd: "))
        figurens_area = area_modul.area().area_rektangel(längd, bredd)
        print("Rektangeln/kvadratens area är:", figurens_area, "a.e")

    elif choice == "2":
        basen = float(input("Ange basen: "))
        höjden = float(input("Ange höjden: "))
        figurens_area = area_modul.area().area_triangel(basen, höjden)
        print("Triangels area är:", figurens_area, "a.e")

    elif choice == "3":
        radien = float(input("Ange radie: "))
        figurens_area = area_modul.area().area_cirkel(radien)
        print("Cirkelns area är:", figurens_area, "a.e")

    elif choice == "4":
        stora_dia = float(input("Ange stora diagonalen: "))
        lilla_dia = float(input("Ange lilla diagonalen: "))
        figurens_area = area_modul.area().area_romb(stora_dia, lilla_dia)
        print("Rombens area är:", figurens_area, "a.e")

    elif choice == "5":
        basen = float(input("Ange basen: "))
        höjden = float(input("Ange höjden: "))
        figurens_area = area_modul.area().area_parallellogram(basen, höjden)
        print("Parallellogrammets area är:", figurens_area, "a.e")

    elif choice == "6":
        stora_sidan = float(input("Ange längden på stora sidan: "))
        lilla_sidan = float(input("Ange längden på lilla sidan: "))
        höjden = float(input("Ange höjden: "))
        figurens_area = area_modul.area().area_parallelltrapets(stora_sidan, lilla_sidan, höjden)
        print("Parallelltrapetsens area är:", figurens_area, "a.e")

    elif choice == "7":
        radien = float(input("Ange radie: "))
        sträckan = float(input("Ange sträcka: "))
        figurens_area = area_modul.area().area_kon(radien, sträckan)
        print("Konens area är", figurens_area, "a.e")

    elif choice == "8":
        radien = float(input("Ange radie: "))
        figurens_area = area_modul.area().area_cirkel(radien)
        print("Klotets area är", figurens_area, "a.e")

    else:
        print("*" * ui_width)
        print("*Fel inmatning, ange mellan 1-7")

    print("-" * ui_width)
    input("Tryck enter för att rensa")

    # Terminalrensning
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
