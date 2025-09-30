#include <iostream>
#include <vector>
using namespace std;

#include "Mamalia.cpp"
#include "Reptil.cpp"
#include "Tumbuhan.cpp"
#include "Habitat.cpp"
#include "MakhlukHidup.cpp"


int main() {
    Habitat hutanTropis("Hutan Tropis Kalimantan", "Tropis Basah", 5000);
    Habitat sabanaJawa("Sabana Baluran", "Kering", 250);
    Habitat perairanMuara("Perairan Muara", "Payau", 1000);

    vector<Habitat*> daftarHabitat = { &hutanTropis, &sabanaJawa, &perairanMuara };

    // Hardcode data
    hutanTropis.tambahMakhluk(new Mamalia("Orangutan","Pongo pygmaeus",45,2,75,"Cokelat Kemerahan"), true);
    hutanTropis.tambahMakhluk(new Mamalia("Harimau Sumatra","Panthera tigris sumatrae",25,4,150,"Oranye Belang"), true);
    hutanTropis.tambahMakhluk(new Tumbuhan("Bunga Raflesia","Rafflesia arnoldii",2,1,2,"Serabut (Parasit)"), true);

    sabanaJawa.tambahMakhluk(new Mamalia("Banteng","Bos javanicus",20,4,800,"Hitam"), true);
    sabanaJawa.tambahMakhluk(new Reptil("Komodo","Varanus komodoensis",30,300,20,"Sisik Keras"), true);
    sabanaJawa.tambahMakhluk(new Tumbuhan("Pohon Jati","Tectona grandis",150,40,150,"Tunggang"), true);

    perairanMuara.tambahMakhluk(new Reptil("Buaya Muara","Crocodylus porosus",70,500,40,"Kulit Keras Berduri"), true);
    perairanMuara.tambahMakhluk(new Reptil("Penyu Hijau","Chelonia mydas",80,120,100,"Tempurung Keras"), true);

    cout << "Data hardcode selesai dimuat." << endl;

    while (true) {
        cout << "\n===== MENU MANAJEMEN EKOSISTEM =====" << endl;
        cout << "1. Tambah Data Makhluk Baru" << endl;
        cout << "2. Tampilkan Semua Data Ekosistem" << endl;
        cout << "3. Keluar" << endl;

        int pilihan;
        cout << "Pilih menu (1-3): ";
        cin >> pilihan;

        if (pilihan == 1) {
            cout << "\nPilih Habitat untuk menambahkan makhluk:" << endl;
            for (size_t i=0; i<daftarHabitat.size(); i++) {
                cout << i+1 << ". " << "Habitat ke-" << (i+1) << endl;
            }
            int ph; cin >> ph;
            if (ph < 1 || ph > daftarHabitat.size()) {
                cout << "Pilihan habitat tidak valid!" << endl;
                continue;
            }
            Habitat* habitatTerpilih = daftarHabitat[ph-1];

            cout << "\n--- Pilih Jenis Makhluk ---" << endl;
            cout << "1. Mamalia\n2. Reptil\n3. Tumbuhan" << endl;
            int jenis; cin >> jenis;

            string nama, latin;
            int usia;
            cout << "Masukkan Nama: "; cin.ignore(); getline(cin, nama);
            cout << "Masukkan Nama Latin: "; getline(cin, latin);
            cout << "Masukkan Usia Maksimal (tahun): "; cin >> usia;

            if (jenis == 1) {
                int kaki, berat; string warna;
                cout << "Masukkan Jumlah Kaki: "; cin >> kaki;
                cout << "Masukkan Berat Badan (kg): "; cin >> berat;
                cout << "Masukkan Warna Rambut: "; cin.ignore(); getline(cin, warna);
                habitatTerpilih->tambahMakhluk(new Mamalia(nama, latin, usia, kaki, berat, warna));
            } else if (jenis == 2) {
                int panjang, telur; string sisik;
                cout << "Masukkan Panjang Tubuh (cm): "; cin >> panjang;
                cout << "Masukkan Jumlah Telur: "; cin >> telur;
                cout << "Masukkan Jenis Sisik: "; cin.ignore(); getline(cin, sisik);
                habitatTerpilih->tambahMakhluk(new Reptil(nama, latin, usia, panjang, telur, sisik));
            } else if (jenis == 3) {
                int tinggi, lama; string akar;
                cout << "Masukkan Tinggi Maksimal (meter): "; cin >> tinggi;
                cout << "Masukkan Lama Hidup Rata-rata (tahun): "; cin >> lama;
                cout << "Masukkan Jenis Akar: "; cin.ignore(); getline(cin, akar);
                habitatTerpilih->tambahMakhluk(new Tumbuhan(nama, latin, usia, tinggi, lama, akar));
            } else {
                cout << "Pilihan jenis tidak valid!" << endl;
            }
        }
        else if (pilihan == 2) {
            cout << "\n<<<<< MENAMPILKAN KESELURUHAN DATA EKOSISTEM >>>>>" << endl;
            for (auto h : daftarHabitat) {
                h->tampilkanSemuaMakhluk();
            }
        }
        else if (pilihan == 3) {
            cout << "Terima kasih, program selesai." << endl;
            break;
        }
        else {
            cout << "Pilihan tidak valid!" << endl;
        }
    }

    return 0;
}
