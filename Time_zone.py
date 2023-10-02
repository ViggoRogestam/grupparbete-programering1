import pytz
from datetime import datetime

# Skapa en klass som heter timezone_converter
# Innuti klassen ska alla attribut och metoder finnas, metoden som jobbar med att konvertera måste finnas i klassen
# Tänk objektorgenterat
# Skapa 2 instanser en instans från from_timezone till to_timezone

class TimeInTimezone:

    def __init__(self, time, timezone):
        self.time = time
        self.timezone = timezone

# hämta en lista så att användaren kan välja mellan olika alternativ
#
def convert_timezone(source_time_in_timezone, target_timezone):
    source_tz = pytz.timezone(source_time_in_timezone.timezone)
    target_tz = pytz.timezone(target_timezone)
    input_time = source_tz.localize(source_time_in_timezone.time, is_dst=None)

    converted_time = input_time.astimezone(target_tz)
    return TimeInTimezone(time=converted_time.strftime("%H:%M:%S"), timezone=target_timezone)

print("\n--- Tidszonsomvandlare ---")
while True:
    source_timezone = input("Ange tidzon: (t.ex. 'Europe/Stockholm') eller 'exit' för att avsluta: ")
    if source_timezone == 'exit':
        break

    input_time_str = input("Ange tid i Timme:Minut:Sekund: ")

    input_time = datetime.strptime(input_time_str, "%H:%M:%S")

    target_timezone = input("Ange måltidszon: (t.ex. 'Europe/London') ")

    # We add the date to input time so that the function works with daylight saving
    current_date = datetime.now(pytz.timezone(source_timezone)).strftime("%d-%m-%Y")
    input_time = datetime.strptime(f"{current_date} {input_time_str}", "%d-%m-%Y %H:%M:%S")

    source_time_in_timezone = TimeInTimezone(time=input_time, timezone=source_timezone)
    target_time_in_timezone = convert_timezone(source_time_in_timezone, target_timezone)
    print(f"\nKonverterad tid blev: {target_time_in_timezone.timezone}: {target_time_in_timezone.time}\n")
