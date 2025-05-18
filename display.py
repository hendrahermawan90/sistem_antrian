import tkinter as tk
import json

def update_display():
    try:
        with open("antrian.json", "r") as f:
            data = json.load(f)
            nomor = data.get("last_called", "-")
            label.config(text=f"SEKARANG DIPANGGIL:\n{nomor}")
    except:
        label.config(text="Tidak ada data")

    root.after(1000, update_display)

# Buat window
root = tk.Tk()
root.title("Display Antrian")
root.geometry("800x500")  # Ukuran jendela biasa
root.configure(bg='black')

# Label tampilan nomor
label = tk.Label(root, text="SEKARANG DIPANGGIL:\n-", font=("Arial", 60, "bold"), fg="white", bg="black")
label.pack(expand=True)

# Jalankan update & mainloop
update_display()
root.mainloop()
