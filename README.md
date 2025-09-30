# Tugas Praktikum 3 - Simulasi Ekosistem OOP
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)


---

## Daftar Isi
1. [Desain Program (UML)](#desain-program-uml)
2. [Struktur Kelas](#struktur-kelas)
3. [Alur Program](#alur-program)
4. [Dokumentasi](#dokumentasi)
5. [Janji](#janji)

---

## Desain Program (UML)
Diagram UML berikut merepresentasikan arsitektur dan hubungan antar kelas dalam program.


<img src="tp3.drawio.png">




<details>
<summary><strong>Klik untuk melihat penjelasan detail desain</strong></summary>

### Relasi Pewarisan (Inheritance)
* **Konsep:** "Dari Umum ke Khusus". Kelas `MakhlukHidup` bertindak sebagai **kelas induk** yang menyimpan atribut umum. Kelas `Mamalia`, `Reptil`, dan `Tumbuhan` adalah **kelas turunan** yang mewarisi sifat dari `MakhlukHidup` dan menambahkan atribut uniknya sendiri.
* **Alasan Desain:** Desain ini mencerminkan hubungan **"adalah sebuah" (is-a)**. Contoh: `Mamalia` adalah sebuah `MakhlukHidup`. Ini menghindari duplikasi kode dan membuat struktur program logis sesuai klasifikasi dunia nyata.

### Relasi Komposisi (Composition)
* **Konsep:** "Wadah dan Isinya". Kelas `Habitat` tidak mewarisi dari kelas manapun, melainkan **memiliki** atau **terdiri dari** kumpulan objek `MakhlukHidup`.
* **Alasan Desain:** Desain ini mencerminkan hubungan **"memiliki sebuah" (has-a)**. Contoh: `Habitat` memiliki `MakhlukHidup`. Ini secara logis memisahkan antara konsep **lingkungan** dengan **penghuninya**.
</details>

---

## Struktur Kelas

Berikut adalah rincian atribut dan method untuk setiap kelas.

### `MakhlukHidup` (Base Class)
| Atribut | Tipe | Deskripsi |
|---|---|---|
| `nama` | `string` | Nama umum dari makhluk hidup. |
| `usia` | `int` | Usia atau rentang hidup makhluk. |
| `namaLatin` | `string` | Nama ilmiah dari makhluk hidup. |

| Method | Deskripsi |
|---|---|
| `displayInfo()` | Method `virtual` yang menampilkan informasi dasar. |

### `Mamalia`, `Reptil`, & `Tumbuhan` (Derived Classes)
Kelas-kelas ini mewarisi semua atribut `MakhlukHidup` dan menambahkan atribut spesifik:

| Kelas | Atribut Spesifik | Deskripsi |
|---|---|---|
| **Mamalia** | `jumlahKaki`, `BeratBadan`, `WarnaRambut` | Ciri khas fisik untuk membedakan mamalia. |
| **Reptil** | `Berat`, `ciriTubuh`, `habitat` | Ciri khas untuk reptil, seperti "bersisik". |
| **Tumbuhan**| `jenisAkar`, `JenisDaun`, `JenisBatang` | Komponen anatomi dasar dari tumbuhan. |

Setiap kelas turunan juga meng-`override` method `displayInfo()` untuk menampilkan detail spesifiknya.

### `Habitat` (Composition Class)
| Atribut | Tipe | Deskripsi |
|---|---|---|
| `NamaHabitat` | `string` | Nama dari lingkungan (contoh: "Sabana"). |
| `TipeIklim` | `string` | Kondisi iklim dari habitat (contoh: "Kering"). |
| `LuasArea` | `int` | Ukuran luas dari habitat (dalam km²). |
| `DaftarMakhluk` | `vector<MakhlukHidup*>` | Kumpulan objek yang menghuni habitat. |

| Method | Deskripsi |
|---|---|
| `tambahMakhluk()` | Menambahkan objek `MakhlukHidup` baru ke dalam habitat. |
| `tampilkanSemuaMakhluk()` | Menampilkan informasi semua makhluk yang ada di habitat. |

---

## Alur Program
1.  **Inisialisasi:** Program dimulai, membuat beberapa objek `Habitat`, dan memuat data awal (*hardcode*) ke habitat yang sesuai.
2.  **Menu Utama:** Sebuah `loop` menampilkan menu utama kepada pengguna:
    - `1. Tambah Data Makhluk Baru`
    - `2. Tampilkan Semua Data Ekosistem`
    - `3. Keluar`
3.  **Tambah Data:** Pengguna memilih habitat, jenis makhluk, lalu memasukkan data yang diminta. Objek baru akan dibuat dan ditambahkan ke habitat tersebut.
4.  **Tampilkan Data:** Program akan menampilkan informasi dari setiap habitat, diikuti oleh detail semua makhluk yang tinggal di dalamnya.
5.  **Keluar:** Program menampilkan pesan penutup dan berhenti.

---

## janji

Saya, Naufal Rizki Rabbani, mengerjakan tugas praktikum ini dalam mata kuliah Desain dan Pemrograman Berbasis Objek untuk keberkahan-Nya. Saya tidak melakukan kecurangan seperti yang telah dispesifikasikan dan saya siap menerima konsekuensi jika terbukti melakukan kecurangan. Aamiin

## dokumentasi

cpp
<img width="822" height="805" alt="Screenshot 2025-09-30 183048" src="https://github.com/user-attachments/assets/db0d0b5c-d68a-4517-b336-cd3d04f8d6f2" />
<img width="676" height="483" alt="Screenshot 2025-09-30 183039" src="https://github.com/user-attachments/assets/ca3a69a0-673b-4426-8f38-26a8a0aa8276" />
<img width="823" height="783" alt="Screenshot 2025-09-30 183031" src="https://github.com/user-attachments/assets/7cfb1cef-e4e7-4ec0-ae77-694c56caa119" />


java
<img width="934" height="850" alt="Screenshot 2025-09-30 183720" src="https://github.com/user-attachments/assets/22a02744-9908-498c-906a-eca4ae51ab23" />
<img width="782" height="504" alt="Screenshot 2025-09-30 183730" src="https://github.com/user-attachments/assets/bddbedeb-181a-416f-9d50-09054d707c08" />
<img width="890" height="770" alt="Screenshot 2025-09-30 183738" src="https://github.com/user-attachments/assets/1205df3a-cb3d-4270-8a4f-ae9c6d5be769" />

python
<img width="867" height="896" alt="Screenshot 2025-09-30 181256" src="https://github.com/user-attachments/assets/962453fd-93d6-413e-afe1-dbca8c37668e" />
<img width="728" height="550" alt="Screenshot 2025-09-30 181315" src="https://github.com/user-attachments/assets/b6f5eb6a-1430-4410-bcd5-f5cf5a289128" />
<img width="699" height="891" alt="Screenshot 2025-09-30 181325" src="https://github.com/user-attachments/assets/9b307ebb-d09b-4d56-a95a-a56212340320" />









