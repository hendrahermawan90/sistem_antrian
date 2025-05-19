import json
import os
from datetime import datetime

def cek_dan_reset_antrian():
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    data = {}

    if os.path.exists("antrian.json"):
        try:
            with open("antrian.json", "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    last_date = data.get("last_date")

    if last_date != hari_ini:
        # Reset jika hari berganti
        data = {
            "last_number": 0,
            "last_called": 0,
            "last_date": hari_ini
        }
        with open("antrian.json", "w") as f:
            json.dump(data, f)

    return data
