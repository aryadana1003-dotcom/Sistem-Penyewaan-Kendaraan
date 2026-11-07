# Kelompok 4
import tkinter.messagebox as messagebox
from models.pembayaran_model import PembayaranModel
from models.penyewaan_model import PenyewaanModel
from views.pembayaran_view import PembayaranView

class PembayaranController:
    def __init__(self, user_role, dashboard_window):
        self.dashboard_window = dashboard_window # Simpan referensi ke window dashboard agar bisa kembali ke sana
        self.model = PembayaranModel()
        self.sewa_model = PenyewaanModel()
        self.view = PembayaranView()
        
        self.view.btn_simpan.configure(command=self.proses_pembayaran)
        
        # Binding tombol kembali dan tombol [X] (close) pada window
        self.view.btn_kembali.configure(command=self.kembali_ke_dashboard)
        self.view.protocol("WM_DELETE_WINDOW", self.kembali_ke_dashboard)
        
        # Simpan data mentah penyewaan agar mudah diakses saat combobox dipilih
        self.data_sewa_cache = []
        
        self.muat_data_tabel()
        self.muat_dropdown()
        
    def kembali_ke_dashboard(self):
        self.view.destroy()                 # Tutup window pembayaran
        self.dashboard_window.deiconify()   # Tampilkan kembali window dashboard

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