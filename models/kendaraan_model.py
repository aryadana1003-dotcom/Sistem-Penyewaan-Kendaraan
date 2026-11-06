# Kelompok 4
from config.database import Database

class KendaraanModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "kendaraan"

    def get_all_kendaraan(self):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Error get_all_kendaraan: {e}")
                return []
        return []

    def create_kendaraan(self, nomor_polisi, merk, model, jenis, tahun, tarif_per_hari, status="Tersedia"):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (nomor_polisi, merk, model, jenis, tahun, tarif_per_hari, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (nomor_polisi, merk, model, jenis, tahun, tarif_per_hari, status)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error create_kendaraan: {e}")
                self.conn.rollback()
                return False
        return False

    def update_kendaraan(self, id_kendaraan, nomor_polisi, merk, model, jenis, tahun, tarif_per_hari, status):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"UPDATE {self.table_name} SET nomor_polisi=%s, merk=%s, model=%s, jenis=%s, tahun=%s, tarif_per_hari=%s, status=%s WHERE id_kendaraan=%s"
                val = (nomor_polisi, merk, model, jenis, tahun, tarif_per_hari, status, id_kendaraan)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error update_kendaraan: {e}")
                self.conn.rollback()
                return False
        return False

    def delete_kendaraan(self, id_kendaraan):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"DELETE FROM {self.table_name} WHERE id_kendaraan=%s"
                cursor.execute(query, (id_kendaraan,))
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error delete_kendaraan: {e}")
                self.conn.rollback()
                return False
        return False