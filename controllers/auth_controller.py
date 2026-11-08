# Kelompok 4
import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from views.dashboard_view import DashboardView

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        
        # Mengikat tombol login
        self.view.btn_login.configure(command=self.login)
        
    def login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()
        
        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password harus diisi!")
            return
            
        user = self.model.autentikasi(username, password)
        
        if user:
            messagebox.showinfo("Sukses", f"Selamat datang, {user['nama']}!")
            self.view.destroy() # Tutup form login
            self.buka_dashboard(user['role'], user['id_user'])
        else:
            messagebox.showerror("Error", "Username atau Password salah!")
            
    def buka_dashboard(self, role, id_user):
        # Inisialisasi DashboardView dengan role dan master sebagai self.view
        self.dashboard = DashboardView(role=role, master=self.view)
        
        # Binding menu dashboard ke masing-masing controller
        self.dashboard.btn_kendaraan.configure(command=lambda: self.buka_kendaraan(role))
        self.dashboard.btn_pelanggan.configure(command=lambda: self.buka_pelanggan(role))
        self.dashboard.btn_penyewaan.configure(command=lambda: self.buka_penyewaan(role, id_user))
        self.dashboard.btn_pembayaran.configure(command=lambda: self.buka_pembayaran(role))

        # BINDING UNTUK ADMIN
        if role.lower() == "admin":
            self.dashboard.btn_laporan.configure(command=lambda: self.buka_laporan(role))
        
        self.dashboard.btn_logout.configure(command=self.logout)

    # Fungsi navigasi untuk membuka controller lain (Lazy Import untuk mencegah circular import)
    def buka_kendaraan(self, role):
        self.dashboard.withdraw() # Sembunyikan dashboard
        from controllers.kendaraan_controller import KendaraanController
        # Kirimkan self.dashboard sebagai parameter tambahan
        KendaraanController(role, self.dashboard)

    def buka_pelanggan(self, role):
        self.dashboard.withdraw()
        from controllers.pelanggan_controller import PelangganController
        PelangganController(role, self.dashboard)

    def buka_penyewaan(self, role, id_user):
        self.dashboard.withdraw()
        from controllers.penyewaan_controller import PenyewaanController
        PenyewaanController(role, id_user, self.dashboard)

    def buka_pembayaran(self, role):
        self.dashboard.withdraw()
        from controllers.pembayaran_controller import PembayaranController
        PembayaranController(role, self.dashboard)

    def buka_laporan(self, role):
        self.dashboard.withdraw()
        from controllers.laporan_controller import LaporanController
        LaporanController(role, self.dashboard)

    def logout(self):
        self.dashboard.destroy()
        app = AuthController()
        app.run()
        
    def run(self):
        self.view.mainloop()