import tkinter as tk
from tkinter import messagebox


# ==============================
# FUNGSI KALKULATOR
# ==============================

def tekan(tombol):
    """Menampilkan tombol yang ditekan pada layar kalkulator."""
    if tombol == "AC":
        layar_var.set("")
        hasil_var.set("")

    elif tombol == "DEL":
        teks = layar_var.get()
        layar_var.set(teks[:-1])

    elif tombol == "=":
        hitung()

    elif tombol == "×":
        layar_var.set(layar_var.get() + "*")

    elif tombol == "÷":
        layar_var.set(layar_var.get() + "/")

    else:
        layar_var.set(layar_var.get() + tombol)


def hitung():
    """Menghitung ekspresi matematika."""
    try:
        ekspresi = layar_var.get()

        if not ekspresi:
            return

        hasil = eval(ekspresi, {"__builtins__": None}, {})

        # Menghilangkan .0 jika hasil berupa bilangan bulat
        if isinstance(hasil, float) and hasil.is_integer():
            hasil = int(hasil)

        hasil_var.set("Hasil")
        layar_var.set(str(hasil))

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Tidak dapat membagi dengan nol!"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Operasi matematika tidak valid!"
        )


def keyboard(event):
    """Mendukung penggunaan keyboard."""
    tombol = event.char

    if tombol in "0123456789.+-*/()":
        if tombol == "*":
            layar_var.set(layar_var.get() + "*")
        else:
            layar_var.set(layar_var.get() + tombol)

    elif event.keysym == "Return":
        hitung()

    elif event.keysym == "BackSpace":
        layar_var.set(layar_var.get()[:-1])

    elif event.keysym == "Escape":
        layar_var.set("")
        hasil_var.set("")


# ==============================
# WINDOW
# ==============================

root = tk.Tk()
root.title("Kalkulator Desktop")
root.geometry("380x620")
root.resizable(False, False)

# Warna
BG = "#101114"
DISPLAY = "#181A1F"
TEXT = "#FFFFFF"
SECONDARY = "#A8ADB7"
BUTTON = "#24272E"
OPERATOR = "#3B82F6"
EQUAL = "#2563EB"
DANGER = "#DC2626"
HOVER = "#343943"


root.configure(bg=BG)


# ==============================
# VARIABEL
# ==============================

layar_var = tk.StringVar()
hasil_var = tk.StringVar()


# ==============================
# HEADER
# ==============================

header = tk.Frame(
    root,
    bg=BG
)
header.pack(
    fill="x",
    padx=25,
    pady=(22, 10)
)

judul = tk.Label(
    header,
    text="Kalkulator",
    font=("Segoe UI", 22, "bold"),
    fg=TEXT,
    bg=BG
)
judul.pack(side="left")

subjudul = tk.Label(
    header,
    text="DESKTOP",
    font=("Segoe UI", 9, "bold"),
    fg=OPERATOR,
    bg=BG
)
subjudul.pack(
    side="left",
    padx=(8, 0),
    pady=(9, 0)
)


# ==============================
# DISPLAY
# ==============================

display_frame = tk.Frame(
    root,
    bg=DISPLAY,
    height=145
)
display_frame.pack(
    fill="x",
    padx=20,
    pady=(5, 18)
)

display_frame.pack_propagate(False)


label_hasil = tk.Label(
    display_frame,
    textvariable=hasil_var,
    font=("Segoe UI", 10),
    fg=SECONDARY,
    bg=DISPLAY,
    anchor="e"
)
label_hasil.pack(
    fill="x",
    padx=20,
    pady=(15, 0)
)


layar = tk.Label(
    display_frame,
    textvariable=layar_var,
    font=("Segoe UI", 30, "bold"),
    fg=TEXT,
    bg=DISPLAY,
    anchor="e"
)
layar.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 15)
)


# ==============================
# TOMBOL
# ==============================

button_frame = tk.Frame(
    root,
    bg=BG
)
button_frame.pack(
    padx=20,
    fill="both",
    expand=True
)


tombol = [
    ["AC", "(", ")", "DEL"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "=", "+"]
]


def buat_tombol(parent, text, row, column):
    """Membuat tombol kalkulator."""

    if text == "AC":
        warna = DANGER
    elif text in ["÷", "×", "−", "+"]:
        warna = OPERATOR
    elif text == "=":
        warna = EQUAL
    elif text == "DEL":
        warna = "#4B5563"
    else:
        warna = BUTTON

    button = tk.Button(
        parent,
        text=text,
        font=("Segoe UI", 16, "bold"),
        fg=TEXT,
        bg=warna,
        activebackground=HOVER,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        cursor="hand2",
        command=lambda: tekan(text)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )

    return button


# Membuat grid tombol
for row in range(5):
    button_frame.rowconfigure(row, weight=1)

for column in range(4):
    button_frame.columnconfigure(column, weight=1)


for r, baris in enumerate(tombol):
    for c, nilai in enumerate(baris):
        buat_tombol(
            button_frame,
            nilai,
            r,
            c
        )


# ==============================
# FOOTER
# ==============================

footer = tk.Label(
    root,
    text="Python 3 • Tkinter",
    font=("Segoe UI", 8),
    fg="#6B7280",
    bg=BG
)
footer.pack(pady=(5, 12))


# ==============================
# KEYBOARD
# ==============================

root.bind("<Key>", keyboard)

# Fokus ke window
root.focus_force()

# Jalankan aplikasi
root.mainloop()
