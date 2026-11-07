# Kelompok 4
import tkinter.messagebox as messagebox
from models.kendaraan_model import KendaraanModel
from views.kendaraan_view import KendaraanView

class KendaraanController:
    def __init__(self, user_role="Petugas"):
        self.user_role = user_role
        self.model = KendaraanModel()
        self.view = KendaraanView()
        
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # Otorisasi: Hanya Admin yang bisa menghapus data kendaraan
        if self.user_role.lower() != "admin":
            self.view.btn_hapus.configure(state="disabled", text="Hapus (Khusus Admin)")
        else:
            self.view.btn_hapus.configure(command=self.hapus_data)
            
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data_kendaraan = self.model.get_all_kendaraan()
        for k in data_kendaraan:
            self.view.table.insert("", "end", values=(k['id_kendaraan'], k['nomor_polisi'], k['merk'], k['model'], k['jenis'], k['tahun'], k['tarif_per_hari'], k['status']))
            
    def simpan_data(self):
        nopol = self.view.entry_nopol.get()
        merk = self.view.entry_merk.get()
        model = self.view.entry_model.get()
        jenis = self.view.combo_jenis.get()
        tahun = self.view.entry_tahun.get()
        tarif = self.view.entry_tarif.get()
        status = self.view.combo_status.get()
        
        if not nopol or not merk or not tarif:
            messagebox.showwarning("Peringatan", "Kolom Nopol, Merk, dan Tarif harus diisi!")
            return
            
        berhasil = self.model.create_kendaraan(nopol, merk, model, jenis, tahun, tarif, status)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data kendaraan berhasil disimpan!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data kendaraan.")
            
    def hapus_data(self):
        selected_item = self.view.table.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Silakan pilih data di tabel terlebih dahulu!")
            return
            
        item_values = self.view.table.item(selected_item[0], "values")
        id_kendaraan = item_values[0]
        
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus kendaraan ini?"):
            if self.model.delete_kendaraan(id_kendaraan):
                messagebox.showinfo("Sukses", "Data dihapus.")
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")