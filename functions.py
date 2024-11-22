
absender = input("Wer ist der Absender? ")
print("")

def gen_newsletter(absender):
    name = input("An wen geht die Nachricht? ")
    print(f"Hallo {name}")
    print("")
    print("Mit dieser EMail möchte ich dich über meine neue Adresse informieren.")
    print("")
    print("Meine neue Adresse lautet:")
    print("Juri Steimann")
    print("Schwarzwaldstraße 12")
    print("D-78462 Konstanz")
    print("Telefon: 0176 1234567")
    print("Email: juri.steimann@web.de")
    print("")
    print("Liebe Grüsse")
    print(f"{absender}")

gen_newsletter(absender)