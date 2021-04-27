# Aufgabe 1:
# Schreiben Sie ein Python-Programm, dass
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient kleiner Zahl durch größere Zahl berechnen und ausgeben (inkl. Nachkommastellen)
benutzer = input("Geben sie ihren Namen ein: ")
print("Hallo,", benutzer)
erste_zahl = float(input("erste Zahl:")) # float (=Cast (Umwandeln einer Zahl)) benötigt, ansonsten wird der Input (erste_Zahl) als String gespeichert
zweite_zahl = float(input("zweite Zahl:"))

# Summe berechnen und ausgeben
summe = erste_zahl + zweite_zahl

print("Summe:", summe)

# Differenz berechnen und ausgeben
if erste_zahl > zweite_zahl:
    differenz = erste_zahl - zweite_zahl
elif erste_zahl < zweite_zahl:
    differenz = zweite_zahl - erste_zahl
else:
    differenz = erste_zahl - zweite_zahl

print("Differenz:", differenz)

# Produkt berechnen und ausgeben
produkt = erste_zahl * zweite_zahl

print("Produkt:", produkt)

# Quotient berechnen und ausgeben
if erste_zahl > zweite_zahl:
    quotient = zweite_zahl / erste_zahl
elif erste_zahl < zweite_zahl:
    quotient = erste_zahl / zweite_zahl
else:
    quotient = zweite_zahl / erste_zahl

print("Quotient:", quotient)