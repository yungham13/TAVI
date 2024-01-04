class Sosial:
    def __init__(self, nama, lokasi):
        self.__nama = nama
        self.lokasi = lokasi

    def dapat_info(self):
        return f"{self.__nama} yang terletak di {self.lokasi}"

class Komunitas(Sosial):
    def __init__(self, nama, lokasi, nama_komunitas):
        super().__init__(nama, lokasi)
        self.nama_komunitas = nama_komunitas
        self.anggota = []

    def tambah_anggota(self, individu):
        self.anggota.append(individu)

class Individu(Sosial):
    def __init__(self, nama, usia):
        super().__init__(nama, "Belum Ditentukan")  # Lokasi default
        self._usia = usia

    def dapat_info(self):
        return f"{self._Sosial__nama}, usia {self._usia} tahun"

    @property
    def nama(self):
        return self._Sosial__nama  # Mengakses atribut private dengan name mangling

class Keluarga(Individu):
    def __init__(self, kepala_keluarga, jumlah_anggota):
        super().__init__(kepala_keluarga, 20)  
        self.kepala_keluarga = kepala_keluarga
        self.jumlah_anggota = jumlah_anggota

    def hitung_anggaran(self):
        # Beberapa perhitungan berdasarkan jumlah anggota keluarga
        return self.jumlah_anggota * 500000

# Penggunaan contoh
sosial_obj = Sosial("Klub Sosial", "Pusat Kota")
print(sosial_obj.dapat_info())

komunitas_obj = Komunitas("Komunitas Lokal", "Pinggiran", "Komunitas Ceria")
komunitas_obj.tambah_anggota(Individu("ilham", 25))
komunitas_obj.tambah_anggota(Individu("ibra", 30))
print(komunitas_obj.dapat_info())
print(f"Anggota komunitas: {[anggota.dapat_info() for anggota in komunitas_obj.anggota]}")

keluarga_obj = Keluarga("rama", 4)
print(keluarga_obj.dapat_info())
print(f"Anggaran untuk keluarga: Rp{keluarga_obj.hitung_anggaran()}")
