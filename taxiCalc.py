print("Herzlich Willkommen zum Taxirechner")
print("")
print("Der Grundpreis pro KM beträg Euro 2.50")
print("Die Taxigrundgebühr beträg Euro 5.70")
km = input("Bitte gib die gefahrenen KM ein: ")
baseFare = 5.70
kmPrice = 2.50
fahrPrice = float(km) * float(kmPrice)
finalPrice = float(fahrPrice) + float(baseFare)
print(f"Du bist {km} km gefahren. Das kostet {fahrPrice} Euro")
print(f"Der Endbetrag (inkl. Grundgebühr) in Euro beträgt: {finalPrice}")
input("Drücke eine Taste!")