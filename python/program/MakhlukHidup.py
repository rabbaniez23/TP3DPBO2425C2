# File: MakhlukHidup.py

class MakhlukHidup:
    # Constructor
    def __init__(self, nama="", nama_latin="", usia_maksimal=0):
        self.__nama = nama
        self.__nama_latin = nama_latin
        self.__usia_maksimal = usia_maksimal

    # Setter dan Getter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    # Setter dan Getter untuk nama_latin
    def set_nama_latin(self, nama_latin):
        self.__nama_latin = nama_latin

    def get_nama_latin(self):
        return self.__nama_latin

    # Setter dan Getter untuk usia_maksimal
    def set_usia_maksimal(self, usia):
        self.__usia_maksimal = usia

    def get_usia_maksimal(self):
        return self.__usia_maksimal

    # Method untuk menampilkan data (akan di-override oleh anak)
    def display_info(self):
        print(f"Nama             : {self.get_nama()}")
        print(f"Nama Latin       : {self.get_nama_latin()}")
        print(f"Usia Maksimal    : {self.get_usia_maksimal()} tahun")