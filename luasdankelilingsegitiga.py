import math

a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

s = (a + b + c) / 2
luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
keliling = a + b + c

print("Luas segitiga:", luas)
print("Keliling segitiga:", keliling)