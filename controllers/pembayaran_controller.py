# Kelompok 4
import tkinter.messagebox as messagebox
from models.pembayaran_model import PembayaranModel
from views.pembayaran_view import PembayaranView

class PembayaranController:
    def __init__(self, user_role):
        self.model = PembayaranModel()
        self.view = PembayaranView()
        
        self.view.btn_simpan.configure(command=self.proses_pembayaran)
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_pembayaran()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_pembayaran'], p['id_penyewaan'], p['tanggal_bayar'], p['jumlah_bayar'], p['metode_pembayaran'], p['status_pembayaran']))
            
    def proses_pembayaran(self):
        id_sewa = self.view.entry_id_penyewaan.get()
        tgl_bayar = self.view.entry_tgl_bayar.get()
        jumlah = self.view.entry_jumlah.get()
        metode = self.view.combo_metode.get()
        status = self.view.combo_status.get()
        
        if not id_sewa or not jumlah or metode == "Pilih Metode Pembayaran":
            messagebox.showwarning("Peringatan", "Lengkapi formulir pembayaran!")
            return
            
        if self.model.create_pembayaran(id_sewa, tgl_bayar, jumlah, metode, status):
            messagebox.showinfo("Sukses", "Pembayaran berhasil diproses!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memproses pembayaran.")