# Ändern bzw. erweitern Sie das Wörterbuch-Beispiel aus der LÜ vom 03.05.2021 so,
# dass Sie wahlweise englische oder deutsche Begriffe eingeben können und das Programm selbtständig
# das jeweils korrespondierende Vokabel findet und, versehen mit einem Hinweis auf die Sprache, ausgibt.

# 
# 
# Funktion zur Eingabe des Suchbegriffs bzw. Wortes
# Funktion zur Suche
# Funktion zur Ausgabe

woerterbuch_deutsch = ["Apfel" , "Birne" , "Kirsche" , "Melone" , "Marille" , "Pfirsich"]
woerterbuch_english = ["apple" , "pear" , "cherry" , "melon" , "apricot" , "peach"]


def befehl_eingabe ():
    korrekt = False
    while korrekt == False:
        auswahl = input( "\n\nBefehl? \n [E]infügen, \n [L]öschen, \n [B]eenden \n [A]bfragen: \n") # \n Zeilenumbruch in der Kommandozeile
        auswahl = auswahl.upper()
        
        if auswahl == "E":
            korrekt = True
            return auswahl
        elif auswahl == "L":
            korrekt = True
            return auswahl
        elif auswahl == "B":
            korrekt = True
            return auswahl
        elif auswahl == "A":
            korrekt = True
            return auswahl


def suchen():
    suchbegriff = input("Bitte Suchbegriff eingeben: ")
    return suchbegriff


def suche_dt(wort):
    i = 0
    vorhanden = 0
    
    while i < len(woerterbuch_deutsch):
        if woerterbuch_deutsch[i].lower() == wort.lower():
            vorhanden = True
            break
        i += 1
        
    if vorhanden == True:
        return True
    else:
        return False


def suche_en(wort):
    i = 0
    vorhanden = 0
    
    while i < len(woerterbuch_english):
        if woerterbuch_english[i].lower() == wort.lower():
            vorhanden = True
            break
        i += 1
        
    if vorhanden == True:
        return True
    else:
        return False


def einfuegen_dt():
    wort_de = input("Wie heißt das Wort? ")
    wort_en = input("Wie heißt das Wort im englischen? ")
    stelle = int(input("An welcher Stelle soll das Wort eingefügt werden? "))
    
    woerterbuch_deutsch.insert(stelle - 1, wort_de)
    woerterbuch_english.insert(stelle - 1, wort_en.lower())


def einfuegen_en():
    wort_en = input("Wie heißt das Wort? ")
    wort_de = input("Wie heißt das Wort im deutschen? ")
    stelle = int(input("An welcher Stelle soll das Wort eingefügt werden? "))
            
    woerterbuch_deutsch.insert(stelle - 1, wort_de)
    woerterbuch_english.insert(stelle - 1, wort_en.lower())

def einfuegen():
    sprache = input("Kommt das Wort aus der deutschen Sprache oder englischen Sprache? \n [deutsch] \n [englisch] \n ")
        
    # Wort kommt aus der deutschen Sprache
    if sprache.lower() == "deutsch":
        einfuegen_dt()
            
    # Wort kommt aus der englischen Sprache
    elif sprache.lower() == "englisch":
        einfuegen_en()
    
    else:
        print("Falsche Eingabe")

    # aktualisierte Wörterbücher ausgeben
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
        
    return True


def loeschen():
    wort_loeschen = suchen()     
    
    if suche_dt(wort_loeschen) == True:
        k = 0 # Laufvariable
        
        while k < len(woerterbuch_deutsch):
            if wort_loeschen.lower() == woerterbuch_deutsch[k].lower():
                wort_loeschen_en = woerterbuch_english[k]
                
                woerterbuch_deutsch.remove(wort_loeschen)
                woerterbuch_english.remove(wort_loeschen_en)
                break
            k += 1
    
    elif suche_en(wort_loeschen) == True:
        k = 0 # Laufvariable
        
        while k < len(woerterbuch_english):
            if wort_loeschen.lower() == woerterbuch_english[k].lower():
                wort_loeschen_dt = woerterbuch_deutsch[k]
                
                woerterbuch_english.remove(wort_loeschen)
                woerterbuch_deutsch.remove(wort_loeschen_dt)
                break
            k += 1
        
    # aktualisierte Wörterbücher ausgeben
    print("\n\n aktualisierte Wörterbücher: \n")
    print(woerterbuch_deutsch)
    print(woerterbuch_english)


def ausgeben():
    wort_suchen = suchen()
    
    if suche_dt(wort_suchen) == True:
        i =0 # Laufvariable
        
        while i < len(woerterbuch_deutsch):
            if wort_suchen.lower() == woerterbuch_deutsch[i].lower():
                print("Wort im Englischen lautet:", woerterbuch_english[i], ", EN")
                break   
            i += 1
    
    elif suche_en(wort_suchen) == True:
        i =0 # Laufvariable
        
        while i < len(woerterbuch_english):
            if wort_suchen.lower() == woerterbuch_english[i].lower():
                print("Wort im Deutschen lautet:", woerterbuch_deutsch[i], ", DE")
                break   
            i += 1
        

    elif suche_dt(wort_suchen) == False and suche_en(wort_suchen) == False:
        print("Wort in den Wörterbüchern nicht enthalten")





running = True
while running:
    maxIndexDE = len(woerterbuch_deutsch)
    maxIndexEN = len(woerterbuch_english)
    
    kommando = befehl_eingabe()
    
    if kommando == "E":
        einfuegen()
    
    elif kommando == "L":
        loeschen()
    
    elif kommando == "B":
        print("Auf Wiedersehen")
        running = False
    
    elif kommando == "A":
        ausgeben()


