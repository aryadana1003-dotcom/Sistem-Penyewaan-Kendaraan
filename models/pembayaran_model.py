# Kelompok 4
from config.database import Database

class PembayaranModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "pembayaran"

    def get_all_pembayaran(self):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Error get_all_pembayaran: {e}")
                return []
        return []

    def update_pembayaran(self, id_pembayaran, id_penyewaan, tanggal_bayar, jumlah_bayar, metode_pembayaran, status_pembayaran):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"UPDATE {self.table_name} SET id_penyewaan=%s, tanggal_bayar=%s, jumlah_bayar=%s, metode_pembayaran=%s, status_pembayaran=%s WHERE id_pembayaran=%s"
                val = (id_penyewaan, tanggal_bayar, jumlah_bayar, metode_pembayaran, status_pembayaran, id_pembayaran)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error update_pembayaran: {e}")
                self.conn.rollback()
                return False
        return False

    def create_pembayaran(self, id_penyewaan, tanggal_bayar, jumlah_bayar, metode_pembayaran, status_pembayaran="Lunas"):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (id_penyewaan, tanggal_bayar, jumlah_bayar, metode_pembayaran, status_pembayaran) VALUES (%s, %s, %s, %s, %s)"
                val = (id_penyewaan, tanggal_bayar, jumlah_bayar, metode_pembayaran, status_pembayaran)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error create_pembayaran: {e}")
                self.conn.rollback()
                return False
        return False