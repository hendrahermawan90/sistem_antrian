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

# Membuat direktori jika belum ada
def buat_folder():
    os.makedirs("tiket/pdf", exist_ok=True)
    os.makedirs("tiket/qr", exist_ok=True)

def cek_printer():
    try:
        printers = win32print.EnumPrinters(2)
        print("Printer terdeteksi:")
        for p in printers:
            print(p[2])  # Nama printer

        printer_name = win32print.GetDefaultPrinter()
        if not printer_name:
            raise Exception("Tidak ada printer default yang ditemukan.")
        return printer_name
    except Exception as e:
        messagebox.showerror("Error Printer", str(e))
        return None

def cetak_pdf_tiket(nomor):
    buat_folder()
    printer_name = cek_printer()
    if not printer_name:
        return

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Buat QR code
    qr_data = f"Nomor Antrian: {nomor}\nWaktu: {waktu}"
    qr = qrcode.make(qr_data)
    qr_path = f"tiket/qr/qr_{nomor}.png"
    qr.save(qr_path)

    # Buat PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="--- TIKET ANTRIAN ---", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Nomor Antrian: {nomor}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Waktu Cetak: {waktu}", ln=True, align="C")
    pdf.cell(200, 10, txt="Harap tunggu hingga dipanggil.", ln=True, align="C")
    pdf.image(qr_path, x=80, y=80, w=50)

    pdf_output = f"tiket/pdf/tiket_{nomor}.pdf"
    pdf.output(pdf_output)

    # Cetak ke printer
    try:
        win32api.ShellExecute(0, "print", pdf_output, f'/d:"{printer_name}"', ".", 0)
    except Exception as e:
        messagebox.showerror("Error Pencetakan", f"Gagal mencetak tiket: {str(e)}")

    # Hapus QR setelah selesai
    if os.path.exists(qr_path):
        os.remove(qr_path)

    # Simpan ke log CSV
    with open("log_antrian.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nomor, waktu])

def ambil_antrian():
    hari_ini = datetime.now().strftime("%Y-%m-%d")

    # Baca file JSON
    try:
        with open("antrian.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"last_number": 0, "last_date": hari_ini}

    # Reset otomatis jika hari berganti
    if data.get("last_date") != hari_ini:
        data["last_number"] = 0
        data["last_date"] = hari_ini
        messagebox.showinfo("Reset Otomatis", "Antrian telah direset karena hari berganti.")

    # Tambah nomor
    data["last_number"] += 1

    # Simpan kembali ke file
    with open("antrian.json", "w") as f:
        json.dump(data, f)

    nomor = data["last_number"]
    label_hasil.config(text=f"Nomor Anda: {nomor}")
    cetak_pdf_tiket(nomor)

# GUI
root = tk.Tk()
root.title("Ambil Antrian")
root.geometry("300x250")

label = tk.Label(root, text="Klik untuk Ambil Antrian", font=("Arial", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Ambil Antrian", font=("Arial", 12), bg="green", fg="white", command=ambil_antrian)
btn.pack(pady=10)

label_hasil = tk.Label(root, text="", font=("Arial", 16), fg="blue")
label_hasil.pack(pady=10)

root.mainloop()
