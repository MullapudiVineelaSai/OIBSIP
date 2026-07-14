import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate():
    length = int(length_scale.get())
    chars = ""
    
    if var_upper.get(): 
        chars += string.ascii_uppercase
    if var_lower.get(): 
        chars += string.ascii_lowercase
    if var_digit.get(): 
        chars += string.digits
    if var_symbol.get(): 
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Minimum 1 character type select cheyali")
        return
    
    password = "".join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy():
    if password_entry.get() == "":
        messagebox.showwarning("Warning", "First password generate chey")
    else:
        pyperclip.copy(password_entry.get())
        messagebox.showinfo("Copied", "Password Copied to Clipboard!")

# Main Window
root = tk.Tk()
root.title("Password Generator - Advanced Tier")
root.geometry("400x380")
root.resizable(False, False)

tk.Label(root, text="=== Random Password Generator ===", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 11)).pack()
length_scale = tk.Scale(root, from_=8, to=32, orient='horizontal', length=300)
length_scale.set(12)
length_scale.pack()

tk.Label(root, text="Select Character Types:", font=("Arial", 11)).pack(pady=5)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digit = tk.BooleanVar(value=True)
var_symbol = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase A-Z", variable=var_upper).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Lowercase a-z", variable=var_lower).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Numbers 0-9", variable=var_digit).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Symbols !@#$%^&*", variable=var_symbol).pack(anchor='w', padx=50)

tk.Button(root, text="Generate Password", command=generate, bg="lightgreen", width=25, font=("Arial", 11, "bold")).pack(pady=15)

password_entry = tk.Entry(root, width=40, font=("Arial", 12))
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy, bg="lightblue", width=25, font=("Arial", 11, "bold")).pack(pady=5)

root.mainloop()
