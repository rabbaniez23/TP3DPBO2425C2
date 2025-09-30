public class Mamalia extends MakhlukHidup {
    private int jumlahKaki;
    private int beratBadan;
    private String warnaRambut;

    public Mamalia(String nama, String namaLatin, int usiaMaksimal,
                   int jumlahKaki, int beratBadan, String warnaRambut) {
        super(nama, namaLatin, usiaMaksimal);
        this.jumlahKaki = jumlahKaki;
        this.beratBadan = beratBadan;
        this.warnaRambut = warnaRambut;
    }

    public int getJumlahKaki() { return jumlahKaki; }
    public int getBeratBadan() { return beratBadan; }
    public String getWarnaRambut() { return warnaRambut; }

    public void setJumlahKaki(int jumlahKaki) { this.jumlahKaki = jumlahKaki; }
    public void setBeratBadan(int beratBadan) { this.beratBadan = beratBadan; }
    public void setWarnaRambut(String warnaRambut) { this.warnaRambut = warnaRambut; }

    @Override
    public void displayInfo() {
        System.out.println("--- DATA MAMALIA ---");
        super.displayInfo();
        System.out.println("Jumlah Kaki      : " + jumlahKaki);
        System.out.println("Berat Badan      : " + beratBadan + " kg");
        System.out.println("Warna Rambut     : " + warnaRambut);
    }
}
