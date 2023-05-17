#####################
#     Zadatak 3     #
#####################

"""
    Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
    navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
    srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
    Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
    ispiše odgovarajuću poruku.
"""

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