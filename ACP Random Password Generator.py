import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except:
        password_output.delete(0, tk.END)
        password_output.insert(0, "Enter valid number!")
        return

    chars = ""
    if letters_var.get():
        chars += string.ascii_letters
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if chars == "":
        password_output.delete(0, tk.END)
        password_output.insert(0, "Select at least 1 option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))

    password_output.delete(0, tk.END)
    password_output.insert(0, password)



root = tk.Tk()
root.title("Password Generator")
root.geometry("320x350")
root.resizable(False, False)



tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)


tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)


letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A–Z)", variable=letters_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers (0–9)", variable=numbers_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor="w", padx=20)


tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=15)


tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
password_output = tk.Entry(root, width=32, font=("Arial", 12))
password_output.pack(pady=5)


root.mainloop()

