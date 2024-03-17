bilangan = int(input("Masukkan bilangan: "))

if bilangan  % 2 == 0:
    print("Bilangan tersebut adalah genap.")
else:
    print("Bilangan tersebut adalah ganjil.")

if bilangan  > 0:
    print("Bilangan tersebut adalah positif.")
elif bilangan < 0:
    print("Bilangan tersebut adalah negatif.")
else:
    print("Bilangan tersebut adalah nol.")