# Kelompok 4
import hashlib
from config.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "user"

    def _hash_password(self, password):
        # Mengubah plain text password menjadi format hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                password_hash = self._hash_password(password)
                
                # Parameterized Query untuk mencegah celah keamanan SQL Injection
                query = f"SELECT id_user, nama, username, role FROM {self.table_name} WHERE username = %s AND password_hash = %s"
                cursor.execute(query, (username, password_hash))
                
                user = cursor.fetchone()
                cursor.close()
                return user
            except Exception as e:
                print(f"Error autentikasi: {e}")
                return None
        return None
        
    def get_all_user(self):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                query = f"SELECT id_user, nama, username, role FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Error get_all_user: {e}")
                return []
        return []