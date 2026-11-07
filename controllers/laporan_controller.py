# Kelompok 4
import tkinter.messagebox as messagebox
from models.penyewaan_model import PenyewaanModel
from views.laporan_view import LaporanView

class LaporanController:
    def __init__(self, user_role="Admin"):
        self.model = PenyewaanModel()
        self.view = LaporanView()
        
        self.view.btn_refresh.configure(command=self.muat_laporan)
        self.muat_laporan()
        
    def muat_laporan(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_penyewaan()
        for p in data:
            # Karena pada laporan_view kolomnya: id_sewa, pelanggan, nopol, kendaraan, tgl_sewa, total, status_sewa, status_bayar
            # Kita map data yang tersedia dari PenyewaanModel
            self.view.table.insert("", "end", values=(
                p['id_penyewaan'], 
                p['nama_pelanggan'], 
                p['nomor_polisi'], 
                p['merk'], 
                p['tanggal_sewa'], 
                p['total_biaya'], 
                p['status_penyewaan'],
                "Cek Detail" # Dummy stat jika tabel pembayaran tidak di-join secara explisit
            ))