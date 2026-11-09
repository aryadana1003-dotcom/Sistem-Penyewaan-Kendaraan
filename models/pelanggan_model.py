# Kelompok 4
from config.database import Database

class PelangganModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "pelanggan"

    def get_all_pelanggan(self):
        # Mengambil seluruh data pelanggan yang masih aktif
        if not self.conn:
            return []

        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)

            query = f"""
                SELECT id_pelanggan, nama, no_telepon, alamat
                FROM {self.table_name}
                WHERE status_data = 'Aktif'
                ORDER BY id_pelanggan DESC
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error get_all_pelanggan: {e}")
            return []

        finally:
            if cursor:
                cursor.close()

    def create_pelanggan(self, nama, no_telepon, alamat):
        # Menambahkan pelanggan baru.
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name}
                    (nama, no_telepon, alamat, status_data)
                VALUES (%s, %s, %s, 'Aktif')
            """

            cursor.execute(query, (nama, no_telepon, alamat))
            self.conn.commit()
            return True

        except Exception as e:
            print(f"Error create_pelanggan: {e}")
            self.conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()

    def update_pelanggan(self, id_pelanggan, nama, no_telepon, alamat):
        # Memperbarui data pelanggan yang masih aktif
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET nama = %s,
                    no_telepon = %s,
                    alamat = %s
                WHERE id_pelanggan = %s
                AND status_data = 'Aktif'
            """

            cursor.execute(
                query,
                (nama, no_telepon, alamat, id_pelanggan)
            )

            berhasil = cursor.rowcount > 0
            self.conn.commit()

            return berhasil

        except Exception as e:
            print(f"Error update_pelanggan: {e}")
            self.conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()

    def delete_pelanggan(self, id_pelanggan):
        # Soft Delete:
        # Mengubah status pelanggan menjadi Dihapus.
        # Data transaksi dan pembayaran tetap tersimpan.
        
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET status_data = 'Dihapus'
                WHERE id_pelanggan = %s
                AND status_data = 'Aktif'
            """

            cursor.execute(query, (id_pelanggan,))

            berhasil = cursor.rowcount > 0
            self.conn.commit()

            return berhasil

        except Exception as e:
            print(f"Error delete_pelanggan: {e}")
            self.conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()