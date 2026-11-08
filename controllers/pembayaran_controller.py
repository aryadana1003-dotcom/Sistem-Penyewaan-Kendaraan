# Kelompok 4
import tkinter.messagebox as messagebox
from models.pembayaran_model import PembayaranModel
from models.penyewaan_model import PenyewaanModel
from views.pembayaran_view import PembayaranView

class PembayaranController:
    def __init__(self, user_role, dashboard_window):
        self.dashboard_window = dashboard_window
        self.model = PembayaranModel()
        self.sewa_model = PenyewaanModel()
        self.view = PembayaranView()
        
        # Variabel penyimpan ID pembayaran yang diklik
        self.id_pembayaran_terpilih = None
        self.data_sewa_cache = []
        
        self.view.btn_simpan.configure(command=self.proses_pembayaran)
        self.view.btn_update.configure(command=self.update_data) # Bind tombol update
        
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        # BINDING: Deteksi saat baris tabel di-klik (Release klik kiri)
        self.view.table.bind("<ButtonRelease-1>", self.on_table_click)
        
        self.muat_data_tabel()
        self.muat_dropdown()
        
    def kembali_ke_dashboard(self):
        self.view.destroy()
        self.dashboard_window.deiconify()

    def on_table_click(self, event):
        # Mengisi form otomatis saat baris di tabel pembayaran diklik 
        selected_item = self.view.table.selection()
        if selected_item:
            item_values = self.view.table.item(selected_item[0], "values")
            
            self.id_pembayaran_terpilih = item_values[0]
            id_sewa_tabel = item_values[1]
            
            # Cari dan set combobox Penyewaan berdasarkan ID Sewa
            for val in self.view.combo_penyewaan.cget("values"):
                # Cek apakah text di combobox diawali dengan "ID_Sewa -"
                if str(val).startswith(str(id_sewa_tabel) + " -"):
                    self.view.combo_penyewaan.set(val)
                    break
                    
            # Isi inputan lainnya
            self.view.entry_tgl_bayar.delete(0, "end")
            self.view.entry_tgl_bayar.insert(0, item_values[2])
            
            self.view.entry_jumlah.delete(0, "end")
            self.view.entry_jumlah.insert(0, str(item_values[3]).replace(".00", ""))
            
            self.view.combo_metode.set(item_values[4])
            self.view.combo_status.set(item_values[5])

    def update_data(self):
        # Memperbarui data pembayaran berdasarkan ID yang dipilih
        if not self.id_pembayaran_terpilih:
            messagebox.showwarning("Peringatan", "Silakan klik data pembayaran pada tabel terlebih dahulu!")
            return
            
        id_sewa_raw = self.view.combo_penyewaan.get()
        if id_sewa_raw == "Pilih Transaksi Penyewaan" or not id_sewa_raw:
            messagebox.showwarning("Peringatan", "Silakan pilih transaksi yang akan dibayar!")
            return
            
        id_sewa = id_sewa_raw.split(" - ")[0]
        tgl_bayar = self.view.entry_tgl_bayar.get()
        jumlah = self.view.entry_jumlah.get()
        metode = self.view.combo_metode.get()
        status = self.view.combo_status.get()
        
        if not tgl_bayar or not jumlah:
            messagebox.showwarning("Peringatan", "Tanggal bayar dan jumlah bayar harus terisi!")
            return
            
        if self.model.update_pembayaran(self.id_pembayaran_terpilih, id_sewa, tgl_bayar, jumlah, metode, status):
            messagebox.showinfo("Sukses", "Data pembayaran berhasil di-update!")
            self.id_pembayaran_terpilih = None
            self.muat_data_tabel()
            
            # Bersihkan form
            self.view.entry_tgl_bayar.delete(0, "end")
            self.view.entry_jumlah.delete(0, "end")
        else:
            messagebox.showerror("Error", "Gagal meng-update data pembayaran.")

    def muat_dropdown(self):
        self.data_sewa_cache = self.sewa_model.get_all_penyewaan()
        
        # Format teks ComboBox: "ID - Nama (Rp Total_Biaya)"
        list_sewa = [f"{s['id_penyewaan']} - {s['nama_pelanggan']} (Rp {s['total_biaya']})" for s in self.data_sewa_cache]
        
        if list_sewa:
            # Menghubungkan combobox dengan fungsi on_penyewaan_selected agar otomatis mengisi jumlah bayar
            self.view.combo_penyewaan.configure(values=list_sewa, command=self.on_penyewaan_selected)
            
    def on_penyewaan_selected(self, choice):
        # Fungsi yang otomatis berjalan saat user memilih salah satu transaksi di ComboBox
        try:
            # Ambil ID Sewa dari teks yang dipilih (angka sebelum karakter ' - ')
            id_sewa_terpilih = choice.split(" - ")[0]
            
            # Cari data total biaya berdasarkan ID sewa dari cache
            for s in self.data_sewa_cache:
                if str(s['id_penyewaan']) == str(id_sewa_terpilih):
                    # Masukkan nilai total biaya secara otomatis ke entry jumlah bayar
                    self.view.entry_jumlah.delete(0, "end")
                    self.view.entry_jumlah.insert(0, str(s['total_biaya']))
                    break
        except Exception as e:
            print(f"Error auto-fill jumlah bayar: {e}")
            
    def muat_data_tabel(self):
        for item in self.view.table.get_children():
            self.view.table.delete(item)
            
        data = self.model.get_all_pembayaran()
        for p in data:
            self.view.table.insert("", "end", values=(p['id_pembayaran'], p['id_penyewaan'], p['tanggal_bayar'], p['jumlah_bayar'], p['metode_pembayaran'], p['status_pembayaran']))
            
    def proses_pembayaran(self):
        id_sewa_raw = self.view.combo_penyewaan.get()
        
        if id_sewa_raw == "Pilih Transaksi Penyewaan" or not id_sewa_raw:
            messagebox.showwarning("Peringatan", "Silakan pilih transaksi yang akan dibayar!")
            return
            
        id_sewa = id_sewa_raw.split(" - ")[0] # Ambil ID Sewa dari teks yang dipilih (angka sebelum karakter ' - ')
        tgl_bayar = self.view.entry_tgl_bayar.get()
        jumlah = self.view.entry_jumlah.get()
        metode = self.view.combo_metode.get()
        status = self.view.combo_status.get()
        
        if not tgl_bayar or not jumlah:
            messagebox.showwarning("Peringatan", "Tanggal bayar dan jumlah bayar harus terisi!")
            return
            
        if self.model.create_pembayaran(id_sewa, tgl_bayar, jumlah, metode, status):
            messagebox.showinfo("Sukses", "Pembayaran berhasil diproses!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memproses pembayaran.")