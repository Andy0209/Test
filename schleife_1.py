# Schleifen- /Zählvariable: i, j, k

counter = 10
while counter >=0:
    counter -= 1 # aufpassen wo counter setzten
    print(counter)


# addieren Sie in einer Schleife(!) die Zahlen 1 bis 100 und geben Sie das Ergebnis aus

counter1 = 1
zahl = 0
while counter1 <=100:
    zahl += counter1
    counter1 += 1

print(counter1)
print("Summe:" ,zahl)