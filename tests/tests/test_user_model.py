# Kelompok 4
import pytest
from unittest.mock import MagicMock, patch
from models.user_model import UserModel

@pytest.fixture
def user_model():
    # Patch (Mock) class Database agar tidak terhubung ke MySQL sungguhan
    with patch('models.user_model.Database') as MockDatabase:
        mock_db_instance = MockDatabase.return_value
        mock_conn = MagicMock()
        mock_db_instance.get_connection.return_value = mock_conn
        
        model = UserModel()
        model.conn = mock_conn
        return model

def test_hash_password(user_model):
    # Menguji apakah fungsi _hash_password menghasilkan format SHA-256 yang valid
    password_mentah = "admin123"
    # SHA-256 dari "admin123" adalah:
    hash_ekspektasi = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
    
    assert user_model._hash_password(password_mentah) == hash_ekspektasi

def test_autentikasi_berhasil(user_model):
    mock_cursor = MagicMock()
    user_model.conn.cursor.return_value = mock_cursor
    
    # Skenario: Database mengembalikan data user (Kombinasi benar)
    mock_cursor.fetchone.return_value = {
        'id_user': 1,
        'nama': 'Aryadana',
        'username': 'admin',
        'role': 'Admin'
    }
    
    result = user_model.autentikasi('admin', 'admin123')
    
    # Verifikasi eksekusi query
    mock_cursor.execute.assert_called_once()
    assert result is not None
    assert result['username'] == 'admin'
    assert result['role'] == 'Admin'

def test_autentikasi_gagal(user_model):
    mock_cursor = MagicMock()
    user_model.conn.cursor.return_value = mock_cursor
    
    # Skenario: Database mengembalikan nilai None (Username/Password salah)
    mock_cursor.fetchone.return_value = None
    
    result = user_model.autentikasi('admin', 'passwordsalah')
    
    assert result is None