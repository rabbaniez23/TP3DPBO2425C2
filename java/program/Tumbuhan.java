public class Tumbuhan extends MakhlukHidup {
    private int tinggiMaksimal;
    private int lamaHidup;
    private String jenisAkar;

    public Tumbuhan(String nama, String namaLatin, int usiaMaksimal,
                    int tinggiMaksimal, int lamaHidup, String jenisAkar) {
        super(nama, namaLatin, usiaMaksimal);
        this.tinggiMaksimal = tinggiMaksimal;
        this.lamaHidup = lamaHidup;
        this.jenisAkar = jenisAkar;
    }

    @Override
    public void displayInfo() {
        System.out.println("--- DATA TUMBUHAN ---");
        super.displayInfo();
        System.out.println("Tinggi Maksimal  : " + tinggiMaksimal + " meter");
        System.out.println("Lama Hidup Rata2 : " + lamaHidup + " tahun");
        System.out.println("Jenis Akar       : " + jenisAkar);
    }
}
