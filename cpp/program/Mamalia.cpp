#include "MakhlukHidup.cpp"

class Mamalia : public MakhlukHidup {
private:
    int jumlahKaki;
    int beratBadan;
    string warnaRambut;

public:
    Mamalia(string n="", string latin="", int usia=0, int kaki=0, int berat=0, string warna="") 
        : MakhlukHidup(n, latin, usia) {
        jumlahKaki = kaki;
        beratBadan = berat;
        warnaRambut = warna;
    }

void setJumlahKaki(int kaki) { jumlahKaki = kaki; }
int getJumlahKaki() { return jumlahKaki; }

void setBeratBadan(int berat) { beratBadan = berat; }
int getBeratBadan() { return beratBadan; }

void setWarnaRambut(string warna) { warnaRambut = warna; }
string getWarnaRambut() { return warnaRambut; }


    void displayInfo() override {
        cout << "--- DATA MAMALIA ---" << endl;
        MakhlukHidup::displayInfo();
        cout << "Jumlah Kaki      : " << getJumlahKaki() << endl;
        cout << "Berat Badan      : " << getBeratBadan() << " kg" << endl;
        cout << "Warna Rambut     : " << getWarnaRambut() << endl;
    }
};
