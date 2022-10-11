from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
import numpy as np

"""
def histogram():
    array_grayscale = []
    for data in imagedata:
        array_grayscale.append(data[2])
        
    plt.hist(array_grayscale, bins=255)
    plt.show()
"""

def openfile():
    
    global openinput
    window.filename = filedialog.askopenfilename(initialdir="../test", filetypes=(("Image Files", "*.png *.jpg *.jpeg"), ("All Files", "*.*")))
    alamatfile = window.filename
    
    if alamatfile:
        openinput = Image.open(alamatfile).resize(ukuran)
        dictfotoinput["image"] = ImageTk.PhotoImage(openinput)
        labelfotoinput.configure(image=dictfotoinput["image"])

def convert_grayscale():
    imagedata.clear()
    datafotograyscale = newfotograyscale.load()
    
    for xpos in range(openinput.width):
        for ypos in range(openinput.height):
            rbuf = openinput.getpixel((xpos,ypos))[0]
            gbuf = openinput.getpixel((xpos,ypos))[1]
            bbuf = openinput.getpixel((xpos,ypos))[2]
            imagedata.append([xpos, ypos, rbuf, gbuf, bbuf])
 
    #mengubah rgb value ke grayscale & update array
    for i, data in enumerate(imagedata):
        x,y,r,g,b = data
        grayscale = ((r+g+b)/3)
        grayscale = int(grayscale)
        imagedata[i] = x,y,grayscale
        
        datafotograyscale[x,y] = (grayscale,grayscale,grayscale)

    dictfotograyscale["image"] = ImageTk.PhotoImage(newfotograyscale)
    labelfotograyscale.configure(image=dictfotograyscale["image"])

def adjust_brightness():
    datafotobrightness = newfotohasil.load()
    value = simpledialog.askinteger(title= "Brightness Value", prompt= "Value") 
    
    if value:
        for data in imagedata:
            x,y,grayscale = data
            newgray = grayscale + value
            
            datafotobrightness[x,y] = (newgray, newgray, newgray)
        
    dictfotohasil["image"] = ImageTk.PhotoImage(newfotohasil)
    labelfotohasil.configure(image=dictfotohasil["image"])
    
def negation():
    datafotonegation = newfotohasil.load()
    
    for data in imagedata:
        x,y,grayscale = data
        negasi = 255 - grayscale
        
        datafotonegation[x,y] = (negasi, negasi, negasi)
    
    dictfotohasil["image"] = ImageTk.PhotoImage(newfotohasil)
    labelfotohasil.configure(image=dictfotohasil["image"])
    
def restart():
    
    newfotoinput = Image.new("RGB", ukuran)
    dictfotoinput["image"] = ImageTk.PhotoImage(newfotoinput)
    labelfotoinput.configure(image = dictfotoinput["image"])

    newfotograyscale = Image.new("RGB", ukuran)
    dictfotograyscale['image'] = ImageTk.PhotoImage(newfotograyscale)
    labelfotograyscale.configure(image = dictfotograyscale["image"])
    
    newfotohasil = Image.new("RGB", ukuran)
    dictfotohasil['image'] = ImageTk.PhotoImage(newfotohasil)
    labelfotohasil.configure(image = dictfotohasil["image"])

"""  Start Tkinter Window  """
window = Tk()
window.geometry('+300+25') #window position
window.resizable(0,0)
window.title("Pointwise Grayscale")

"""  Deklarasi Variabel  """
ukuran = (200,350)
imagedata = []
dictfotoinput, dictfotograyscale, dictfotohasil = dict(), dict(), dict()

"""  Deklarasi Frame  """
framefotoinput = Frame(window)
framefotograyscale = Frame(window)
framefotohasil = Frame(window)

"""  Deklarasi Image Kosong  """
newfotoinput = Image.new("RGB", ukuran)
dictfotoinput["image"] = ImageTk.PhotoImage(newfotoinput)
labelfotoinput = Label(framefotoinput, image=dictfotoinput['image'])

newfotograyscale = Image.new("RGB", ukuran)
dictfotograyscale['image'] = ImageTk.PhotoImage(newfotograyscale)
labelfotograyscale = Label(framefotograyscale, image=dictfotograyscale["image"])

newfotohasil = Image.new("RGB", ukuran)
dictfotohasil['image'] = ImageTk.PhotoImage(newfotohasil)
labelfotohasil = Label(framefotohasil, image=dictfotohasil['image'])

labelfotoinput.pack()
labelfotograyscale.pack()
labelfotohasil.pack()

"""  Button  """
buttoninput = Button(window, text="Open Files", command=openfile)
buttongrayscale = Button(window, text="Grayscale", command=convert_grayscale)
buttonbrightness = Button(window, text="Brightness Adjusment", command=adjust_brightness)
buttonnegation = Button(window, text="Negation", command=negation)
buttongamma = Button(window, text="Gamma Correction")
buttoncontrast1 = Button(window, text="Contrast Stretching 1")
buttoncontrast2 = Button(window, text="Contrast Stretching 2")
buttonintensity1 = Button(window, text="Intensity Slicing 1")
buttonintensity2 = Button(window, text="Intensity Slicing 2")
buttonbitextract = Button(window, text="Bit Extraction")
buttonRangecompress = Button(window, text="Range Compression")
buttonekualisasihistogram = Button(window, text="Ekualisasi Histogram")
buttonrestart = Button(window, text="Reset", command=restart)


framefotoinput.grid(row=1, column=1, sticky=EW)
framefotograyscale.grid(row=1, column=2, sticky=EW)
framefotohasil.grid(row=2, column=2, rowspan=14, sticky=EW)

buttoninput.grid(row = 2, column = 1, sticky=EW)
buttongrayscale.grid(row = 3, column = 1, sticky=EW)
buttonbrightness.grid(row = 4, column = 1, sticky=EW)
buttonnegation.grid(row = 5, column = 1, sticky=EW)
buttongamma.grid(row = 6, column = 1, sticky=EW)
buttoncontrast1.grid(row = 7, column = 1, sticky=EW)
buttoncontrast2.grid(row = 8, column = 1, sticky=EW)
buttonintensity1.grid(row = 9, column = 1, sticky=EW)
buttonintensity2.grid(row = 10, column = 1, sticky=EW)
buttonbitextract.grid(row = 11, column = 1, sticky=EW)
buttonRangecompress.grid(row = 12, column = 1, sticky=EW)
buttonekualisasihistogram.grid(row = 13, column = 1, sticky=EW)
buttonrestart.grid(row = 14, column = 1, sticky=EW)

window.mainloop()