import json
import os
from datetime import datetime

# Fungsi untuk mengecek dan mereset antrian jika hari berganti
def cek_dan_reset_antrian():
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    data = {}

    if os.path.exists("antrian.json"):
        try:
            with open("antrian.json", "r") as f:
                data = json.load(f)  # Membaca data dari file JSON
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}

    last_date = data.get("last_date")

    if last_date != hari_ini:  # Jika tanggal terakhir tidak sama dengan hari ini
        # Reset data antrian jika tanggal berganti
        data = {
            "last_number": 0,
            "last_called": 0,
            "last_date": hari_ini
        }
        with open("antrian.json", "w") as f:
            json.dump(data, f)  # Menyimpan data baru ke file JSON

    return data
