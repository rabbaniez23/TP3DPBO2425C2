# File: main.py

from Mamalia import Mamalia
from Reptil import Reptil
from Tumbuhan import Tumbuhan
from Habitat import Habitat

def main():
    # --- BUAT BEBERAPA OBJEK HABITAT ---
    hutan_tropis = Habitat("Hutan Tropis Kalimantan", "Tropis Basah", 5000)
    sabana_jawa = Habitat("Sabana Baluran", "Kering", 250)
    perairan_muara = Habitat("Perairan Muara", "Payau", 1000)

    # Simpan semua habitat dalam sebuah list untuk kemudahan pengelolaan
    daftar_habitat = [hutan_tropis, sabana_jawa, perairan_muara]

    # ==========================================================
    # --- DATA HARDCODE UNTUK TESTING (Didistribusikan & Tanpa Pesan) ---
    # ==========================================================
    
    # Menambahkan data ke Hutan Tropis
    hutan_tropis.tambah_makhluk(Mamalia("Orangutan", "Pongo pygmaeus", 45, 2, 75, "Cokelat Kemerahan"), silent=True)
    hutan_tropis.tambah_makhluk(Mamalia("Harimau Sumatra", "Panthera tigris sumatrae", 25, 4, 150, "Oranye Belang"), silent=True)
    hutan_tropis.tambah_makhluk(Tumbuhan("Bunga Raflesia", "Rafflesia arnoldii", 2, 1, 2, "Serabut (Parasit)"), silent=True)
    hutan_tropis.tambah_makhluk(Tumbuhan("Anggrek Bulan", "Phalaenopsis amabilis", 5, 1, 5, "Epifit"), silent=True)
    hutan_tropis.tambah_makhluk(Tumbuhan("Kantong Semar", "Nepenthes", 10, 2, 10, "Serabut"), silent=True)
    
    # Menambahkan data ke Sabana Jawa
    sabana_jawa.tambah_makhluk(Mamalia("Banteng", "Bos javanicus", 20, 4, 800, "Hitam"), silent=True)
    sabana_jawa.tambah_makhluk(Reptil("Komodo", "Varanus komodoensis", 30, 300, 20, "Sisik Keras"), silent=True)
    sabana_jawa.tambah_makhluk(Tumbuhan("Pohon Jati", "Tectona grandis", 150, 40, 150, "Tunggang"), silent=True)

    # Menambahkan data ke Perairan Muara
    perairan_muara.tambah_makhluk(Reptil("Buaya Muara", "Crocodylus porosus", 70, 500, 40, "Kulit Keras Berduri"), silent=True)
    perairan_muara.tambah_makhluk(Reptil("Penyu Hijau", "Chelonia mydas", 80, 120, 100, "Tempurung Keras"), silent=True)

    print("Data hardcode untuk beberapa habitat selesai dimuat.")
    # ==========================================================
    
    while True:
        print("\n===== MENU MANAJEMEN EKOSISTEM =====")
        print("1. Tambah Data Makhluk Baru")
        print("2. Tampilkan Semua Data Ekosistem")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            # --- MENU TAMBAH DATA DENGAN PILIHAN HABITAT ---
            print("\nPilih Habitat untuk menambahkan makhluk:")
            for i, habitat in enumerate(daftar_habitat):
                print(f"{i+1}. {habitat.get_nama_habitat()}")
            
            try:
                pilihan_habitat = int(input(f"Pilih habitat (1-{len(daftar_habitat)}): "))
                if 1 <= pilihan_habitat <= len(daftar_habitat):
                    habitat_terpilih = daftar_habitat[pilihan_habitat - 1]
                    
                    # Proses input data makhluk (sama seperti sebelumnya)
                    print("\n--- Pilih Jenis Makhluk ---")
                    print("1. Mamalia\n2. Reptil\n3. Tumbuhan")
                    jenis = input("Pilih jenis (1-3): ")
                    
                    nama = input("Masukkan Nama: ")
                    nama_latin = input("Masukkan Nama Latin: ")
                    usia_maksimal = int(input("Masukkan Usia Maksimal (tahun): "))

                    makhluk_baru = None
                    if jenis == '1':
                        jumlah_kaki = int(input("Masukkan Jumlah Kaki: "))
                        berat_badan = int(input("Masukkan Berat Badan (kg): "))
                        warna_rambut = input("Masukkan Warna Rambut: ")
                        makhluk_baru = Mamalia(nama, nama_latin, usia_maksimal, jumlah_kaki, berat_badan, warna_rambut)
                    elif jenis == '2':
                        panjang_tubuh = int(input("Masukkan Panjang Tubuh (cm): "))
                        jumlah_telur = int(input("Masukkan Jumlah Telur: "))
                        jenis_sisik = input("Masukkan Jenis Sisik: ")
                        makhluk_baru = Reptil(nama, nama_latin, usia_maksimal, panjang_tubuh, jumlah_telur, jenis_sisik)
                    elif jenis == '3':
                        tinggi_maksimal = int(input("Masukkan Tinggi Maksimal (meter): "))
                        lama_hidup = int(input("Masukkan Lama Hidup Rata-rata (tahun): "))
                        jenis_akar = input("Masukkan Jenis Akar: ")
                        makhluk_baru = Tumbuhan(nama, nama_latin, usia_maksimal, tinggi_maksimal, lama_hidup, jenis_akar)
                    else:
                        print("Pilihan jenis tidak valid!")
                        continue
                    
                    # Menambahkan ke habitat yang dipilih (tanpa 'silent=True' agar pesan muncul)
                    habitat_terpilih.tambah_makhluk(makhluk_baru)
                else:
                    print("Pilihan habitat tidak valid!")
            except ValueError:
                print("Input harus berupa angka!")

        elif pilihan == '2':
            # --- MENAMPILKAN DATA DARI SEMUA HABITAT ---
            print("\n<<<<< MENAMPILKAN KESELURUHAN DATA EKOSISTEM >>>>>")
            for habitat in daftar_habitat:
                habitat.tampilkan_semua_makhluk()
            print("\n<<<<< SELESAI MENAMPILKAN DATA >>>>>")

        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()