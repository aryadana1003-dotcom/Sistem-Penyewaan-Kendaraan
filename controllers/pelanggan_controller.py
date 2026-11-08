# Kelompok 4
import tkinter.messagebox as messagebox
from models.pelanggan_model import PelangganModel
from views.pelanggan_view import PelangganView

class PelangganController:
    def __init__(self, user_role, dashboard_window):
        self.dashboard_window = dashboard_window
        self.model = PelangganModel()
        self.view = PelangganView()
        
        # Variabel untuk menyimpan ID pelanggan yang sedang di-klik
        self.id_pelanggan_terpilih = None
        
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data) # Bind tombol update
        self.view.btn_hapus.configure(command=self.hapus_data)
        
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        # BINDING: Deteksi saat baris tabel di-klik (Release klik kiri)
        self.view.table.bind("<ButtonRelease-1>", self.on_table_click)
        
        self.muat_data_tabel()

    def on_table_click(self, event):
        # Mengisi form secara otomatis saat baris di tabel pelanggan diklik
        selected_item = self.view.table.selection()
        if selected_item:
            item_values = self.view.table.item(selected_item[0], "values")
            
            # Simpan ID pelanggan ke memori
            self.id_pelanggan_terpilih = item_values[0]
            
            # Bersihkan form lama
            self.view.entry_nama.delete(0, "end")
            self.view.entry_telepon.delete(0, "end")
            self.view.entry_alamat.delete(0, "end")
            
            # Isi form dengan data yang di-klik
            self.view.entry_nama.insert(0, item_values[1])
            self.view.entry_telepon.insert(0, item_values[2])
            self.view.entry_alamat.insert(0, item_values[3])

    def update_data(self):
        # Memperbarui data pelanggan ke database
        if not self.id_pelanggan_terpilih:
            messagebox.showwarning("Peringatan", "Silakan klik data pada tabel yang ingin diubah terlebih dahulu!")
            return
            
        nama = self.view.entry_nama.get()
        telp = self.view.entry_telepon.get()
        alamat = self.view.entry_alamat.get()
        
        if not nama or not telp:
            messagebox.showwarning("Peringatan", "Nama dan No Telepon harus diisi!")
            return
            
        if self.model.update_pelanggan(self.id_pelanggan_terpilih, nama, telp, alamat):
            messagebox.showinfo("Sukses", "Data pelanggan berhasil di-update!")
            self.id_pelanggan_terpilih = None # Reset pilihan
            self.muat_data_tabel()
            
            # Kosongkan form setelah berhasil update
            self.view.entry_nama.delete(0, "end")
            self.view.entry_telepon.delete(0, "end")
            self.view.entry_alamat.delete(0, "end")
        else:
            messagebox.showerror("Error", "Gagal meng-update data pelanggan.")
        
    def kembali_ke_dashboard(self):
        self.view.destroy()                # Tutup jendela pelanggan
        self.dashboard_window.deiconify()  # Tampilkan kembali dashboard

    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_pelanggan()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_pelanggan'], p['nama'], p['no_telepon'], p['alamat']))
            
    def simpan_data(self):
        nama = self.view.entry_nama.get()
        telp = self.view.entry_telepon.get()
        # Perbaikan Error: Menggunakan get() kosong karena menggunakan CTkEntry
        alamat = self.view.entry_alamat.get()
        
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