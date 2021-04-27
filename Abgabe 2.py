# mithilfe der Leibnitz-Reihe die Zahl Pi näherungsweise berechnen

name = input("Bitte Namen eingeben:")
print("Hallo", name)

i = int(input("Anzahl der Interationen angeben:"))
zahlIt = 0 # Laufvariable, spiegelt die momentane Anzahl der Interationen wieder
piAnnäh = 0

while zahlIt < i:
    piAnnäh += (-1)**zahlIt/(2*zahlIt+1) # Berechnung der Leibnitz-Reihe
    print("Zwischenwert der Annäherung an Pi:", piAnnäh)
    zahlIt += 1

piAnnäh *= 4 # Am Ende muss die Annäherung noch mit 4 multipliziert werden,  sodass diese laut der Leibnitz-Reihe korrket ist.
print("Annäherung an Pi:", piAnnäh)