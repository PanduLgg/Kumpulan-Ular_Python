import datetime

class Orang:
    lingkungan = "RT 2/30 Kelurahan Majujaya"
    def __init__(self, nama, tgl):
        self.nama_lengkap = nama
        self.tgl_lahir = tgl

    def umur(self):
        today = datetime.date.today()
        umur = today.year - self.tgl_lahir.year

        if today < datetime.date(today.year, self.tgl_lahir.month, self.tgl_lahir.day):
            umur -= 1

        return umur

    def tulis_deskripsi(self):
        return f"{self.nama_lengkap} lahir pada {self.tgl_lahir.strftime('%A %B %Y')} atau ({self.tgl_lahir}) umur {self.umur()}"

orang1 = Orang(
    "Ahmad",
    datetime.date(1987, 3, 20)
)
orang2 = Orang(
    "Bayu",
    datetime.date(1988, 5, 12)
)

daftar_warga = [orang1, orang2]
for o in daftar_warga:
    print(o.tulis_deskripsi())