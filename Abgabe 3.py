# Ändern bzw. erweitern Sie das Wörterbuch-Beispiel aus der LÜ vom 03.05.2021 so,
# dass Sie wahlweise englische oder deutsche Begriffe eingeben können und das Programm selbtständig
# das jeweils korrespondierende Vokabel findet und, versehen mit einem Hinweis auf die Sprache, ausgibt.

woerterbuch_deutsch = ["Apfel" , "Birne" , "Kirsche" , "Melone" , "Marille" , "Pfirsich"]
woerterbuch_english = ["apple" , "pear" , "cherry" , "melon" , "apricot" , "peach"]



suchbegriff = input("Bitte Suchbegriff eingeben: ")

maxIndexDE = len(woerterbuch_deutsch)
maxIndexEN = len(woerterbuch_english)

i =0
j =0


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