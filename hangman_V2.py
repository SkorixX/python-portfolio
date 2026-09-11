woerter = ["Frankreich", "verdreht", "exzellent", "komisch", "Banane", "Schwimmmeisterschaften", "vollgas", "Meisterwerk", "programmieren", "Abgasuntersuchung"]
import random
geheimwort = random.choice(woerter).lower()
geraten = []
fehler = 0
fehlend = len(set(geheimwort))

def wort_anzeigen(geheimwort, geraten):
    for zeichen in geheimwort:
        if zeichen in geraten:
            print(zeichen, end=" ")
        else:
            print("_", end=" ")
    print(geraten)

while True:
    buchstabe = input("Gib einen Buchstaben ein: ").lower()
    if len(buchstabe) > 1:
        print("Zu viele Zeichen.")
    else:
        if buchstabe in geraten:
            print("Dieser Buchstabe wurde bereits erraten.")
            continue
        else:
            geraten.append(buchstabe)
        if buchstabe in geheimwort:
            print("Ja!")
            fehlend = fehlend - 1
            if fehlend == 0:
                wort_anzeigen(geheimwort, geraten)
                print("Du hast gewonnen!")
                break
        else:
            print("Nein!")
            fehler = fehler + 1
            if fehler == 12:
                wort_anzeigen(geheimwort, geraten)
                print("Du hast verloren!")
                break
            print("du hast bereits", fehler, "Fehler")