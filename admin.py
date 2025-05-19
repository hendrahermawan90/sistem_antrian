import tkinter as tk
from tkinter import messagebox
import json
import os
import pyttsx3
from utils import cek_dan_reset_antrian

class LoketApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemanggil Antrian")
        self.master.geometry("350x220")
        self.nomor_dipanggil = 0

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.set_bahasa_indonesia()

        self.label = tk.Label(master, text="Nomor Dipanggil:\n-", font=("Arial", 22), fg="blue")
        self.label.pack(pady=30)

        self.btn = tk.Button(master, text="Panggil Antrian", font=("Arial", 12), bg="orange", fg="white", command=self.panggil)
        self.btn.pack(pady=10)

    def set_bahasa_indonesia(self):
        for voice in self.engine.getProperty('voices'):
            if "indonesian" in voice.name.lower() or "id" in voice.id.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def panggil(self):
        data = cek_dan_reset_antrian()
        last_number = data.get("last_number", 0)
        last_called = data.get("last_called", 0)

        if last_called < last_number:
            self.nomor_dipanggil = last_called + 1
            self.label.config(text=f"Nomor Dipanggil:\n{self.nomor_dipanggil}")

            teks = f"Nomor antrian {self.nomor_dipanggil}, silakan ke loket"
            self.engine.say(teks)
            self.engine.runAndWait()

            data["last_called"] = self.nomor_dipanggil
            with open("antrian.json", "w") as f:
                json.dump(data, f)
        else:
            messagebox.showinfo("Info", "Tidak ada antrian baru yang belum dipanggil.")

root = tk.Tk()
app = LoketApp(root)
root.mainloop()
