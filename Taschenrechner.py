zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
operation = input("Wählen Sie die Operation (+, -, *, /): ")

if operation == "+":
    print(zahl1 + zahl2)
elif operation == "-":
    print(zahl1 - zahl2)
elif operation == "*":
    print(zahl1 * zahl2)
elif operation == "/":

    if zahl2 == 0:
        ergebnis = "Fehler: Division durch Null ist nicht erlaubt."
    else:
        print(zahl1 / zahl2)
    