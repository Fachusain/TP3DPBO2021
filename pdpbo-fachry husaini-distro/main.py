from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window")

myLabel = Label(root, text="Nama Distro:").grid(column=0, row=0)
nama = Entry(root, width=20, borderwidth=5)
nama.insert(0, "")
nama.grid(column=1, row=0)

myLabel = Label(root, text="Alamat:").grid(column=0, row=1)
alamat = Entry(root, width=20, borderwidth=5)
alamat.insert(0, "")
alamat.grid(column=1, row=1)

myLabel = Label(root, text="Produk:").grid(column=0, row=2)
produk = Entry(root, width=20, borderwidth=5)
produk.insert(0, "")
produk.grid(column=1, row=2)



myLabel = Label(root, text="Kategori:").grid(column=0, row=4)
options = [
    "Kaos",
    "Jaket",
    "Hoodie",
    "Jeans",
]

ram = StringVar()
ram.set(options[0])

drop = OptionMenu(root, ram, *options)
drop.grid(column=1, row=4)

myLabel = Label(root, text="Ukuran:").grid(column=0, row=5)
var1 = StringVar()

ukuran = Checkbutton(root, text="M", variable=var1, onvalue = "M", offvalue="")
ukuran.deselect()
ukuran.grid(column=3, row=5, columnspan=1)

var2 = StringVar()

ukuran = Checkbutton(root, text="L", variable=var2, onvalue = "L", offvalue="")
ukuran.deselect()
ukuran.grid(column=2, row=5, columnspan=1)

var3 = StringVar()

ukuran = Checkbutton(root, text="XL", variable=var3, onvalue = "XL", offvalue="")
ukuran.deselect()
ukuran.grid(column=1, row=5, columnspan=1)

myLabel = Label(root, text="Warna:").grid(column=0, row=6)

Colours = [
    ("Merah", "Merah"),
    ("Hijau", "Hijau"),
    ("Hitam", "Hitam"),
    ("Putih", "Putih")
]

colour = StringVar()
colour.set("")

i = 1
for text, colours, in Colours:
    Radiobutton(root, text=text, variable=colour, value=colours).grid(column=i, row=6)
    i = i + 1

photo = Button(root, text="Photo", fg="Black", bg="#FFFFFF")
photo.grid(column=0, row =8)

submit = Button(root, text="Submit", fg="Black",command=Lambda : popup(Nama.get(),Genre.get()colour.set), bg="#FFFFFF")
submit.grid(column=1, row =8)

SeeAllSubmit = Button(root, text="Show Data", fg="Black", bg="#FFFFFF")
SeeAllSubmit.grid(column=0, row =9)

ClearData = Button(root, text="Clear Data", fg="Black", bg="#FFFFFF")
ClearData.grid(column=1, row =9)

root.mainloop()