import tkinter as tk
from tkinter import messagebox
import json
import os
import pyttsx3

class LoketApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemanggil Antrian")
        self.master.geometry("350x220")
        self.nomor_dipanggil = 0

        # Inisialisasi engine suara
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)  # Kecepatan bicara

        # Pilih suara Bahasa Indonesia jika tersedia
        self.set_bahasa_indonesia()

        # UI
        self.label = tk.Label(master, text="Nomor Dipanggil:\n-", font=("Arial", 22), fg="blue")
        self.label.pack(pady=30)

        self.btn = tk.Button(master, text="Panggil Antrian", font=("Arial", 12), bg="orange", fg="white", command=self.panggil)
        self.btn.pack(pady=10)

    def set_bahasa_indonesia(self):
        # Cari voice dengan 'indonesian' atau 'id' di deskripsinya
        for voice in self.engine.getProperty('voices'):
            if "indonesian" in voice.name.lower() or "id" in voice.id.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def panggil(self):
        if os.path.exists("antrian.json"):
            with open("antrian.json", "r") as f:
                data = json.load(f)

            last_number = data.get("last_number", 0)
            last_called = data.get("last_called", 0)

            if last_called < last_number:
                self.nomor_dipanggil = last_called + 1
                self.label.config(text=f"Nomor Dipanggil:\n{self.nomor_dipanggil}")

                # Ucapkan dengan TTS
                teks = f"Nomor antrian {self.nomor_dipanggil}, silakan ke loket"
                self.engine.say(teks)
                self.engine.runAndWait()

                # Simpan status terakhir yang dipanggil
                data["last_called"] = self.nomor_dipanggil
                with open("antrian.json", "w") as f:
                    json.dump(data, f)

            else:
                messagebox.showinfo("Info", "Tidak ada antrian baru yang belum dipanggil.")
        else:
            messagebox.showerror("File Tidak Ditemukan", "File antrian.json belum tersedia.")

# Jalankan aplikasi
root = tk.Tk()
app = LoketApp(root)
root.mainloop()
