class Pegawai:
    honor_per_jam = "30.000"
    def __init__(self, nama, jam_kerja):
        self.nama_asli = nama
        self.jam_hasil = jam_kerja

    def hitung(self):
        honor = int(30000)
        jam = self.jam_hasil
        hasil = honor*jam

        return hasil

    def hasil(self):
        return f"{self.nama_asli} Jam Kerja {self.jam_hasil} Honor Rp.{self.hitung()}"


charlie = Pegawai("Charlie", 8)
steven = Pegawai("Steven", 12)
vander = Pegawai("Vader", 5)
lin = Pegawai("Lin", 2)


daftar_karyawan = [charlie, steven, vander, lin]
for x in daftar_karyawan:
    print(x.hasil())