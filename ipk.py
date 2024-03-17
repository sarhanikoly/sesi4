def hitung_bobot(nilai):
    if nilai >= 85:
        return 4.0
    elif nilai >= 80:
        return 3.7
    elif nilai >= 75:
        return 3.3
    elif nilai >= 70:
        return 3.0
    elif nilai >= 65:
        return 2.7
    elif nilai >= 60:
        return 2.3
    elif nilai >= 55:
        return 2.0
    elif nilai >= 50:
        return 1.7
    elif nilai >= 40:
        return 1.0
    else:
        return 0.0

def main():
    print("Masukkan nilai untuk setiap mata kuliah:")
    mata_kuliah = ['Algoritma', 'Perancangan Objek', 'Kalkulus', 'Etika Profesi', 'Databases', 'English 1']
    nilai_mata_kuliah = {}
    total_bobot = 0
    total_sks = 0

    for matkul in mata_kuliah:
        nilai = float(input(f"Masukkan nilai untuk {matkul}: "))
        sks = float(input(f"Masukkan jumlah SKS untuk {matkul}: "))
        bobot = hitung_bobot(nilai)
        nilai_mata_kuliah[matkul] = (bobot, sks)
        total_bobot += bobot * sks
        total_sks += sks

    if total_sks == 0:
        print("Total SKS tidak boleh nol. Perhitungan IPK tidak dapat dilakukan.")
    else:
        ipk = total_bobot / total_sks
        print(f"IPK Anda untuk semester ini adalah: {ipk:.2f}")

if __name__ == "__main__":
    main()