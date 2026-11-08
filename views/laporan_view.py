# Kelompok 4
import customtkinter as ctk
from tkinter import ttk

class LaporanView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Laporan Transaksi Penyewaan")
        self.geometry("950x550")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # --- HEADER KONTROL LAPORAN ---
        self.frame_atas = ctk.CTkFrame(self)
        self.frame_atas.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        ctk.CTkLabel(self.frame_atas, text="Laporan Penyewaan Kendaraan", font=("Arial", 18, "bold")).pack(pady=15)
        
        self.btn_refresh = ctk.CTkButton(self.frame_atas, text="Muat Ulang Laporan", fg_color="blue")
        self.btn_refresh.pack(pady=10)

        # TOMBOL KEMBALI KE DASHBOARD
        self.btn_kembali = ctk.CTkButton(self.frame_atas, text="Kembali ke Dashboard", fg_color="gray", command=self.destroy)
        self.btn_kembali.pack(pady=5)

        # --- TABEL KONTEN LAPORAN ---
        self.frame_bawah = ctk.CTkFrame(self)
        self.frame_bawah.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        kolom = ("id_sewa", "pelanggan", "nopol", "kendaraan", "tgl_sewa", "total", "status_sewa", "status_bayar")
        self.table = ttk.Treeview(self.frame_bawah, columns=("id", "pelanggan", "nopol", "merk", "tgl_sewa", "biaya", "status"), show="headings")
        
        # Atur Judul Kolom
        self.table.heading("id", text="ID Sewa")
        self.table.heading("pelanggan", text="Pelanggan")
        self.table.heading("nopol", text="Nopol")
        self.table.heading("merk", text="Kendaraan")
        self.table.heading("tgl_sewa", text="Tgl Sewa")
        self.table.heading("biaya", text="Total Biaya")
        self.table.heading("status", text="Status")
        
        # Atur Lebar Kolom
        self.table.column("id", width=60, anchor="center")
        self.table.column("pelanggan", width=130)
        self.table.column("nopol", width=90, anchor="center")
        self.table.column("merk", width=90)
        self.table.column("tgl_sewa", width=90, anchor="center")
        self.table.column("biaya", width=100, anchor="e")
        self.table.column("status", width=90, anchor="center")
        
        self.table.pack(fill="both", expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = LaporanView()
    app.mainloop()