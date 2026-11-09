# Kelompok 4
import tkinter.messagebox as messagebox
from models.pelanggan_model import PelangganModel
from views.pelanggan_view import PelangganView

class PelangganController:
    def __init__(self, user_role, dashboard_window):

        # Menyimpan role pengguna
        self.user_role = str(user_role).strip().lower()

        self.dashboard_window = dashboard_window

        self.model = PelangganModel()
        self.view = PelangganView(
            user_role=self.user_role
        )

        # ID pelanggan yang sedang dipilih
        self.id_pelanggan_terpilih = None

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_update.configure(
            command=self.update_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        self.view.btn_kembali.configure(
            command=self.kembali_ke_dashboard
        )

        self.view.protocol(
            "WM_DELETE_WINDOW",
            self.kembali_ke_dashboard
        )

        # Binding klik pada tabel
        self.view.table.bind(
            "<ButtonRelease-1>",
            self.on_table_click
        )

        self.muat_data_tabel()

    def on_table_click(self, event=None):
        # Mengisi form berdasarkan data yang dipilih

        selected_item = self.view.table.selection()

        if not selected_item:
            return

        item_values = self.view.table.item(
            selected_item[0],
            "values"
        )

        if not item_values:
            return

        # Menyimpan ID pelanggan
        self.id_pelanggan_terpilih = item_values[0]

        # Membersihkan form
        self.kosongkan_form()

        # Mengisi form dari tabel
        self.view.entry_nama.insert(
            0, item_values[1]
        )

        self.view.entry_telepon.insert(
            0, item_values[2]
        )

        self.view.entry_alamat.insert(
            0, item_values[3]
        )

    def kosongkan_form(self):
        # Mengosongkan seluruh input.

        self.view.entry_nama.delete(0, "end")
        self.view.entry_telepon.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def update_data(self):
        # Memperbarui data pelanggan.

        if not self.id_pelanggan_terpilih:
            messagebox.showwarning(
                "Peringatan",
                "Silakan pilih data pelanggan yang ingin diubah terlebih dahulu!"
            )
            return

        nama = self.view.entry_nama.get().strip()
        telp = self.view.entry_telepon.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not telp:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan nomor telepon harus diisi!"
            )
            return

        if self.model.update_pelanggan(
            self.id_pelanggan_terpilih,
            nama,
            telp,
            alamat
        ):

            messagebox.showinfo(
                "Sukses",
                "Data pelanggan berhasil diperbarui!"
            )

            self.id_pelanggan_terpilih = None

            self.kosongkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data pelanggan."
            )

    def kembali_ke_dashboard(self):
        # Menutup halaman pelanggan dan kembali ke dashboard.

        self.view.destroy()
        self.dashboard_window.deiconify()

    def muat_data_tabel(self):
        # Menampilkan daftar pelanggan aktif

        # Membersihkan isi tabel sebelumnya
        for item in self.view.table.get_children():
            self.view.table.delete(item)

        # Mengambil data dari Model
        data = self.model.get_all_pelanggan()

        for pelanggan in data:
            self.view.table.insert(
                "",
                "end",
                values=(
                    pelanggan["id_pelanggan"],
                    pelanggan["nama"],
                    pelanggan["no_telepon"],
                    pelanggan["alamat"]
                )
            )

    def simpan_data(self):
        # Menyimpan pelanggan baru

        nama = self.view.entry_nama.get().strip()
        telp = self.view.entry_telepon.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not telp:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan nomor telepon harus diisi!"
            )
            return

        if self.model.create_pelanggan(
            nama, telp, alamat
        ):

            messagebox.showinfo(
                "Sukses",
                "Data pelanggan berhasil disimpan!"
            )

            self.kosongkan_form()
            self.id_pelanggan_terpilih = None
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data pelanggan."
            )

    def hapus_data(self):
        # Menghapus pelanggan dari daftar aktif khusus Admin

        # Pemeriksaan hak akses
        if self.user_role != "admin":
            messagebox.showwarning(
                "Akses Ditolak",
                "Penghapusan data pelanggan hanya dapat dilakukan oleh Admin."
            )
            return

        # Memeriksa apakah ada data yang dipilih
        selected_item = self.view.table.selection()

        if not selected_item:
            messagebox.showwarning(
                "Pilih Data",
                "Pilih pelanggan pada tabel terlebih dahulu!"
            )
            return

        # Mengambil ID pelanggan
        id_pelanggan = self.view.table.item(
            selected_item[0],
            "values"
        )[0]

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Penghapusan",
            "Yakin ingin menghapus pelanggan ini dari daftar aktif?\n\n"
            "Riwayat transaksi dan pembayaran tetap disimpan."
        )

        if not konfirmasi:
            return

        # Proses penghapusan melalui Model
        if self.model.delete_pelanggan(id_pelanggan):

            self.id_pelanggan_terpilih = None

            self.kosongkan_form()
            self.muat_data_tabel()

            messagebox.showinfo(
                "Sukses",
                "Pelanggan berhasil dihapus dari daftar aktif.\n"
                "Riwayat transaksi tetap tersimpan."
            )

        else:
            messagebox.showerror(
                "Error",
                "Pelanggan gagal dihapus. "
                "Data mungkin sudah tidak aktif atau koneksi database bermasalah."
            )