# Kelompok 4
import customtkinter as ctk
from tkinter import ttk

class KendaraanView(ctk.CTkToplevel): # Menggunakan Toplevel agar terbuka sebagai jendela baru dari Dashboard
    def __init__(self):
        super().__init__()
        self.title("Kelola Data Kendaraan")
        self.geometry("1000x550")
        
        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        # --- FRAME KIRI: FORMULIR INPUT KENDARAAN ---
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kiri, text="Form Data Kendaraan", font=("Arial", 16, "bold")).pack(pady=15)
        
        self.entry_nopol = ctk.CTkEntry(self.frame_kiri, placeholder_text="Nomor Polisi (Contoh: DN 1234 AB)")
        self.entry_nopol.pack(pady=10, padx=15, fill="x")
        
        self.entry_merk = ctk.CTkEntry(self.frame_kiri, placeholder_text="Merk (Contoh: Toyota)")
        self.entry_merk.pack(pady=10, padx=15, fill="x")
        
        self.entry_model = ctk.CTkEntry(self.frame_kiri, placeholder_text="Model (Contoh: Avanza)")
        self.entry_model.pack(pady=10, padx=15, fill="x")
        
        self.combo_jenis = ctk.CTkComboBox(self.frame_kiri, values=["Mobil", "Motor"])
        self.combo_jenis.pack(pady=10, padx=15, fill="x")
        self.combo_jenis.set("Pilih Jenis Kendaraan")
        
        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Keluaran")
        self.entry_tahun.pack(pady=10, padx=15, fill="x")
        
        self.entry_tarif = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tarif per Hari")
        self.entry_tarif.pack(pady=10, padx=15, fill="x")
        
        self.combo_status = ctk.CTkComboBox(self.frame_kiri, values=["Tersedia", "Disewa", "Perawatan"])
        self.combo_status.pack(pady=10, padx=15, fill="x")
        self.combo_status.set("Tersedia")
        
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=15, fill="x")
        
        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data Terpilih", fg_color="red")
        self.btn_hapus.pack(pady=5, padx=15, fill="x")

        # TOMBOL KEMBALI KE DASHBOARD
        self.btn_kembali = ctk.CTkButton(self.frame_kiri, text="Kembali ke Dashboard", fg_color="gray", command=self.destroy)
        self.btn_kembali.pack(pady=15, padx=15, fill="x")

        # --- FRAME KANAN: TABEL DATA KENDARAAN ---
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kanan, text="Daftar Kendaraan", font=("Arial", 16, "bold")).pack(pady=15)
        
        # Komponen Tabel (Treeview)
        kolom = ("id", "nopol", "merk", "model", "jenis", "tahun", "tarif", "status")
        self.table = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        self.table.heading("id", text="ID")
        self.table.heading("nopol", text="Nomor Polisi")
        self.table.heading("merk", text="Merk")
        self.table.heading("model", text="Model")
        self.table.heading("jenis", text="Jenis")
        self.table.heading("tahun", text="Tahun")
        self.table.heading("tarif", text="Tarif/Hari")
        self.table.heading("status", text="Status")
        
        self.table.column("id", width=30, anchor="center")
        self.table.column("nopol", width=90, anchor="center")
        self.table.column("merk", width=80)
        self.table.column("model", width=80)
        self.table.column("jenis", width=60, anchor="center")
        self.table.column("tahun", width=60, anchor="center")
        self.table.column("tarif", width=90, anchor="e")
        self.table.column("status", width=80, anchor="center")
        
        self.table.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = KendaraanView()
    app.mainloop()