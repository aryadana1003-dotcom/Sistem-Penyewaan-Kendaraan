# Kelompok 4
import tkinter.messagebox as messagebox
from models.penyewaan_model import PenyewaanModel
from models.pelanggan_model import PelangganModel
from models.kendaraan_model import KendaraanModel
from views.penyewaan_view import PenyewaanView

class PenyewaanController:
    # Ditambahkan parameter id_user dan dashboard_window
    def __init__(self, user_role, id_user, dashboard_window):
        self.id_user = id_user
        self.dashboard_window = dashboard_window
        self.model = PenyewaanModel()
        self.pelanggan_model = PelangganModel()
        self.kendaraan_model = KendaraanModel()
        self.view = PenyewaanView()
        
        self.view.btn_simpan.configure(command=self.simpan_transaksi)
        self.view.btn_selesai.configure(command=self.selesaikan_sewa)
        
        # Binding tombol kembali dan tombol [X] (close) pada window
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        self.muat_data_tabel()
        self.muat_dropdown() 
        
    def kembali_ke_dashboard(self):
        self.view.destroy()
        self.dashboard_window.deiconify()

    def muat_dropdown(self):
        pelanggan = self.pelanggan_model.get_all_pelanggan()
        kendaraan = self.kendaraan_model.get_all_kendaraan()
        
        list_pelanggan = [f"{p['id_pelanggan']} - {p['nama']}" for p in pelanggan]
        list_kendaraan = [f"{k['id_kendaraan']} - {k['nomor_polisi']} ({k['merk']})" for k in kendaraan if k['status'] == 'Tersedia']
        
        if list_pelanggan: self.view.combo_pelanggan.configure(values=list_pelanggan)
        if list_kendaraan: self.view.combo_kendaraan.configure(values=list_kendaraan)
        
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_penyewaan()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_penyewaan'], p['nama_pelanggan'], p['nomor_polisi'], p['tanggal_sewa'], p['tanggal_kembali'], p['total_biaya'], p['status_penyewaan']))
            
    def simpan_transaksi(self):
        id_pel_raw = self.view.combo_pelanggan.get()
        id_ken_raw = self.view.combo_kendaraan.get()
        
        if id_pel_raw == "Pilih Pelanggan" or id_ken_raw == "Pilih Kendaraan":
            messagebox.showwarning("Peringatan", "Silakan pilih Pelanggan dan Kendaraan!")
            return
            
        id_pelanggan = id_pel_raw.split(" - ")[0]
        id_kendaraan = id_ken_raw.split(" - ")[0]
        
        tgl_sewa = self.view.entry_tgl_sewa.get()
        tgl_kembali = self.view.entry_tgl_kembali.get()
        biaya = self.view.entry_biaya.get()
        status = self.view.combo_status.get()
        
        if self.model.create_penyewaan(id_pelanggan, id_kendaraan, self.id_user, tgl_sewa, tgl_kembali, biaya, status):
            messagebox.showinfo("Sukses", "Transaksi penyewaan berhasil dibuat!")
            self.muat_data_tabel()
            self.muat_dropdown() 
        else:
            messagebox.showerror("Error", "Gagal membuat transaksi.")
            
    def selesaikan_sewa(self):
        selected_item = self.view.table.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Pilih transaksi yang akan diselesaikan!")
            return
            
        id_sewa = self.view.table.item(selected_item[0], "values")[0]
        
        if messagebox.askyesno("Konfirmasi", "Tandai penyewaan ini sebagai 'Selesai'?"):
            if self.model.update_status_penyewaan(id_sewa, "Selesai"):
                messagebox.showinfo("Sukses", "Status penyewaan diperbarui.")
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal memperbarui status.")