# Kelompok 4
import pytest
from unittest.mock import MagicMock, patch
from models.kendaraan_model import KendaraanModel

@pytest.fixture
def kendaraan_model():
    with patch('models.kendaraan_model.Database') as MockDatabase:
        mock_db_instance = MockDatabase.return_value
        mock_conn = MagicMock()
        mock_db_instance.get_connection.return_value = mock_conn
        
        model = KendaraanModel()
        model.conn = mock_conn
        return model

def test_get_all_kendaraan(kendaraan_model):
    mock_cursor = MagicMock()
    kendaraan_model.conn.cursor.return_value = mock_cursor
    
    # Data manipulasi (Dummy) yang seolah-olah ditarik dari database
    data_dummy = [
        {'id_kendaraan': 1, 'nomor_polisi': 'DN 1234 AB', 'merk': 'Toyota', 'status': 'Tersedia'},
        {'id_kendaraan': 2, 'nomor_polisi': 'DN 5678 CD', 'merk': 'Honda', 'status': 'Disewa'}
    ]
    mock_cursor.fetchall.return_value = data_dummy
    
    result = kendaraan_model.get_all_kendaraan()
    
    assert len(result) == 2
    assert result[0]['nomor_polisi'] == 'DN 1234 AB'
    assert result[1]['status'] == 'Disewa'
    mock_cursor.execute.assert_called_once()

def test_create_kendaraan(kendaraan_model):
    mock_cursor = MagicMock()
    kendaraan_model.conn.cursor.return_value = mock_cursor
    
    # Menguji pemanggilan insert data
    result = kendaraan_model.create_kendaraan('DN 9999 XX', 'Suzuki', 'Ertiga', 'Mobil', '2020', 300000)
    
    assert result is True
    mock_cursor.execute.assert_called_once()
    kendaraan_model.conn.commit.assert_called_once() # Memastikan koneksi menyimpan data