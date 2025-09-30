# File: Mamalia.py

# Import kelas induknya
from MakhlukHidup import MakhlukHidup

class Mamalia(MakhlukHidup):
    # Constructor
    def __init__(self, nama="", nama_latin="", usia_maksimal=0, jumlah_kaki=0, berat_badan=0, warna_rambut=""):
        # Panggil constructor dari kelas induk
        super().__init__(nama, nama_latin, usia_maksimal)
        self.__jumlah_kaki = jumlah_kaki
        self.__berat_badan = berat_badan
        self.__warna_rambut = warna_rambut

    # Setter dan Getter khusus Mamalia
    def set_jumlah_kaki(self, jumlah):
        self.__jumlah_kaki = jumlah
        
    def get_jumlah_kaki(self):
        return self.__jumlah_kaki

    def set_berat_badan(self, berat):
        self.__berat_badan = berat

    def get_berat_badan(self):
        return self.__berat_badan

    def set_warna_rambut(self, warna):
        self.__warna_rambut = warna

    def get_warna_rambut(self):
        return self.__warna_rambut

    # Override method display_info dari induk
    def display_info(self):
        print("--- DATA MAMALIA ---")
        super().display_info()  # Panggil display_info dari induk
        print(f"Jumlah Kaki      : {self.get_jumlah_kaki()}")
        print(f"Berat Badan      : {self.get_berat_badan()} kg")
        print(f"Warna Rambut     : {self.get_warna_rambut()}")