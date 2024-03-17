class Anggota:
    def __init__(self, jenis_kelamin, berat_badan, tinggi_badan, usia, nilai_rata_rata, memiliki_skill, memiliki_cacat):
        self.jenis_kelamin = jenis_kelamin
        self.berat_badan = berat_badan
        self.tinggi_badan = tinggi_badan
        self.usia = usia
        self.nilai_rata_rata = nilai_rata_rata
        self.memiliki_skill = memiliki_skill
        self.memiliki_cacat = memiliki_cacat

    def cek_kelayakan(self):
        if self.memiliki_cacat:
            return False
        
        if self.jenis_kelamin.lower() == 'perempuan':
            if self.berat_badan >= 45 and self.berat_badan <= 50 and self.tinggi_badan >= 165 and self.usia < 20:
                return True
        elif self.jenis_kelamin.lower() == 'laki-laki':
            if self.berat_badan <= 70 and self.tinggi_badan >= 170 and self.usia <= 25:
                return True
        
        if self.nilai_rata_rata >= 90 and self.usia < 30:
            return True
        
        if self.memiliki_skill and not self.memiliki_cacat:
            return True
        
        return False


def main():
    jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")
    berat_badan = float(input("Berat Badan (kg): "))
    tinggi_badan = float(input("Tinggi Badan (cm): "))
    usia = int(input("Usia: "))
    nilai_rata_rata = float(input("Nilai Rata-rata Akademis: "))
    memiliki_skill = input("Apakah memiliki skill (y/n): ")
    memiliki_cacat = input("Apakah memiliki cacat (y/n): ")

    if memiliki_skill.lower() == 'y':
        memiliki_skill = True
    else:
        memiliki_skill = False 
    
    if memiliki_cacat.lower() == 'y':
        memiliki_cacat = True
    else:
        memiliki_cacat = False

    anggota = Anggota(jenis_kelamin, berat_badan, tinggi_badan, usia, nilai_rata_rata, memiliki_skill, memiliki_cacat)
    if anggota.cek_kelayakan():
        print("\nSelamat! Anda layak menjadi anggota Organisasi X.")
    else:
        print("\nMaaf, Anda tidak memenuhi syarat untuk menjadi anggota Organisasi X.")


if __name__ == "__main__":
    main()
