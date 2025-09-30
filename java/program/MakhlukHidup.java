public class MakhlukHidup {
    protected String nama;
    protected String namaLatin;
    protected int usiaMaksimal;

    public MakhlukHidup(String nama, String namaLatin, int usiaMaksimal) {
        this.nama = nama;
        this.namaLatin = namaLatin;
        this.usiaMaksimal = usiaMaksimal;
    }

    public String getNama() { return nama; }
    public String getNamaLatin() { return namaLatin; }
    public int getUsiaMaksimal() { return usiaMaksimal; }

    public void setNama(String nama) { this.nama = nama; }
    public void setNamaLatin(String namaLatin) { this.namaLatin = namaLatin; }
    public void setUsiaMaksimal(int usiaMaksimal) { this.usiaMaksimal = usiaMaksimal; }

    public void displayInfo() {
        System.out.println("Nama             : " + nama);
        System.out.println("Nama Latin       : " + namaLatin);
        System.out.println("Usia Maksimal    : " + usiaMaksimal + " tahun");
    }
}
