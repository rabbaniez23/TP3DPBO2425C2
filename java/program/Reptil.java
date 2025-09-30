public class Reptil extends MakhlukHidup {
    private int panjangTubuh;
    private int jumlahTelur;
    private String jenisSisik;

    public Reptil(String nama, String namaLatin, int usiaMaksimal,
                  int panjangTubuh, int jumlahTelur, String jenisSisik) {
        super(nama, namaLatin, usiaMaksimal);
        this.panjangTubuh = panjangTubuh;
        this.jumlahTelur = jumlahTelur;
        this.jenisSisik = jenisSisik;
    }

    public int getPanjangTubuh() { return panjangTubuh; }
    public int getJumlahTelur() { return jumlahTelur; }
    public String getJenisSisik() { return jenisSisik; }

    public void setPanjangTubuh(int panjangTubuh) { this.panjangTubuh = panjangTubuh; }
    public void setJumlahTelur(int jumlahTelur) { this.jumlahTelur = jumlahTelur; }
    public void setJenisSisik(String jenisSisik) { this.jenisSisik = jenisSisik; }


    @Override
    public void displayInfo() {
        System.out.println("--- DATA REPTIL ---");
        super.displayInfo();
        System.out.println("Panjang Tubuh    : " + panjangTubuh + " cm");
        System.out.println("Jumlah Telur     : " + jumlahTelur);
        System.out.println("Jenis Sisik      : " + jenisSisik);
    }
}
