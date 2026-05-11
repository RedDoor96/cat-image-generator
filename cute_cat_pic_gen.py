import requests as req
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import PhotoImage
import io
from PIL import Image, ImageTk

root = ttk.Window(themename='vapor')
root.title('cat images :)')
root.geometry('800x800')
url = 'https://api.thecatapi.com/v1/images/search'

def gen_cat():
    global img
    respone = req.get(url)
    data = respone.json()
    img_url = data[0]['url']
    img_data = req.get(img_url).content

    image = Image.open(io.BytesIO(img_data))
    image = image.resize((780,700))
    photo = ImageTk.PhotoImage(image)

    panel.config(image=photo)
    panel.image = photo



panel = tk.Label(root)
panel.pack(side = "bottom", fill = "both", expand = True)

gen_cat_button = ttk.Button(root, text='generate cat', command=gen_cat)

gen_cat_button.pack(pady=10)

gen_cat()

tk.mainloop()