

brojevi = []

while True:
    value = input("Unesite broj: ")
    try:
        brojevi.append(float(value))
    except ValueError:
        if (value == "Done"):
            break

        print("'%s' Pogrešan unos!" % value)
        continue

print("Uneti brojevi '%d'" % len(brojevi))
print("Srednja vrijednost brojeva '%d'" % (sum(brojevi) / len(brojevi)))
print("Minimalna vrijednost '%d'" % min(brojevi))
print("Masimalna vrijednost'%d'" % max(brojevi))
print(sorted(brojevi))
