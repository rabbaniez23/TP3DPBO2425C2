import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Habitat hutanTropis = new Habitat("Hutan Tropis Kalimantan", "Tropis Basah", 5000);
        Habitat sabanaJawa = new Habitat("Sabana Baluran", "Kering", 250);
        Habitat perairanMuara = new Habitat("Perairan Muara", "Payau", 1000);

        ArrayList<Habitat> daftarHabitat = new ArrayList<>();
        daftarHabitat.add(hutanTropis);
        daftarHabitat.add(sabanaJawa);
        daftarHabitat.add(perairanMuara);

        // Hardcode data
        hutanTropis.tambahMakhluk(new Mamalia("Orangutan","Pongo pygmaeus",45,2,75,"Cokelat Kemerahan"), true);
        hutanTropis.tambahMakhluk(new Mamalia("Harimau Sumatra","Panthera tigris sumatrae",25,4,150,"Oranye Belang"), true);
        hutanTropis.tambahMakhluk(new Tumbuhan("Bunga Raflesia","Rafflesia arnoldii",2,1,2,"Serabut (Parasit)"), true);

        sabanaJawa.tambahMakhluk(new Mamalia("Banteng","Bos javanicus",20,4,800,"Hitam"), true);
        sabanaJawa.tambahMakhluk(new Reptil("Komodo","Varanus komodoensis",30,300,20,"Sisik Keras"), true);
        sabanaJawa.tambahMakhluk(new Tumbuhan("Pohon Jati","Tectona grandis",150,40,150,"Tunggang"), true);

        perairanMuara.tambahMakhluk(new Reptil("Buaya Muara","Crocodylus porosus",70,500,40,"Kulit Keras Berduri"), true);
        perairanMuara.tambahMakhluk(new Reptil("Penyu Hijau","Chelonia mydas",80,120,100,"Tempurung Keras"), true);

        System.out.println("Data hardcode selesai dimuat.");

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n===== MENU MANAJEMEN EKOSISTEM =====");
            System.out.println("1. Tambah Data Makhluk Baru");
            System.out.println("2. Tampilkan Semua Data Ekosistem");
            System.out.println("3. Keluar");

            System.out.print("Pilih menu (1-3): ");
            int pilihan = sc.nextInt();
            sc.nextLine();

            if (pilihan == 1) {
                System.out.println("\nPilih Habitat untuk menambahkan makhluk:");
                for (int i=0; i<daftarHabitat.size(); i++) {
                    System.out.println((i+1) + ". " + daftarHabitat.get(i).getNamaHabitat());
                }
                int ph = sc.nextInt();
                sc.nextLine();

                if (ph < 1 || ph > daftarHabitat.size()) {
                    System.out.println("Pilihan habitat tidak valid!");
                    continue;
                }

                Habitat habitatTerpilih = daftarHabitat.get(ph-1);

                System.out.println("\n--- Pilih Jenis Makhluk ---");
                System.out.println("1. Mamalia\n2. Reptil\n3. Tumbuhan");
                int jenis = sc.nextInt();
                sc.nextLine();

                System.out.print("Masukkan Nama: ");
                String nama = sc.nextLine();
                System.out.print("Masukkan Nama Latin: ");
                String latin = sc.nextLine();
                System.out.print("Masukkan Usia Maksimal (tahun): ");
                int usia = sc.nextInt();
                sc.nextLine();

                switch (jenis) {
                    case 1:
                        System.out.print("Masukkan Jumlah Kaki: ");
                        int kaki = sc.nextInt();
                        System.out.print("Masukkan Berat Badan (kg): ");
                        int berat = sc.nextInt();
                        sc.nextLine();
                        System.out.print("Masukkan Warna Rambut: ");
                        String warna = sc.nextLine();
                        habitatTerpilih.tambahMakhluk(new Mamalia(nama, latin, usia, kaki, berat, warna), false);
                        break;
                    case 2:
                        System.out.print("Masukkan Panjang Tubuh (cm): ");
                        int panjang = sc.nextInt();
                        System.out.print("Masukkan Jumlah Telur: ");
                        int telur = sc.nextInt();
                        sc.nextLine();
                        System.out.print("Masukkan Jenis Sisik: ");
                        String sisik = sc.nextLine();
                        habitatTerpilih.tambahMakhluk(new Reptil(nama, latin, usia, panjang, telur, sisik), false);
                        break;
                    case 3:
                        System.out.print("Masukkan Tinggi Maksimal (meter): ");
                        int tinggi = sc.nextInt();
                        System.out.print("Masukkan Lama Hidup Rata-rata (tahun): ");
                        int lama = sc.nextInt();
                        sc.nextLine();
                        System.out.print("Masukkan Jenis Akar: ");
                        String akar = sc.nextLine();
                        habitatTerpilih.tambahMakhluk(new Tumbuhan(nama, latin, usia, tinggi, lama, akar), false);
                        break;
                    default:
                        System.out.println("Pilihan jenis tidak valid!");
                        break;
                }
            } else if (pilihan == 2) {
                System.out.println("\n<<<<< MENAMPILKAN KESELURUHAN DATA EKOSISTEM >>>>>");
                for (Habitat h : daftarHabitat) {
                    h.tampilkanSemuaMakhluk();
                }
            } else if (pilihan == 3) {
                System.out.println("Terima kasih, program selesai.");
                break;
            } else {
                System.out.println("Pilihan tidak valid!");
            }
        }

        sc.close();
    }
}
