#include "MakhlukHidup.cpp"

class Reptil : public MakhlukHidup {
private:
    int panjangTubuh;
    int jumlahTelur;
    string jenisSisik;

public:
    Reptil(string n="", string latin="", int usia=0, int panjang=0, int telur=0, string sisik="") 
        : MakhlukHidup(n, latin, usia) {
        panjangTubuh = panjang;
        jumlahTelur = telur;
        jenisSisik = sisik;
    }
    void setPanjangTubuh(int panjang) { panjangTubuh = panjang; }
    int getPanjangTubuh() { return panjangTubuh; }

    void setJumlahTelur(int telur) { jumlahTelur = telur; }
    int getJumlahTelur() { return jumlahTelur; }

    void setJenisSisik(string sisik) { jenisSisik = sisik; }
    string getJenisSisik() { return jenisSisik; }


    void displayInfo() override {
        cout << "--- DATA REPTIL ---" << endl;
        MakhlukHidup::displayInfo();
        cout << "Panjang Tubuh    : " << getPanjangTubuh()<< " cm" << endl;
        cout << "Jumlah Telur     : " << getJumlahTelur() << endl;
        cout << "Jenis Sisik      : " << getJenisSisik() << endl;
    }
};
