import tkinter as tk
from tkinter import messagebox
import pywhatkit
import pyautogui

def send_messages() :
    numbers = entry_numbers.get()
    if not numbers :
        messagebox.showerror("لطفا شماره ها را وارد کنید")
        return
    
    message = text_message.get("1.0",tk.END).strip()
    if not message :
        messagebox.showerror("لطفا پیام خود را وارد کنید")
        return

    num_list = [num.strip() for num in numbers.split(",")]
    
    for num in num_list :
        try:
            pywhatkit.sendwhatmsg_instantly(num, message, tab_close=True)
            pyautogui.press("enter")
            label_status.config(text=f"پیام به {num} ارسال شد")
        except Exception as e:
            messagebox.showerror("خطا", f"ارسال به {num} ناموفق بود: {e}")
    messagebox.showinfo("پایان", "ارسال پیام‌ها کامل شد")
    
window = tk.Tk()
window.title("ارسال پیام واتساپ")
window.geometry("500x300")

# ورودی شماره‌ها
tk.Label(window, text="شماره‌ها (با کاما جدا کنید):").pack()
entry_numbers = tk.Entry(window, width=40)
entry_numbers.pack(pady=5)

# ورودی پیام
tk.Label(window, text="متن پیام:").pack()
text_message = tk.Text(window, height=5, width=40)
text_message.pack(pady=5)

# دکمه ارسال
btn_send = tk.Button(window, text="ارسال پیام‌ها", command=send_messages)
btn_send.pack(pady=10)

# وضعیت
label_status = tk.Label(window, text="آماده ارسال...")
label_status.pack()

window.mainloop()