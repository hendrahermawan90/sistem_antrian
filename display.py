import tkinter as tk
from utils import cek_dan_reset_antrian

# Fungsi untuk memperbarui tampilan nomor antrian yang sedang dipanggil
def update_display():
    try:
        data = cek_dan_reset_antrian()  # Mendapatkan data antrian terkini
        nomor = data.get("last_called", "-")  # Mendapatkan nomor yang dipanggil
        label.config(text=f"SEKARANG DIPANGGIL:\n{nomor}")  # Menampilkan nomor yang dipanggil
    except Exception as e:
        label.config(text="Tidak ada data")  # Menampilkan pesan jika data tidak ada
        print(f"Error: {e}")  # Menampilkan error jika terjadi masalah dalam mengambil data

    root.after(1000, update_display)  # Memperbarui tampilan setiap 1000 ms (1 detik)

root = tk.Tk()
root.title("Display Antrian")
root.geometry("800x500")
root.configure(bg='black')

# Label untuk menampilkan nomor yang dipanggil
label = tk.Label(root, text="SEKARANG DIPANGGIL:\n-", font=("Arial", 60, "bold"), fg="white", bg="black")
label.pack(expand=True)

update_display()  # Memulai pembaruan tampilan
root.mainloop()
