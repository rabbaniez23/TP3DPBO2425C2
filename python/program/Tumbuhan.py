# File: Tumbuhan.py

# Import kelas induknya
from MakhlukHidup import MakhlukHidup

class Tumbuhan(MakhlukHidup):
    # Constructor
    def __init__(self, nama="", nama_latin="", usia_maksimal=0, tinggi_maksimal=0, lama_hidup=0, jenis_akar=""):
        # Panggil constructor dari kelas induk
        super().__init__(nama, nama_latin, usia_maksimal)
        self.__tinggi_maksimal = tinggi_maksimal
        self.__lama_hidup = lama_hidup
        self.__jenis_akar = jenis_akar
        
    # Setter dan Getter khusus Tumbuhan
    def set_tinggi_maksimal(self, tinggi):
        self.__tinggi_maksimal = tinggi

    def get_tinggi_maksimal(self):
        return self.__tinggi_maksimal

    def set_lama_hidup(self, lama):
        self.__lama_hidup = lama

    def get_lama_hidup(self):
        return self.__lama_hidup

    def set_jenis_akar(self, jenis):
        self.__jenis_akar = jenis

    def get_jenis_akar(self):
        return self.__jenis_akar

    # Override method display_info dari induk
    def display_info(self):
        print("--- DATA TUMBUHAN ---")
        super().display_info() # Panggil display_info dari induk
        print(f"Tinggi Maksimal  : {self.get_tinggi_maksimal()} meter")
        print(f"Lama Hidup Rata2 : {self.get_lama_hidup()} tahun")
        print(f"Jenis Akar       : {self.get_jenis_akar()}")