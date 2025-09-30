#include "MakhlukHidup.cpp"
#include <iostream>
#include <string>

using namespace std;

class Tumbuhan : public MakhlukHidup {
private:
    int tinggiMaksimal;
    int lamaHidup;
    string jenisAkar;

public:
    Tumbuhan(string n="", string latin="", int usia=0, int tinggi=0, int lama=0, string akar="") 
        : MakhlukHidup(n, latin, usia) {
        tinggiMaksimal = tinggi;
        lamaHidup = lama;
        jenisAkar = akar;
    }

    void setTinggiMaksimal(int tinggi) { tinggiMaksimal = tinggi; }
    int getTinggiMaksimal() { return tinggiMaksimal; }

    void setLamaHidup(int lama) { lamaHidup = lama; }
    int getLamaHidup() { return lamaHidup; }

    void setJenisAkar(string akar) { jenisAkar = akar; }
    string getJenisAkar() { return jenisAkar; }


    void displayInfo() override {
        cout << "--- DATA TUMBUHAN ---" << endl;
        MakhlukHidup::displayInfo();
        cout << "Tinggi Maksimal  : " << getTinggiMaksimal() << " meter" << endl;
        cout << "Lama Hidup Rata2 : " << getLamaHidup() << " tahun" << endl;
        cout << "Jenis Akar       : " << getJenisAkar() << endl; // <-- Perbaikan di sini
    }
};