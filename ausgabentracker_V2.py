kategorien = [
    "Nahrung", 
    "Auto", 
    "Klamotten", 
    "Klamotten kids", 
    "Freizeit", 
    "Haushalt", 
    "Wohnung", 
    "Versicherungen", 
    "auswärts Essen", 
    "Kids", 
    "Streaming"
] 

ausgaben = [
]

menue = [
    "Budget eingeben",
    "Budget anzeigen",
    "Ausgabe hinzufügen",
    "Ausgaben anzeigen",
    "Kategorie hinzufügen",
    "Beenden"
]

def budget_eingeben():
    budget = float(input("Wie hoch soll dein Budget sein? ").replace("Euro", "").replace("€", "").replace(",", "."))
    return budget

def budget_anzeigen(budget, gesamt):
    if budget is None:
        print("Es wurde noch kein Budget erfasst")
    else:
        verbleibend = verbleibende_ausgaben(budget, gesamt)
        print("Dein Gesamtbudget liegt bei", f"{budget:.2f}", "€")
        print("Verbleibend:", f"{verbleibend:.2f}", "€")

def ausgabe_hinzufuegen(kategorien, ausgaben):
    while True:
        for nummer, kategorie in enumerate(kategorien, start=1):
            print(nummer, kategorie)

        print(len(kategorien) + 1, "Neue Kategorie hinzufügen")

        try:
            auswahl = int(input("Zu welcher Kategorie gehört dein Einkauf? "))
        except ValueError:
            print("Unbekannte Eingabe. Bitte gib eine Zahl an.")
            continue

        if auswahl > len(kategorien) + 1 or auswahl <= 0:
            print("Die Auswahl existiert nicht. Bitte gib eine Zahl zwischen 1 und", len(kategorien) + 1, "an.")
            continue

        if auswahl == len(kategorien) + 1:
            neue_kategorie(kategorien)
            continue
    
        ausgewählt = kategorien[auswahl - 1]
        break

    while True:
        betrag = float(input("Welchen Betrag hast du ausgegeben? ").replace("Euro", "").replace("€", "").replace(",", "."))
        if betrag <= 0:
            print("Ungültiger Betrag")
        else: 
            break
    ausgabe = {
    "Betrag": betrag,
    "Kategorie": ausgewählt,
    }
    ausgaben.append(ausgabe)
    return ausgabe      

def ausgaben_anzeigen(ausgaben):
    if len(ausgaben) == 0:
        print("Es wurde noch keine Ausgabe erfasst.")
    else:
        for ausgabe in ausgaben:
            print(ausgabe["Kategorie"], "-", f"{ausgabe["Betrag"]:.2f}", "€")

    gesamt = gesamtausgaben(ausgaben)
    print("Gesamtausgaben:", f"{gesamt:.2f}", "€")

def neue_kategorie(kategorien):
    name_kategorie = input("Wie soll die neue Kategorie heissen? ")
    kategorien.append(name_kategorie)
    return name_kategorie

def verbleibende_ausgaben(budget, gesamt): 
    
    verbleibend = budget - gesamt
    return verbleibend

def gesamtausgaben(ausgaben):
    gesamt = 0
    for ausgabe in ausgaben:
        gesamt += ausgabe["Betrag"]

    return gesamt

budget = None

while True:
    for nummer, punkt in enumerate(menue, start=1):
        print(nummer, punkt)
    auswahl = int(input("Wähle eine Aktion aus: "))

    if auswahl == 1:
        budget = budget_eingeben()
        print("Dein Budget in höhe von", f"{budget:.2f}", "€ wurde erfasst.")
    elif auswahl == 2:
        gesamt = gesamtausgaben(ausgaben)
        budget_anzeigen(budget, gesamt)
    elif auswahl == 3:
        ausgabe = ausgabe_hinzufuegen(kategorien, ausgaben)
        print("Deine Ausgabe in höhe von", f"{ausgabe["Betrag"]:.2f}", "€ wurde erfasst.")
    elif auswahl == 4:
        ausgaben_anzeigen(ausgaben)
    elif auswahl == 5:
        name = neue_kategorie(kategorien)
        print("Die neue Kategorie", name, "wurde hinzugefügt.")
    elif auswahl == 6:
        break




