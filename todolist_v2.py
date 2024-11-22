todos = ['Apfel', 'Birne']

for _ in range(100000):
    print("Was willst du tun?")
    print("(1) To-Do anzeigen")
    print("(2) To-Do hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 1:
        print("Meine Liste hat folgende Einträge:")
        print("")
        for todo in todos:
            print(f"- {todo}")
    if int(option) == 2:
        newItem = input("Was möchtest du hinzufügen? ")
        todos.append(newItem)

    print("")
    print("")
print("Programm beendet.")