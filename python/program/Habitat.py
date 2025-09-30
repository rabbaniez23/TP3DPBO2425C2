# File: Habitat.py

class Habitat:
    # Constructor
    def __init__(self, nama_habitat="", tipe_iklim="", luas_area=0):
        self.__nama_habitat = nama_habitat
        self.__tipe_iklim = tipe_iklim
        self.__luas_area = luas_area
        self.__daftar_makhluk = []

    # --- SETTER & GETTER (Tidak ada perubahan) ---
    def set_nama_habitat(self, nama):
        self.__nama_habitat = nama
        
    def get_nama_habitat(self):
        return self.__nama_habitat

    def set_tipe_iklim(self, tipe):
        self.__tipe_iklim = tipe

    def get_tipe_iklim(self):
        return self.__tipe_iklim
    
    def set_luas_area(self, luas):
        self.__luas_area = luas

    def get_luas_area(self):
        return self.__luas_area

    # --- METHOD UTAMA (Perubahan di sini) ---
    # Menambah parameter 'silent' untuk mengontrol pesan output
    def tambah_makhluk(self, makhluk, silent=False):
        self.__daftar_makhluk.append(makhluk)
        if not silent:
            print(f"\n-> '{makhluk.get_nama()}' berhasil ditambahkan ke habitat '{self.get_nama_habitat()}'.")

    def tampilkan_semua_makhluk(self):
        # Header untuk setiap habitat
        print(f"\n{'='*20} HABITAT: {self.get_nama_habitat().upper()} {'='*20}")
        print(f"(Tipe Iklim: {self.get_tipe_iklim()}, Luas: {self.get_luas_area()} km^2)")
        print("-" * (42 + len(self.get_nama_habitat())))
        
        if not self.__daftar_makhluk:
            print("Habitat ini masih kosong.")
        else:
            for i, makhluk in enumerate(self.__daftar_makhluk):
                print(f"\n--- Makhluk ke-{i+1} ---")
                makhluk.display_info()