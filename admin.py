import tkinter as tk
from tkinter import messagebox
import json
import os
import pyttsx3
from utils import cek_dan_reset_antrian

# Kelas untuk aplikasi pemanggil antrian
class LoketApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemanggil Antrian")
        self.master.geometry("350x220")
        self.nomor_dipanggil = 0

        # Inisialisasi modul text-to-speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)  # Mengatur kecepatan suara
        self.set_bahasa_indonesia()  # Mengatur bahasa menjadi Indonesia

        # Label untuk menampilkan nomor yang dipanggil
        self.label = tk.Label(master, text="Nomor Dipanggil:\n-", font=("Arial", 22), fg="blue")
        self.label.pack(pady=30)

        # Tombol untuk memanggil antrian
        self.btn = tk.Button(master, text="Panggil Antrian", font=("Arial", 12), bg="orange", fg="white", command=self.panggil)
        self.btn.pack(pady=10)

    # Fungsi untuk mengatur suara text-to-speech menjadi bahasa Indonesia
    def set_bahasa_indonesia(self):
        found = False
        for voice in self.engine.getProperty('voices'):
            if "indonesian" in voice.name.lower() or "id" in voice.id.lower():
                self.engine.setProperty('voice', voice.id)  # Mengatur suara ke bahasa Indonesia
                found = True
                break
        if not found:
            print("Voice Bahasa Indonesia tidak ditemukan, menggunakan default.")

    # Fungsi untuk memanggil antrian berikutnya
    def panggil(self):
        data = cek_dan_reset_antrian()  # Mendapatkan data antrian terkini
        last_number = data.get("last_number", 0)
        last_called = data.get("last_called", 0)

        if last_called < last_number:  # Memastikan ada nomor antrian yang belum dipanggil
            self.nomor_dipanggil = last_called + 1  # Menentukan nomor yang dipanggil
            self.label.config(text=f"Nomor Dipanggil:\n{self.nomor_dipanggil}")  # Menampilkan nomor yang dipanggil

            teks = f"Nomor antrian {self.nomor_dipanggil}, silakan ke loket"  # Pesan untuk diucapkan
            self.engine.say(teks)  # Mengucapkan pesan
            self.engine.runAndWait()  # Menunggu sampai selesai

            data["last_called"] = self.nomor_dipanggil  # Menyimpan nomor yang dipanggil
            with open("antrian.json", "w") as f:
                json.dump(data, f)
        else:
            messagebox.showinfo("Info", "Tidak ada antrian baru yang belum dipanggil.")  # Menampilkan pesan jika semua antrian sudah dipanggil

root = tk.Tk()
app = LoketApp(root)
root.mainloop()
