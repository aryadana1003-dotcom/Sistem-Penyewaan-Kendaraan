# Kelompok 4
import tkinter.messagebox as messagebox
from models.penyewaan_model import PenyewaanModel
from views.laporan_view import LaporanView

class LaporanController:
    # Tambahkan parameter user_role dan dashboard_window
    def __init__(self, user_role, dashboard_window):
        self.user_role = user_role
        self.dashboard_window = dashboard_window
        self.model = PenyewaanModel()
        self.view = LaporanView()
        
        self.view.btn_refresh.configure(command=self.muat_laporan)
        
        # Binding tombol kembali dan tombol [X] (close) pada window
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        self.muat_laporan()
        
    def kembali_ke_dashboard(self):
        self.view.destroy()
        self.dashboard_window.deiconify()
        
    def muat_laporan(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_penyewaan()
        for p in data:
            self.table_values = (
                p['id_penyewaan'], 
                p['nama_pelanggan'], 
                p['nomor_polisi'], 
                p['merk'], 
                p['tanggal_sewa'], 
                p['total_biaya'], 
                p['status_penyewaan']
            )
            self.view.table.insert("", "end", values=self.table_values)