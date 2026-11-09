# Kelompok 4
import customtkinter as ctk
from tkinter import ttk

class PelangganView(ctk.CTkToplevel):
    def __init__(self, user_role="Petugas"):
        super().__init__()

        self.user_role = str(user_role).strip().lower()

        self.title("Kelola Data Pelanggan")
        self.geometry("900x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT PELANGGAN
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Pelanggan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Nama Lengkap"
        )
        self.entry_nama.pack(
            pady=10, padx=15, fill="x"
        )

        self.entry_telepon = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Nomor Telepon (Contoh: 0812...)"
        )
        self.entry_telepon.pack(
            pady=10, padx=15, fill="x"
        )

        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat Lengkap"
        )
        self.entry_alamat.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data Baru",
            fg_color="green"
        )
        self.btn_simpan.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Update Data Terpilih",
            fg_color="blue"
        )
        self.btn_update.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Hapus Berdasarkan Hak Akses
        if self.user_role == "admin":

            self.btn_hapus = ctk.CTkButton(
                self.frame_kiri,
                text="Hapus Data Terpilih",
                fg_color="red",
                hover_color="#B91C1C",
                state="normal"
            )

        else:

            self.btn_hapus = ctk.CTkButton(
                self.frame_kiri,
                text="Hapus (Khusus Admin)",
                fg_color="red",
                hover_color="#B91C1C",
                state="disabled"
            )

        self.btn_hapus.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Kembali
        self.btn_kembali = ctk.CTkButton(
            self.frame_kiri,
            text="Kembali ke Dashboard",
            fg_color="gray",
            command=self.destroy
        )
        self.btn_kembali.pack(
            pady=15, padx=15, fill="x"
        )

        # FRAME KANAN: TABEL DATA PELANGGAN
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Pelanggan Aktif",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        kolom = ("id", "nama", "telepon", "alamat")

        self.table = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        self.table.heading("id", text="ID")
        self.table.heading("nama", text="Nama Lengkap")
        self.table.heading("telepon", text="No. Telepon")
        self.table.heading("alamat", text="Alamat")

        self.table.column(
            "id", width=30, anchor="center"
        )
        self.table.column(
            "nama", width=120
        )
        self.table.column(
            "telepon", width=100, anchor="center"
        )
        self.table.column(
            "alamat", width=200
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


if __name__ == "__main__":
    app = PelangganView()
    app.mainloop()