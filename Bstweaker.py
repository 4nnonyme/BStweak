import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox

# وظيفة لتنفيذ أوامر ADB
def run_adb_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

# الاتصال بالمحاكي
def connect_bluestacks():
    output = run_adb_command("adb connect localhost:5555")
    messagebox.showinfo("ADB Connection", output)

# تغيير DPI
def change_dpi():
    dpi_value = dpi_entry.get()
    if dpi_value.isdigit():
        command = f"adb shell wm density {dpi_value}"
        run_adb_command(command)
        messagebox.showinfo("DPI", f"DPI changed to {dpi_value}")
    else:
        messagebox.showerror("Error", "Please enter a valid number.")

# تغيير FPS
def change_fps():
    fps_value = fps_entry.get()
    if fps_value.isdigit():
        command = f"adb shell settings put system min_refresh_rate {fps_value} && adb shell settings put system peak_refresh_rate {fps_value}"
        run_adb_command(command)
        messagebox.showinfo("FPS", f"FPS changed to {fps_value}")
    else:
        messagebox.showerror("Error", "Please enter a valid number.")

# تثبيت APK
def install_apk():
    file_path = filedialog.askopenfilename(filetypes=[["APK Files", "*.apk"]])
    if file_path:
        command = f'adb install "{file_path}"'
        output = run_adb_command(command)
        messagebox.showinfo("Install APK", output)

# إنشاء الواجهة
tk = ctk.CTk()
tk.title("BlueStacks Tweaker - Created by 4nnonyme")
tk.geometry("500x600")
tk.configure(bg="#1E1E1E")

ctk.CTkButton(tk, text="Connect to BlueStacks", command=connect_bluestacks).pack(pady=10)

ctk.CTkLabel(tk, text="Set DPI:").pack()
dpi_entry = ctk.CTkEntry(tk)
dpi_entry.pack()
ctk.CTkButton(tk, text="Apply DPI", command=change_dpi).pack(pady=5)

ctk.CTkLabel(tk, text="Set FPS:").pack()
fps_entry = ctk.CTkEntry(tk)
fps_entry.pack()
ctk.CTkButton(tk, text="Apply FPS", command=change_fps).pack(pady=5)

ctk.CTkButton(tk, text="Install APK", command=install_apk).pack(pady=10)

tk.mainloop()
