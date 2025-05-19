## ✅ Sistem Antrian Otomatis

```markdown
# 🏢 Sistem Antrian Otomatis (Python + Tkinter)

Aplikasi **antrian otomatis** berbasis Python dan GUI (Tkinter) dengan fitur lengkap:
- Pengunjung bisa ambil nomor antrian lewat GUI
- Tiket langsung dicetak dalam bentuk PDF + QR Code
- Admin bisa memanggil nomor secara otomatis dengan suara (TTS)
- Tampilan display real-time untuk nomor yang sedang dipanggil

---

## 📂 Struktur Proyek

```

📁 sistem-antrian/
├── admin.py         # Aplikasi pemanggilan nomor antrian oleh petugas
├── pengunjung.py    # Aplikasi ambil nomor antrian + cetak tiket otomatis
├── display.py       # Tampilan display nomor antrian real-time
├── utils.py         # Fungsi utilitas bersama, termasuk reset harian otomatis
├── antrian.json     # File penyimpanan status antrian
├── log\_antrian.csv  # Log riwayat antrian (otomatis dibuat)
└── tiket/
├── pdf/         # Tempat menyimpan tiket dalam bentuk PDF
└── qr/          # Tempat menyimpan gambar QR sementara

````

---

## 🚀 Fitur Utama

- 🎫 **Ambil Nomor Otomatis** via GUI
- 🖨️ **Cetak Tiket** dengan PDF + QR Code (siap print)
- 🗣️ **Pemanggilan Otomatis** dengan Text-to-Speech (suara manusia)
- 📺 **Display Realtime** untuk nomor yang sedang dipanggil
- 🔁 **Reset Harian Otomatis** *(via `utils.py`)*
- 📄 **Log CSV** untuk riwayat data antrian

---

## 📦 Teknologi yang Digunakan

- Python 3
- Tkinter (GUI)
- `pyttsx3` – Text-to-Speech
- `qrcode` – Pembuatan QR Code
- `fpdf` – Generate file PDF
- `win32api`, `win32print` – Untuk akses printer Windows

---

## 💻 Cara Menjalankan

1. **Instal library yang dibutuhkan**
   Sebelum menjalankan aplikasi, pastikan kamu sudah menginstall library yang dibutuhkan:
   ```bash
   pip install pyttsx3 qrcode fpdf pywin32
````

2. **Ambil Antrian (oleh Pengunjung)**
   Untuk pengunjung yang ingin mengambil antrian:

   ```bash
   python pengunjung.py
   ```

3. **Panggil Nomor (oleh Admin)**
   Untuk admin yang ingin memanggil nomor antrian:

   ```bash
   python admin.py
   ```

4. **Tampilkan Display Antrian**
   Untuk menampilkan nomor yang sedang dipanggil:

   ```bash
   python display.py
   ```

---

## 🔁 Tentang Reset Otomatis Harian (`utils.py`)

Agar sistem tetap akurat setiap hari, aplikasi ini secara otomatis **mereset antrian** jika hari telah berganti. Proses ini:

* Mengecek tanggal terakhir dari `antrian.json`
* Jika berbeda dengan hari ini, maka:

  * `last_number` dan `last_called` direset ke `0`
  * `last_date` diupdate ke tanggal hari ini

Fungsi ini terletak di file `utils.py` dan **dijalankan otomatis** oleh `admin.py`, `pengunjung.py`, dan `display.py` saat aplikasi dibuka.

---

## 🛠️ Menjadikan Aplikasi Ini Sebagai `.exe`

Untuk membuat aplikasi ini bisa dijalankan sebagai file `.exe` (tanpa membutuhkan Python di sistem target), kamu bisa menggunakan **PyInstaller**. Ikuti langkah-langkah berikut:

### 1. **Instal PyInstaller**

Install PyInstaller dengan perintah berikut:

```bash
pip install pyinstaller
```

### 2. **Buat File `.exe`**

Masuk ke folder tempat file `.py` kamu berada, lalu jalankan perintah berikut untuk masing-masing file:

* Untuk `pengunjung.py`:

  ```bash
  pyinstaller --onefile --windowed pengunjung.py
  ```

* Untuk `admin.py`:

  ```bash
  pyinstaller --onefile --windowed admin.py
  ```

* Untuk `display.py`:

  ```bash
  pyinstaller --onefile --windowed display.py
  ```

Opsi `--onefile` akan menghasilkan satu file `.exe`, dan `--windowed` akan mencegah munculnya terminal saat aplikasi dijalankan (karena menggunakan Tkinter).

### 3. **File `.exe` di Folder `dist/`**

Setelah proses selesai, kamu akan menemukan file `.exe` di folder `dist/`. File tersebut bisa langsung dijalankan di komputer lain tanpa perlu menginstal Python!

* Misalnya: `dist/pengunjung.exe`, `dist/admin.exe`, `dist/display.exe`

### 4. **(Opsional) Tambahkan Ikon**

Kamu juga bisa menambahkan ikon untuk file `.exe` dengan menggunakan perintah berikut (pastikan file `.ico` kamu sudah siap):

```bash
pyinstaller --onefile --windowed --icon=ikon.ico admin.py
```

### 5. **Catatan**

* Pastikan file `antrian.json` dan folder `tiket/` berada di direktori yang sama dengan file `.exe`.
* Jika menggunakan printer, pastikan printer default sudah terpasang di sistem yang menjalankan aplikasi `.exe`.

---

## 📸 Screenshot (Opsional)

![image](https://github.com/user-attachments/assets/0b1ec248-2da4-4a7c-a4b3-8d28ad1233dc)

---

## ⚠️ Catatan

* Pastikan kamu punya **printer** yang diset sebagai **default** di Windows
* File `antrian.json` akan otomatis dibuat jika belum ada
* QR Code bersifat sementara dan akan dihapus setelah tiket dicetak
* Jalankan semua file dari direktori yang sama agar file bisa saling berhubungan

---

## 📄 Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pendidikan, kantor, klinik, atau instansi lainnya.

---

## 🙋‍♂️ Developer

**Hendra Hermawan**

Link Github : [https://github.com/hendrahermawan90/sistem\_antrian](https://github.com/hendrahermawan90/sistem_antrian)

```
