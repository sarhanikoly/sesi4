bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

if bilangan1> bilangan2  and bilangan2  > bilangan3:
    print("Bilangan pertama ({}) lebih besar dari kedua bilangan lainnya.".format(bilangan1))
elif bilangan2> bilangan1 and bilangan2 > bilangan3:
    print("Bilangan kedua ({}) lebih besar dari kedua bilangan lainnya.".format(bilangan2))
elif bilangan3> bilangan1 and bilangan3 > bilangan2:
    print("Bilangan ketiga ({}) lebih besar dari kedua bilangan lainnya.".format(bilangan3))
else:
    print("Ketiga bilangan sama besar.")