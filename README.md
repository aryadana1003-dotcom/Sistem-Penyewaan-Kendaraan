# Sistem Penyewaan Kendaraan

Aplikasi Desktop **Sistem Penyewaan Kendaraan** berbasis Python yang dibangun menggunakan arsitektur **Model-View-Controller (MVC)**, antarmuka modern **CustomTkinter**, serta basis data **MySQL**. Aplikasi ini dirancang untuk mengelola master data kendaraan, data pelanggan, transaksi penyewaan, pembayaran, hingga pelaporan administratif secara terpusat dengan sistem kontrol akses berbasis peran (*Role-Based Access Control*).

---

## 🚀 Fitur Utama
1. **Autentikasi & Keamanan**: 
   * Sistem login aman dengan enkripsi password **SHA-256**.
   * Hak akses pengguna berbasis peran (**Admin** dan **Petugas**).
2. **Manajemen Master Data (CRUD & Update)**:
   * **Data Kendaraan**: Pengelolaan informasi armada, status ketersediaan, tarif, dan fitur pembaruan data secara *real-time*.
   * **Data Pelanggan**: Pendataan identitas, nomor telepon, alamat, serta fitur edit data.
3. **Manajemen Transaksi**:
   * **Penyewaan**: Pembuatan transaksi sewa dengan pemilihan otomatis data pelanggan dan kendaraan melalui *ComboBox*, serta perhitungan total biaya.
   * **Pembayaran**: Pencatatan riwayat pembayaran yang terintegrasi otomatis dengan total biaya transaksi penyewaan.
4. **Laporan Transaksi (Khusus Admin)**:
   * Rekapitulasi seluruh data penyewaan kendaraan dengan tampilan tabel yang bersih dan terstruktur.
5. **Navigasi Single-Window**:
   * Sistem jendela terpadu di mana perpindahan menu menyembunyikan jendela utama (`withdraw`) dan mengembalikannya (`deiconify`) saat tombol kembali ditekan.
6. **Unit Testing & CI/CD Pipeline**:
   * Pengujian otomatis menggunakan pustaka `pytest` dengan teknik *mocking*.
   * Integrasi **GitHub Actions** untuk pengujian *Continuous Integration* otomatis di setiap *push* atau *pull request*.

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman**: Python 3.x
* **GUI Framework**: CustomTkinter
* **Basis Data**: MySQL (Laragon / XAMPP)
* **Konektor DB**: `mysql-connector-python`
* **Pengujian**: `pytest`, `pytest-cov`
* **CI/CD**: GitHub Actions

---

## 📂 Struktur Direktori Proyek
```text
Sistem-Penyewaan-Kendaraan/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # Konfigurasi GitHub Actions CI Pipeline
├── config/
│   └── database.py            # Konfigurasi koneksi database MySQL
├── controllers/
│   ├── auth_controller.py     # Kontroler autentikasi & navigasi dashboard
│   ├── kendaraan_controller.py# Logika kontroler data kendaraan
│   ├── pelanggan_controller.py# Logika kontroler data pelanggan
│   ├── penyewaan_controller.py# Logika kontroler transaksi penyewaan
│   ├── pembayaran_controller.py# Logika kontroler transaksi pembayaran
│   └── laporan_controller.py  # Logika kontroler laporan (Admin)
├── models/
│   ├── user_model.py          # Model database & enkripsi SHA-256 user
│   ├── kendaraan_model.py     # Model database CRUD kendaraan
│   ├── pelanggan_model.py     # Model database CRUD pelanggan
│   ├── penyewaan_model.py     # Model database CRUD penyewaan
│   └── pembayaran_model.py    # Model database CRUD pembayaran
├── views/
│   ├── login_view.py          # Tampilan antarmuka login
│   ├── dashboard_view.py      # Tampilan antarmuka dashboard utama
│   ├── kendaraan_view.py      # Tampilan form & tabel kendaraan
│   ├── pelanggan_view.py      # Tampilan form & tabel pelanggan
│   ├── penyewaan_view.py      # Tampilan form & tabel penyewaan
│   ├── pembayaran_view.py     # Tampilan form & tabel pembayaran
│   └── laporan_view.py        # Tampilan laporan penyewaan
├── tests/
│   ├── test_user_model.py     # Unit test untuk model user & autentikasi
│   └── test_kendaraan_model.py# Unit test untuk model kendaraan
├── env/                       # Virtual Environment Python
├── conftest.py                # Konfigurasi root pytest
├── main.py                    # Titik masuk utama aplikasi (Entry Point)
├── requirements.txt           # Daftar dependensi pustaka Python
└── README.md                  # Dokumentasi proyek