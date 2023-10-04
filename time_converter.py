import pytz
from datetime import datetime
from pytz.exceptions import UnknownTimeZoneError

class TidszonsOmvandlare:
    """En klass för att omvandla tid från en tidszon till en annan."""

    def __init__(self, fran_tidszon, till_tidszon):
        """
        Initialiserar en TidszonsOmvandlare-objekt.

        Args:
            fran_tidszon (timezone): Källtidszonsobjektet.
            till_tidszon (timezone): Måltidszonsobjektet.
        """
        self.fran_tidszon = fran_tidszon
        self.till_tidszon = till_tidszon

    def omvandla_tidszon(self):
        """
        Omvandlar aktuell tid från källtidszonen till måltidszonen.

        Returns:
            str: En sträng som representerar tiden i måltidszonen i formatet "%H:%M:%S".
        """
        fran_tidszon_datumtid = datetime.now(self.fran_tidszon)
        omvandlad_tidszon = fran_tidszon_datumtid.astimezone(self.till_tidszon)
        return omvandlad_tidszon.strftime("%H:%M:%S")


def omvandla_tidszon():
    """
    Kör ett program för tidszonsomvandlare.

    Detta program ber användaren att ange källtidszon och måltidszon och
    omvandlar aktuell tid från källtidszonen till måltidszonen.
    """
    print("\n--- Tidszonsomvandlare ---")

    while True:
        try:
            fran_tidszon_input = input("Ange kontinent/huvudstad du vill konvertera från: (t.ex. 'Europe/Stockholm') eller 'avsluta' för att avsluta: ")
            if fran_tidszon_input == 'avsluta':
                break
            fran_tidszon_strang = fran_tidszon_input or "Europe/Stockholm"
            fran_tidszon = pytz.timezone(fran_tidszon_strang)

            till_tidszon_input = input("Ange kontinent/huvudstad du vill konvertera till: (t.ex. 'Europe/London') eller 'avsluta' för att avsluta: ")
            if till_tidszon_input == 'avsluta':
                break
            till_tidszon_strang = till_tidszon_input or "Europe/London"
            till_tidszon = pytz.timezone(till_tidszon_strang)

            omvandlare = TidszonsOmvandlare(fran_tidszon, till_tidszon)
            omvandlad_tid = omvandlare.omvandla_tidszon()
            print(f"\nOmvandlad tid från {fran_tidszon_strang} till {till_tidszon_strang}: {omvandlad_tid}\n")

        except UnknownTimeZoneError as e:
            print(f"{e} är inte en giltig tidszon.")


if __name__ == "__main__":
    omvandla_tidszon()
