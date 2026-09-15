kategorien = ["Nahrung", "Auto", "Klamotten", "Klamotten kids", "Freizeit", "Haushalt", "Wohnung", "Versicherungen", "auswärts Essen", "Kids", "Streaming"] 

ausgaben = []

def neue_kategorie():
    kategorien.append(input("Die neue kategorie heisst: "))

def verbleibende_ausgaben(budget, gesamt):
    
    verbleibend = budget - gesamt
    return verbleibend

def gesamtausgaben(ausgaben):
    gesamt = 0
    for ausgabe in ausgaben:
        gesamt += ausgabe["Betrag"]

    return gesamt

new_budget = input("möchtest du ein Budget erfassen? ").lower()
if new_budget == "yes":
    budget = float(input("Wie hoch soll dein Budget sein? "))

while True:
    for nummer, kategorie in enumerate(kategorien, start=1):
        print(nummer, kategorie)

    print(len(kategorien) + 1, "Neue Kategorie hinzufügen")

    try:
        auswahl = int(input("zu welcher Kategorie gehört dein einkauf? "))
    except ValueError:
        print("unbekannte Eingabe. Bitte gib eine Zahl an")
        continue

    if auswahl > len(kategorien) + 1 or auswahl <= 0:
        print("Die Auswahl existiert nicht. Bitte gib eine Zahl zwischen 1 und", len(kategorien) + 1, "an")
        continue

    if auswahl == len(kategorien) + 1:
        neue_kategorie()
        continue
    
    ausgewählt = kategorien[auswahl - 1]
    
    while True:
        betrag = float(input("Welchen Betrag hast du ausgegeben? "))
        if betrag <= 0:
            print("ungültiger betrag")
        else: 
            break
    ausgabe = {
    "Betrag": betrag,
        "Kategorie": ausgewählt,
    }
    ausgaben.append(ausgabe)
    gesamt = gesamtausgaben(ausgaben)
    if new_budget == "yes":
        rest = verbleibende_ausgaben(budget, gesamt)
        if rest > 0:
            print("du hast noch", f"{rest:.2f}", "€ in deinem budget")
        elif rest == 0:
            print("dein Budget ist aufgebraucht")
        else:
            print("Du bist", f"{abs(rest):.2f}", "über deinem budget")
    
    weiter = input("möchtest du einen weiteren Betrag eingeben? ")

    if weiter != "y":
        for ausgabe in ausgaben:
            print(ausgabe["Kategorie"], "-", f"{ausgabe["Betrag"]:.2f}", "€")
        print("Gesamtausgaben:", f"{gesamt:.2f}", "€")
        break

if new_budget == "yes":
    if gesamt == budget:
        print("Du hast dein Budget erreicht.")
    elif gesamt > budget:
        print("Du hast", f"{gesamt - budget:.2f}", "€ zu viel ausgegeben.")
    else:
        print("Du hast noch", f"{budget - gesamt:.2f}", "€ im budget.")





    
    
    