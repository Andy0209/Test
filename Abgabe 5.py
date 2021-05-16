# Ändern bzw. erweitern Sie das Wörterbuch-Beispiel aus der LÜ vom 03.05.2021 so,
# dass Sie wahlweise englische oder deutsche Begriffe eingeben können und das Programm selbtständig
# das jeweils korrespondierende Vokabel findet und, versehen mit einem Hinweis auf die Sprache, ausgibt.

woerterbuch_deutsch = {"Apfel": "apple",
                       "Birne": "pear",
                       "Kirsche": "cherry",
                       "Melone": "melon",
                       "Marille": "apricot",
                       "Pfirsich": "peach"
                       }

woerterbuch_english = {"apple": "Apfel",
                       "pear": "Birne",
                       "cherry": "Kirsche",
                       "melon": "Melone",
                       "apricot": "Marille",
                       "peach": "Pfirsich"
                       }

while True:
    try:
        suchbegriff = input("Bitte Suchbegriff eingeben: ")
        
        if suchbegriff in woerterbuch_deutsch: # überprüfen, ob Suchbegriff im Wörterbuch enthalten
            print("Wort im Englischen lautet:", woerterbuch_deutsch[suchbegriff], ", EN")
            break
                
        elif suchbegriff in woerterbuch_english: # überprüfen, ob Suchbegriff im Wörterbuch enthalten
            print("Wort im Deutschen lautet:", woerterbuch_english[suchbegriff], ", DE")
            break
        
        raise KeyError()
            
    except KeyError: # möglicher Fehler: kein Key-Wort -> KeyError
        print("Gesuchtes Wort nicht in den Wörterbüchern enthalten \nBitte neu eingeben\n")

print("\nAuf Wiedersehen \n")
