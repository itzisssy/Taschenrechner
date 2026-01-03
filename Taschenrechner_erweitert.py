operatoren = ["+", "-", "*", "/", "^", "%"]

while True:
    # --- Zahl 1 eingeben ---
    while True:
        eingabe1 = input("Geben Sie die erste Zahl ein (oder 'exit' zum Beenden): ")
        if eingabe1.lower() == "exit":
            print("Programm beendet.")
            exit()
        try:
            zahl1 = float(eingabe1)
            break  # Eingabe erfolgreich
        except ValueError:
            print("Fehlgeschlagen. Bitte eine gültige Zahl eingeben.")

    # --- Zahl 2 eingeben ---
    while True:
        eingabe2 = input("Geben Sie die zweite Zahl ein (oder 'exit' zum Beenden): ")
        if eingabe2.lower() == "exit":
            print("Programm beendet.")
            exit()
        try:
            zahl2 = float(eingabe2)
            break  # Eingabe erfolgreich
        except ValueError:
            print("Fehlgeschlagen. Bitte eine gültige Zahl eingeben.")

    # --- Operator eingeben ---
    while True:
        operator = input("Wählen Sie die Operation (+, -, *, /, ^, %) oder 'exit': ")
        if operator.lower() == "exit":
            print("Programm beendet.")
            exit()
        if operator not in operatoren:
            print("Fehlgeschlagen. Ungültiger Operator.")
        else:
            break  # gültiger Operator

    # --- Berechnung ---
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        if zahl2 == 0:
            ergebnis = "Fehler: Division durch Null nicht erlaubt."
        else:
            ergebnis = zahl1 / zahl2
    elif operator == "^":
        ergebnis = zahl1 ** zahl2
    elif operator == "%":
        ergebnis = zahl1 % zahl2

    print("Ergebnis:", ergebnis)

