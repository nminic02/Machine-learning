def total_euro(a, b):
    return a*b

a=float(input("Unesi broj radnih sati:"))
b=float(input("Unesi placenost po satu:"))

print ("Ukupno: %d eura" % total_euro(a, b))