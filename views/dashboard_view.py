# Kelompok 4
import customtkinter as ctk

class DashboardView(ctk.CTkToplevel):
    def __init__(self, role="Petugas", master=None):
        super().__init__()
        self.title(f"Dashboard Penyewaan Kendaraan - Role: {role.upper()}")
        self.geometry("900x500")
        
        # Grid Layout: 1 Baris, 2 Kolom (Sidebar Kiri, Konten Kanan)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # --- SIDEBAR KIRI ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar_frame, text="Menu Utama", font=("Arial", 18, "bold")).pack(pady=20, padx=20)
        
        self.btn_kendaraan = ctk.CTkButton(self.sidebar_frame, text="Data Kendaraan")
        self.btn_kendaraan.pack(pady=10, padx=20, fill="x")
        
        self.btn_pelanggan = ctk.CTkButton(self.sidebar_frame, text="Data Pelanggan")
        self.btn_pelanggan.pack(pady=10, padx=20, fill="x")
        
        self.btn_penyewaan = ctk.CTkButton(self.sidebar_frame, text="Transaksi Penyewaan")
        self.btn_penyewaan.pack(pady=10, padx=20, fill="x")
        
        self.btn_pembayaran = ctk.CTkButton(self.sidebar_frame, text="Data Pembayaran")
        self.btn_pembayaran.pack(pady=10, padx=20, fill="x")
        
        self.btn_logout = ctk.CTkButton(self.sidebar_frame, text="Logout", fg_color="red")
        self.btn_logout.pack(pady=40, padx=20, fill="x", side="bottom")

        # --- KONTEN KANAN ---
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        ctk.CTkLabel(self.content_frame, text="Selamat Datang di Sistem Penyewaan Kendaraan", font=("Arial", 24)).pack(expand=True)

if __name__ == "__main__":
    app = DashboardView()
    app.mainloop()