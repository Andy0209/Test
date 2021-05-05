# Ändern bzw. erweitern Sie das Wörterbuch-Beispiel aus der LÜ vom 03.05.2021 so,
# dass Sie wahlweise englische oder deutsche Begriffe eingeben können und das Programm selbtständig
# das jeweils korrespondierende Vokabel findet und, versehen mit einem Hinweis auf die Sprache, ausgibt.

woerterbuch_deutsch = ["Apfel" , "Birne" , "Kirsche" , "Melone" , "Marille" , "Pfirsich"]
woerterbuch_english = ["apple" , "pear" , "cherry" , "melon" , "apricot" , "peach"]

running = True
while running:
    auswahl = input("Befehl? \n [E]infügen, \n [L]öschen, \n [B]eenden \n [A]bfragen: \n") # \n Zeilenumbruch in der Kommandozeile

    maxIndexDE = len(woerterbuch_deutsch)
    maxIndexEN = len(woerterbuch_english)

    if auswahl == 'E' or auswahl ==  'e':
        sprache = input("Kommt das Wort aus der deutschen Sprache oder englischen Sprache? \n [deutsch] \n [englisch] \n ")
        
        # Wort kommt aus der deutschen Sprache
        if sprache.lower() == 'deutsch':
            wort_de = input("Wie heißt das Wort? ")
            wort_en = input("Wie heißt das Wort im englischen? ")
            stelle = int(input("An welcher Stelle soll das Wort eingefügt werden? "))
            
            woerterbuch_deutsch.insert(stelle - 1, wort_de)
            woerterbuch_english.insert(stelle - 1, wort_en)
            
        # Wort kommt aus der englischen Sprache
        if sprache.lower() == 'englisch':
            wort_en = input("Wie heißt das Wort? ")
            wort_de = input("Wie heißt das Wort im deutschen? ")
            stelle = int(input("An welcher Stelle soll das Wort eingefügt werden? "))
            
            woerterbuch_deutsch.insert(stelle - 1, wort_de)
            woerterbuch_english.insert(stelle - 1, wort_en)
        
        # aktualisierte Wörterbücher ausgeben
        print(woerterbuch_deutsch)
        print(woerterbuch_english)
    
    elif auswahl == 'L' or auswahl == 'l':
        loeschen = input("Welches Wort soll gelöscht werden?" )
        k = 0 # Laufvariable
        l = 0 # Laufvariable
        
        while k < maxIndexDE:
            if loeschen.lower() == woerterbuch_deutsch[k].lower():
                loeschen_en = woerterbuch_english[k]
                
                woerterbuch_deutsch.remove(loeschen)
                woerterbuch_english.remove(loeschen_en)
                break
            k += 1
        
        while l < maxIndexEN:
            if loeschen.lower() == woerterbuch_english[l].lower():
                loeschen_de = woerterbuch_deutsch[l]
                
                woerterbuch_english.remove(loeschen)
                woerterbuch_deutsch.remove(loeschen_de)
                break
            l += 1
        
        # aktualisierte Wörterbücher ausgeben
        print(woerterbuch_deutsch)
        print(woerterbuch_english)
                
    elif auswahl == 'B' or auswahl == 'b':
        running = False
        
    else: # Standardvorgang -> immer mit dem geringsten Risiko
        suchbegriff = input("Bitte Suchbegriff eingeben: ")
        
        i =0 # Laufvariable
        j =0 # Laufvariable
        
        while i < maxIndexDE:    
            if suchbegriff.lower() == woerterbuch_deutsch[i].lower():
                print("Wort im Englischen lautet:", woerterbuch_english[i], ", EN")
                break   
            i += 1

        
        while j < maxIndexEN:    
            if suchbegriff.lower() == woerterbuch_english[j].lower():
                print("Wort im Deutschen lautet:", woerterbuch_deutsch[j], ", DE")
                break   
            j += 1


        if i == maxIndexDE and j == maxIndexEN:
            print("Wort in den Wörterbüchern nicht enthalten")
