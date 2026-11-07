# Kelompok 4
import customtkinter as ctk
from tkinter import ttk

class PenyewaanView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Transaksi Penyewaan Kendaraan")
        self.geometry("1100x600")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        
        # --- FRAME KIRI: FORMULIR INPUT PENYEWAAN ---
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kiri, text="Form Penyewaan", font=("Arial", 16, "bold")).pack(pady=15)

        # Ganti Entry dengan ComboBox
        self.combo_pelanggan = ctk.CTkComboBox(self.frame_kiri, values=["Pilih Pelanggan"])
        self.combo_pelanggan.pack(pady=10, padx=15, fill="x")
        
        self.combo_kendaraan = ctk.CTkComboBox(self.frame_kiri, values=["Pilih Kendaraan"])
        self.combo_kendaraan.pack(pady=10, padx=15, fill="x")
        
        self.entry_tgl_sewa = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tanggal Sewa (YYYY-MM-DD)")
        self.entry_tgl_sewa.pack(pady=10, padx=15, fill="x")
        
        self.entry_tgl_kembali = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tanggal Kembali (YYYY-MM-DD)")
        self.entry_tgl_kembali.pack(pady=10, padx=15, fill="x")
        
        self.entry_biaya = ctk.CTkEntry(self.frame_kiri, placeholder_text="Total Biaya")
        self.entry_biaya.pack(pady=10, padx=15, fill="x")
        
        self.combo_status = ctk.CTkComboBox(self.frame_kiri, values=["Menunggu Pembayaran", "Berlangsung", "Selesai", "Dibatalkan"])
        self.combo_status.pack(pady=10, padx=15, fill="x")
        self.combo_status.set("Menunggu Pembayaran")
        
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Buat Transaksi", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=15, fill="x")
        
        self.btn_selesai = ctk.CTkButton(self.frame_kiri, text="Selesaikan Sewa", fg_color="blue")
        self.btn_selesai.pack(pady=5, padx=15, fill="x")

        # TOMBOL KEMBALI
        self.btn_kembali = ctk.CTkButton(self.frame_kiri, text="Kembali ke Dashboard", fg_color="gray", command=self.destroy)
        self.btn_kembali.pack(pady=15, padx=15, fill="x")

        # --- FRAME KANAN: TABEL DATA PENYEWAAN ---
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kanan, text="Data Transaksi Penyewaan", font=("Arial", 16, "bold")).pack(pady=15)
        
        kolom = ("id_sewa", "pelanggan", "kendaraan", "tgl_sewa", "tgl_kembali", "total_biaya", "status")
        self.table = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        self.table.heading("id_sewa", text="ID Sewa")
        self.table.heading("pelanggan", text="Nama Pelanggan")
        self.table.heading("kendaraan", text="Kendaraan (Nopol)")
        self.table.heading("tgl_sewa", text="Tgl Sewa")
        self.table.heading("tgl_kembali", text="Tgl Kembali")
        self.table.heading("total_biaya", text="Total Biaya")
        self.table.heading("status", text="Status")
        
        self.table.column("id_sewa", width=50, anchor="center")
        self.table.column("pelanggan", width=120)
        self.table.column("kendaraan", width=120)
        self.table.column("tgl_sewa", width=90, anchor="center")
        self.table.column("tgl_kembali", width=90, anchor="center")
        self.table.column("total_biaya", width=100, anchor="e")
        self.table.column("status", width=120, anchor="center")
        
        self.table.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = PenyewaanView()
    app.mainloop()