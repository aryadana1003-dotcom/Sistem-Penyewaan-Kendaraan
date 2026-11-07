# Kelompok 4
import tkinter.messagebox as messagebox
from models.penyewaan_model import PenyewaanModel
from views.penyewaan_view import PenyewaanView

class PenyewaanController:
    def __init__(self, user_role, id_user):
        self.id_user = id_user
        self.model = PenyewaanModel()
        self.view = PenyewaanView()
        
        self.view.btn_simpan.configure(command=self.simpan_transaksi)
        self.view.btn_selesai.configure(command=self.selesaikan_sewa)
        
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_penyewaan()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_penyewaan'], p['nama_pelanggan'], p['nomor_polisi'], p['tanggal_sewa'], p['tanggal_kembali'], p['total_biaya'], p['status_penyewaan']))
            
    def simpan_transaksi(self):
        id_pelanggan = self.view.entry_id_pelanggan.get()
        id_kendaraan = self.view.entry_id_kendaraan.get()
        tgl_sewa = self.view.entry_tgl_sewa.get()
        tgl_kembali = self.view.entry_tgl_kembali.get()
        biaya = self.view.entry_biaya.get()
        status = self.view.combo_status.get()
        
        if not id_pelanggan or not id_kendaraan or not biaya:
            messagebox.showwarning("Peringatan", "Formulir transaksi belum lengkap!")
            return
            
        if self.model.create_penyewaan(id_pelanggan, id_kendaraan, self.id_user, tgl_sewa, tgl_kembali, biaya, status):
            messagebox.showinfo("Sukses", "Transaksi penyewaan berhasil dibuat!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal membuat transaksi.")
            
    def selesaikan_sewa(self):
        selected_item = self.view.table.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Pilih transaksi yang akan diselesaikan!")
            return
            
        id_sewa = self.view.table.item(selected_item[0], "values")[0]
        
        if messagebox.askyesno("Konfirmasi", "Tandai penyewaan ini sebagai 'Selesai'?"):
            # Update status jadi selesai
            if self.model.update_status_penyewaan(id_sewa, "Selesai"):
                messagebox.showinfo("Sukses", "Status penyewaan diperbarui.")
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal memperbarui status.")