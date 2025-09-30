# File: Reptil.py

# Import kelas induknya
from MakhlukHidup import MakhlukHidup

class Reptil(MakhlukHidup):
    # Constructor
    def __init__(self, nama="", nama_latin="", usia_maksimal=0, panjang_tubuh=0, jumlah_telur=0, jenis_sisik=""):
        # Panggil constructor dari kelas induk
        super().__init__(nama, nama_latin, usia_maksimal)
        self.__panjang_tubuh = panjang_tubuh
        self.__jumlah_telur = jumlah_telur
        self.__jenis_sisik = jenis_sisik

    # Setter dan Getter khusus Reptil
    def set_panjang_tubuh(self, panjang):
        self.__panjang_tubuh = panjang

    def get_panjang_tubuh(self):
        return self.__panjang_tubuh
    
    def set_jumlah_telur(self, jumlah):
        self.__jumlah_telur = jumlah

    def get_jumlah_telur(self):
        return self.__jumlah_telur

    def set_jenis_sisik(self, jenis):
        self.__jenis_sisik = jenis

    def get_jenis_sisik(self):
        return self.__jenis_sisik

    # Override method display_info dari induk
    def display_info(self):
        print("--- DATA REPTIL ---")
        super().display_info() # Panggil display_info dari induk
        print(f"Panjang Tubuh    : {self.get_panjang_tubuh()} cm")
        print(f"Jumlah Telur     : {self.get_jumlah_telur()}")
        print(f"Jenis Sisik      : {self.get_jenis_sisik()}")