#Funktion zur Lösung des Spieles "Türme von Hanoi"

def Türme_von_hanoi(anzahl, von='A', temporär='B', ziel='C'):
    if anzahl > 0:
        Türme_von_hanoi(anzahl - 1, von, ziel, temporär)
        print("Scheibe {} von {} nach {}".format(anzahl, von, ziel))
        Türme_von_hanoi(anzahl - 1, temporär, von, ziel)
