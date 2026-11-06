# Kelompok 4
from config.database import Database

class PenyewaanModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "penyewaan"

    def get_all_penyewaan(self):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                # Menggunakan JOIN agar data yang dirender di View lebih informatif
                query = """
                    SELECT p.*, pel.nama AS nama_pelanggan, k.nomor_polisi, k.merk, u.nama AS nama_petugas 
                    FROM penyewaan p
                    JOIN pelanggan pel ON p.id_pelanggan = pel.id_pelanggan
                    JOIN kendaraan k ON p.id_kendaraan = k.id_kendaraan
                    JOIN user u ON p.id_user = u.id_user
                """
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Error get_all_penyewaan: {e}")
                return []
        return []

    def create_penyewaan(self, id_pelanggan, id_kendaraan, id_user, tanggal_sewa, tanggal_kembali, total_biaya, status_penyewaan="Menunggu Pembayaran"):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (id_pelanggan, id_kendaraan, id_user, tanggal_sewa, tanggal_kembali, total_biaya, status_penyewaan) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (id_pelanggan, id_kendaraan, id_user, tanggal_sewa, tanggal_kembali, total_biaya, status_penyewaan)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error create_penyewaan: {e}")
                self.conn.rollback()
                return False
        return False

    def update_status_penyewaan(self, id_penyewaan, status_penyewaan, tanggal_kembali_aktual=None):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"UPDATE {self.table_name} SET status_penyewaan=%s, tanggal_kembali_aktual=%s WHERE id_penyewaan=%s"
                val = (status_penyewaan, tanggal_kembali_aktual, id_penyewaan)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error update_status_penyewaan: {e}")
                self.conn.rollback()
                return False
        return False