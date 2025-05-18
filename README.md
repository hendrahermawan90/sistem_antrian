
## ✅ `README.md` Final untuk Sistem Antrian Otomatis

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
- 🔁 **Reset Harian Otomatis**
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
   ```bash
   pip install pyttsx3 qrcode fpdf pywin32
````

2. **Ambil Antrian (oleh Pengunjung)**

   ```bash
   python pengunjung.py
   ```

3. **Panggil Nomor (oleh Admin)**

   ```bash
   python admin.py
   ```

4. **Tampilkan Display Antrian**

   ```bash
   python display.py
   ```

---

## 📸 Screenshot (Opsional)

![image](https://github.com/user-attachments/assets/b813b1a7-40e7-4aca-8a97-3c3fe4f4cf6a)


---

## ⚠️ Catatan

* Pastikan kamu punya **printer** yang diset sebagai **default** di Windows
* File `antrian.json` akan otomatis dibuat jika belum ada
* QR Code bersifat sementara dan akan dihapus setelah tiket dicetak
* Jalankan semua file dari direktori yang sama

---

## 📄 Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pendidikan, kantor, klinik, atau instansi lainnya.

---

## 🙋‍♂️ Developer

**Hendra**
