import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password():
    length = int(length_var.get())
    include_digits = digits_var.get()
    include_special = special_var.get()
    include_spaces = spaces_var.get()

    chars = list(string.ascii_letters)

    
    if include_digits:
        chars += list(string.digits)
    if include_special:
        chars += list('!@#$%^&*()-_=+[]{};:,.<>?/|')
    if include_spaces:
        chars += [' ']

    if not chars:
        password_var.set("Выберите хотя бы один тип символов")
        return

    password = []

    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice('!@#$%^&*()-_=+[]{};:,.<>?/|'))
    if include_spaces:
        password.append(' ')

    # остальные символы - буквы (а если не хватает длины, то добавляем случайные)
    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    password = password[:length]
    password_var.set(''.join(password))

root = tk.Tk()
root.title("Генератор паролей")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid()

ttk.Label(main_frame, text="Длина пароля:").grid(column=0, row=0, sticky="w")
length_var = tk.StringVar(value="12")
length_spin = ttk.Spinbox(main_frame, from_=4, to=32, textvariable=length_var, width=5)
length_spin.grid(column=1, row=0, sticky="w")

digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
spaces_var = tk.BooleanVar(value=False)

ttk.Checkbutton(main_frame, text="Включать цифры", variable=digits_var).grid(column=0, row=1, sticky="w")
ttk.Checkbutton(main_frame, text="Включать спецсимволы", variable=special_var).grid(column=0, row=2, sticky="w")
ttk.Checkbutton(main_frame, text="Включать пробелы", variable=spaces_var).grid(column=0, row=3, sticky="w")

ttk.Button(main_frame, text="Сгенерировать", command=generate_password).grid(column=0, row=4, pady=8, sticky="w")

password_var = tk.StringVar()
password_entry = ttk.Entry(main_frame, textvariable=password_var, width=30)
password_entry.grid(column=0, row=5, columnspan=2, sticky="we")

root.mainloop()