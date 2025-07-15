from unicodedata import name
import pyautogui as pag
import time
import tkinter as tk

def screenshot():
    # time.sleep(5)
    name = time.time()
    name = 'D:/Documents/New folder (2)/screenshot/{}.png'.format(name)
    img = pag.screenshot()
    img.save(name)
    img.show()
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Ambil Screenshot', command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text='Exit', command=quit)
close.pack(side=tk.LEFT)

root.mainloop()