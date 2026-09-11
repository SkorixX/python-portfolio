import random
geheimzahl = random.randint(1, 10)

while True:
    tipp = int(input("Gib eine Zahl zwischen 1 und 10 ein: "))
    if tipp < geheimzahl:
        print("Die Zahl ist zu klein.")
    elif tipp > geheimzahl:
        print("Die Zahl ist zu groß.")
    else:
        print("Glückwunsch! gschafft.")
        break