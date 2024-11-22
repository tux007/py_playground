todos = ['Apfel', 'Birne']

for _ in range(100000):
    newItem = input("Was möchtest du hinzufügen? ")
    todos.append(newItem)
    print("Meine Liste hat folgende Einträge:")

    for todo in todos:
        print(f"- {todo}")

print("")
print("Programm beendet.")