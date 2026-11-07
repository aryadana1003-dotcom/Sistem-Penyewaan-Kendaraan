# kelompok 4
import tkinter.messagebox as messagebox
from models.pelanggan_model import PelangganModel
from views.pelanggan_view import PelangganView

class PelangganController:
    def __init__(self, user_role="Petugas"):
        self.model = PelangganModel()
        self.view = PelangganView()
        
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_pelanggan()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_pelanggan'], p['nama'], p['no_telepon'], p['alamat']))
            
    def simpan_data(self):
        nama = self.view.entry_nama.get()
        telp = self.view.entry_telepon.get()
        alamat = self.view.entry_alamat.get("1.0", "end-1c")
        
        if not nama or not telp:
            messagebox.showwarning("Peringatan", "Nama dan No Telepon harus diisi!")
            return
            
        if self.model.create_pelanggan(nama, telp, alamat):
            messagebox.showinfo("Sukses", "Data pelanggan berhasil disimpan!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")
            
    def hapus_data(self):
        selected_item = self.view.table.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Pilih data di tabel!")
            return
            
        id_pelanggan = self.view.table.item(selected_item[0], "values")[0]
        
        if messagebox.askyesno("Konfirmasi", "Yakin hapus data pelanggan ini?"):
            if self.model.delete_pelanggan(id_pelanggan):
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Pelanggan ini mungkin masih memiliki transaksi.")