import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
import qrcode
from fpdf import FPDF
import csv
import win32api
import win32print
from utils import cek_dan_reset_antrian

# Fungsi untuk membuat folder tempat penyimpanan tiket PDF dan QR Code
def buat_folder():
    os.makedirs("tiket/pdf", exist_ok=True)  # Membuat folder pdf jika belum ada
    os.makedirs("tiket/qr", exist_ok=True)  # Membuat folder qr jika belum ada

# Fungsi untuk mengecek apakah printer tersedia dan mendeteksi printer default
def cek_printer():
    try:
        printers = win32print.EnumPrinters(2)  # Mendapatkan daftar printer
        print("Printer terdeteksi:")
        for p in printers:
            print(p[2])  # Menampilkan nama printer
        return win32print.GetDefaultPrinter()  # Mengembalikan printer default
    except Exception as e:
        messagebox.showerror("Error Printer", str(e))  # Menampilkan error jika gagal mendeteksi printer
        return None

# Fungsi untuk mencetak tiket dalam format PDF
def cetak_pdf_tiket(nomor):
    buat_folder()  # Membuat folder jika belum ada
    printer_name = cek_printer()  # Mengecek printer yang tersedia
    if not printer_name:
        return  # Jika tidak ada printer, keluar dari fungsi

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Mendapatkan waktu saat ini
    qr_data = f"Nomor Antrian: {nomor}\nWaktu: {waktu}"  # Data untuk QR Code
    qr = qrcode.make(qr_data)  # Membuat QR Code dari data
    qr_path = f"tiket/qr/qr_{nomor}.png"  # Menyimpan QR Code ke file
    qr.save(qr_path)

    # Membuat PDF untuk tiket
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="--- TIKET ANTRIAN ---", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Nomor Antrian: {nomor}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Waktu Cetak: {waktu}", ln=True, align="C")
    pdf.cell(200, 10, txt="Harap tunggu hingga dipanggil.", ln=True, align="C")
    pdf.image(qr_path, x=80, y=80, w=50)  # Menyisipkan QR Code ke dalam PDF

    pdf_output = f"tiket/pdf/tiket_{nomor}.pdf"  # Path untuk menyimpan PDF
    pdf.output(pdf_output)  # Menyimpan PDF

    # Mencetak tiket menggunakan printer default
    try:
        win32api.ShellExecute(0, "print", pdf_output, f'/d:"{printer_name}"', ".", 0)
    except Exception as e:
        messagebox.showerror("Error Pencetakan", f"Gagal mencetak tiket: {str(e)}")  # Menampilkan error jika gagal cetak

    # Menghapus file QR Code setelah dicetak
    if os.path.exists(qr_path):
        os.remove(qr_path)

    # Menyimpan log tiket ke dalam file CSV
    with open("log_antrian.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nomor, waktu])  # Menulis nomor dan waktu ke file log

# Fungsi untuk mengambil nomor antrian baru
def ambil_antrian():
    global label_hasil  # Mengakses label_hasil dari fungsi
    data = cek_dan_reset_antrian()  # Mendapatkan data antrian terkini
    data["last_number"] += 1  # Increment nomor antrian

    # Menyimpan nomor antrian terbaru ke dalam file JSON
    with open("antrian.json", "w") as f:
        json.dump(data, f)

    nomor = data["last_number"]
    label_hasil.config(text=f"Nomor Anda: {nomor}")  # Menampilkan nomor antrian
    cetak_pdf_tiket(nomor)  # Mencetak tiket untuk nomor antrian

# Membuat antarmuka pengguna menggunakan tkinter
root = tk.Tk()
root.title("Ambil Antrian")
root.geometry("300x250")

label = tk.Label(root, text="Klik untuk Ambil Antrian", font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Ambil Antrian", font=("Arial", 12), bg="green", fg="white", command=ambil_antrian)
btn.pack(pady=10)

label_hasil = tk.Label(root, text="", font=("Arial", 16), fg="blue")
label_hasil.pack(pady=10)

root.mainloop()  # Menjalankan aplikasi GUI
