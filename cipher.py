import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    shift %= 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def process_cipher(mode):
    message = message_entry.get("1.0", "end-1c")
    try:
        shift = int(shift_value.get())
        if not 1 <= shift <= 25:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer between 1 and 25.")
        return
    
    result = caesar_cipher(message, shift, mode)
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)
    output_text.config(state="disabled")

def clear_fields():
    message_entry.delete("1.0", "end")
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.config(state="disabled")
    shift_value.set("")

# Create main window
root = tk.Tk()
root.title("Caesar Cipher - Red & Black Theme")
root.geometry("520x450")
root.resizable(False, False)

# Colors
bg_color = "#1c1c1c"
fg_color = "#ff4c4c"
entry_bg = "#2e2e2e"
btn_color = "#ff4c4c"
btn_text = "#ffffff"

root.configure(bg=bg_color)

# Header
header = tk.Label(root, text="Caesar Cipher - Encrypt & Decrypt", font=("Helvetica", 16, "bold"),
                  bg=bg_color, fg=fg_color)
header.pack(pady=15)

# Message Input
tk.Label(root, text="Enter Message:", font=("Helvetica", 12), bg=bg_color, fg=fg_color).pack(anchor="w", padx=20)
message_entry = tk.Text(root, height=5, bg=entry_bg, fg=btn_text, insertbackground=btn_text, wrap="word")
message_entry.pack(fill="x", padx=20, pady=5)

# Shift value
tk.Label(root, text="Shift Value (1-25):", font=("Helvetica", 12), bg=bg_color, fg=fg_color).pack(anchor="w", padx=20)
shift_value = tk.StringVar()
shift_entry = tk.Entry(root, textvariable=shift_value, bg=entry_bg, fg=btn_text, insertbackground=btn_text)
shift_entry.pack(fill="x", padx=20, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt", command=lambda: process_cipher("encrypt"),
                        bg=btn_color, fg=btn_text, font=("Helvetica", 10), width=10)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(btn_frame, text="Decrypt", command=lambda: process_cipher("decrypt"),
                        bg=btn_color, fg=btn_text, font=("Helvetica", 10), width=10)
decrypt_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields,
                      bg=btn_color, fg=btn_text, font=("Helvetica", 10), width=10)
clear_btn.grid(row=0, column=2, padx=5)

# Output
tk.Label(root, text="Output Message:", font=("Helvetica", 12), bg=bg_color, fg=fg_color).pack(anchor="w", padx=20)
output_text = tk.Text(root, height=5, state="disabled", bg=entry_bg, fg=btn_text, wrap="word")
output_text.pack(fill="x", padx=20, pady=5)

root.mainloop()