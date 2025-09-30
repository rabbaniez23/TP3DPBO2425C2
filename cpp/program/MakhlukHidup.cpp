#ifndef MAKHLUK_HIDUP_CPP
#define MAKHLUK_HIDUP_CPP

#include <iostream>
#include <string>
using namespace std;

class MakhlukHidup {
protected:
    string nama;
    string namaLatin;
    int usiaMaksimal;

public:
    MakhlukHidup(string n="", string latin="", int usia=0) {
        nama = n;
        namaLatin = latin;
        usiaMaksimal = usia;
    }

    void setNama(string n) { nama = n; }
    string getNama() { return nama; }

    void setNamaLatin(string n) { namaLatin = n; }
    string getNamaLatin() { return namaLatin; }

    void setUsiaMaksimal(int u) { usiaMaksimal = u; }
    int getUsiaMaksimal() { return usiaMaksimal; }

    virtual void displayInfo() {
        cout << "Nama             : " << getNama() << endl;
        cout << "Nama Latin       : " << getNamaLatin() << endl;
        cout << "Usia Maksimal    : " << getUsiaMaksimal() << " tahun" << endl;
    }

    virtual ~MakhlukHidup() {}
};


#endif