import java.util.ArrayList;

public class Habitat {
    private String namaHabitat;
    private String tipeIklim;
    private int luasArea;
    private ArrayList<MakhlukHidup> daftarMakhluk;

    public Habitat(String namaHabitat, String tipeIklim, int luasArea) {
        this.namaHabitat = namaHabitat;
        this.tipeIklim = tipeIklim;
        this.luasArea = luasArea;
        this.daftarMakhluk = new ArrayList<>();
    }

    public String getNamaHabitat() { return namaHabitat; }

    public void tambahMakhluk(MakhlukHidup m, boolean silent) {
        daftarMakhluk.add(m);
        if (!silent) {
            System.out.println("\n-> '" + m.getNama() + "' berhasil ditambahkan ke habitat '" + namaHabitat + "'.");
        }
    }

    public void tampilkanSemuaMakhluk() {
        System.out.println("\n==================== HABITAT: " + namaHabitat + " ====================");
        System.out.println("(Tipe Iklim: " + tipeIklim + ", Luas: " + luasArea + " km^2)");
        System.out.println("-------------------------------------------------------------");

        if (daftarMakhluk.isEmpty()) {
            System.out.println("Habitat ini masih kosong.");
        } else {
            for (int i=0; i<daftarMakhluk.size(); i++) {
                System.out.println("\n--- Makhluk ke-" + (i+1) + " ---");
                daftarMakhluk.get(i).displayInfo();
            }
        }
    }
}
