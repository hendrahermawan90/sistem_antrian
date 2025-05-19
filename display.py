import tkinter as tk
from utils import cek_dan_reset_antrian

def update_display():
    try:
        data = cek_dan_reset_antrian()
        nomor = data.get("last_called", "-")
        label.config(text=f"SEKARANG DIPANGGIL:\n{nomor}")
    except:
        label.config(text="Tidak ada data")

    root.after(1000, update_display)

root = tk.Tk()
root.title("Display Antrian")
root.geometry("800x500")
root.configure(bg='black')

label = tk.Label(root, text="SEKARANG DIPANGGIL:\n-", font=("Arial", 60, "bold"), fg="white", bg="black")
label.pack(expand=True)

update_display()
root.mainloop()
