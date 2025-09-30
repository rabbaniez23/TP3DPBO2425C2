#include <iostream>
#include <string>
#include <vector>
using namespace std;

#include "MakhlukHidup.cpp"

class Habitat {
private:
    string namaHabitat;
    string tipeIklim;
    int luasArea;
    vector<MakhlukHidup*> daftarMakhluk;

public:
    Habitat(string nama="", string iklim="", int luas=0) {
        namaHabitat = nama;
        tipeIklim = iklim;
        luasArea = luas;
    }

    void setNamaHabitat(string nama) { namaHabitat = nama; }
    string getNamaHabitat() { return namaHabitat; }

    void setTipeIklim(string iklim) { tipeIklim = iklim; }
    string getTipeIklim() { return tipeIklim; }

    void setLuasArea(int luas) { luasArea = luas; }
    int getLuasArea() { return luasArea; }

    void tambahMakhluk(MakhlukHidup* m, bool silent=false) {
        daftarMakhluk.push_back(m);
        if (!silent) {
            cout << "\n-> '" << m->getNama() << "' berhasil ditambahkan ke habitat '" << getNamaHabitat() << "'." << endl;
        }
    }

    void tampilkanSemuaMakhluk() {
        cout << "\n==================== HABITAT: " << getNamaHabitat() << " ====================" << endl;
        cout << "(Tipe Iklim: " << getTipeIklim()<< ", Luas: " << getLuasArea() << " km^2)" << endl;
        cout << "-------------------------------------------------------------" << endl;

        if (daftarMakhluk.empty()) {
            cout << "Habitat ini masih kosong." << endl;
        } else {
            for (size_t i=0; i<daftarMakhluk.size(); i++) {
                cout << "\n--- Makhluk ke-" << (i+1) << " ---" << endl;
                daftarMakhluk[i]->displayInfo();
            }
        }
    }
};
