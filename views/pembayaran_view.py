# Kelompok 4
import customtkinter as ctk
from tkinter import ttk

class PembayaranView(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Kelola Transaksi Pembayaran")
        self.geometry("950x500")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        # --- FRAME KIRI: FORMULIR PEMBAYARAN ---
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kiri, text="Form Pembayaran", font=("Arial", 16, "bold")).pack(pady=15)

        self.combo_penyewaan = ctk.CTkComboBox(self.frame_kiri, values=["Pilih Transaksi Penyewaan"])
        self.combo_penyewaan.pack(pady=10, padx=15, fill="x")

        self.entry_tgl_bayar = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tanggal Bayar (YYYY-MM-DD)")
        self.entry_tgl_bayar.pack(pady=10, padx=15, fill="x")
        
        self.entry_jumlah = ctk.CTkEntry(self.frame_kiri, placeholder_text="Jumlah Bayar (Rp)")
        self.entry_jumlah.pack(pady=10, padx=15, fill="x")
        
        self.combo_metode = ctk.CTkComboBox(self.frame_kiri, values=["Tunai", "Transfer", "Kartu Kredit", "E-Wallet"])
        self.combo_metode.pack(pady=10, padx=15, fill="x")
        self.combo_metode.set("Pilih Metode Pembayaran")
        
        self.combo_status = ctk.CTkComboBox(self.frame_kiri, values=["Belum Dibayar", "Lunas"])
        self.combo_status.pack(pady=10, padx=15, fill="x")
        self.combo_status.set("Lunas")
        
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Proses Pembayaran", fg_color="green")
        self.btn_simpan.pack(pady=10, padx=15, fill="x")
        
        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Update Data Terpilih", fg_color="blue")
        self.btn_update.pack(pady=10, padx=15, fill="x")
        
        self.btn_kembali = ctk.CTkButton(self.frame_kiri, text="Kembali ke Dashboard", fg_color="gray", command=self.destroy)
        self.btn_kembali.pack(pady=15, padx=15, fill="x")

        # --- FRAME KANAN: TABEL PEMBAYARAN ---
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kanan, text="Riwayat Pembayaran", font=("Arial", 16, "bold")).pack(pady=15)
        
        kolom = ("id_bayar", "id_sewa", "tgl_bayar", "jumlah", "metode", "status")
        self.table = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        self.table.heading("id_bayar", text="ID Bayar")
        self.table.heading("id_sewa", text="ID Sewa")
        self.table.heading("tgl_bayar", text="Tgl Bayar")
        self.table.heading("jumlah", text="Jumlah Bayar")
        self.table.heading("metode", text="Metode")
        self.table.heading("status", text="Status")
        
        self.table.column("id_bayar", width=50, anchor="center")
        self.table.column("id_sewa", width=50, anchor="center")
        self.table.column("tgl_bayar", width=80, anchor="center")
        self.table.column("jumlah", width=100, anchor="e")
        self.table.column("metode", width=90, anchor="center")
        self.table.column("status", width=90, anchor="center")
        
        self.table.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = PembayaranView()
    app.mainloop()