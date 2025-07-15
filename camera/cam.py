import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
frame = None

def ambil_gambar():
    global frame
    if frame is not None:
        cv2.imwrite('capture.jpg', frame)
        messagebox.showinfo('Info', 'Gambar disimpan sebagai capture.jpg')
    else:
        messagebox.showerror('Error', 'Frame belum tersedia')

def tutup():
    cap.release()
    root.destroy()

root = tk.Tk()
root.title('Camera Panel')

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

btn = tk.Button(root, text='Ambil Gambar', command=ambil_gambar)
btn.pack(side=tk.LEFT, padx=10, pady=10)
btn_quit = tk.Button(root, text='Keluar', command=tutup)
btn_quit.pack(side=tk.RIGHT, padx=10, pady=10)

def update_frame():
    global frame
    ret, frame = cap.read()
    if ret:
        # Convert frame to RGB and then to ImageTk
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
    root.after(10, update_frame)

update_frame()
root.mainloop()