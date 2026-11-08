# Kelompok 4
import tkinter.messagebox as messagebox
from models.kendaraan_model import KendaraanModel
from views.kendaraan_view import KendaraanView

class KendaraanController:
    def __init__(self, user_role, dashboard_window):
        self.user_role = user_role
        self.dashboard_window = dashboard_window
        self.model = KendaraanModel()
        self.view = KendaraanView()
        
        # Variabel untuk menyimpan ID kendaran yang sedang di-klik
        self.id_kendaraan_terpilih = None 
        
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data) # Bind tombol update
        
        if self.user_role.lower() != "admin":
            self.view.btn_hapus.configure(state="disabled", text="Hapus (Khusus Admin)")
        else:
            self.view.btn_hapus.configure(command=self.hapus_data)
            
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        # BINDING: Deteksi saat baris tabel di-klik (Release klik kiri)
        self.view.table.bind("<ButtonRelease-1>", self.on_table_click)
            
        self.muat_data_tabel()

    def on_table_click(self, event):
        # Fungsi ini berjalan saat user mengklik baris di tabel
        selected_item = self.view.table.selection()
        if selected_item:
            # Ambil nilai dari baris yang di-klik
            item_values = self.view.table.item(selected_item[0], "values")
            
            # Simpan ID kendaraan ke memori
            self.id_kendaraan_terpilih = item_values[0]
            
            # Bersihkan form lama
            self.view.entry_nopol.delete(0, "end")
            self.view.entry_merk.delete(0, "end")
            self.view.entry_model.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")
            self.view.entry_tarif.delete(0, "end")
            
            # Isi form dengan data yang di-klik
            self.view.entry_nopol.insert(0, item_values[1])
            self.view.entry_merk.insert(0, item_values[2])
            self.view.entry_model.insert(0, item_values[3])
            self.view.combo_jenis.set(item_values[4])
            self.view.entry_tahun.insert(0, item_values[5])
            self.view.entry_tarif.insert(0, item_values[6])
            self.view.combo_status.set(item_values[7])

    def update_data(self):
        if not self.id_kendaraan_terpilih:
            messagebox.showwarning("Peringatan", "Silakan klik data pada tabel yang ingin diubah terlebih dahulu!")
            return
            
        nopol = self.view.entry_nopol.get()
        merk = self.view.entry_merk.get()
        model = self.view.entry_model.get()
        jenis = self.view.combo_jenis.get()
        tahun = self.view.entry_tahun.get()
        tarif = self.view.entry_tarif.get()
        status = self.view.combo_status.get()
        
        if not nopol or not merk or not tarif:
            messagebox.showwarning("Peringatan", "Kolom Nopol, Merk, dan Tarif tidak boleh kosong!")
            return
            
        if self.model.update_kendaraan(self.id_kendaraan_terpilih, nopol, merk, model, jenis, tahun, tarif, status):
            messagebox.showinfo("Sukses", "Data kendaraan berhasil di-update!")
            self.id_kendaraan_terpilih = None # Reset pilihan
            self.muat_data_tabel()
            
            # Kosongkan form setelah berhasil update
            self.view.entry_nopol.delete(0, "end")
            self.view.entry_merk.delete(0, "end")
            self.view.entry_model.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")
            self.view.entry_tarif.delete(0, "end")
        else:
            messagebox.showerror("Error", "Gagal meng-update data kendaraan.")
        
    def kembali_ke_dashboard(self):
        self.view.destroy()
        self.dashboard_window.deiconify()

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