from cProfile import label
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
import numpy as np
import os


histograypath = "src/temp/grayscale.png"
histohasilpath = "src/temp/hasil.png"

def create_histogray():
    array_grayscale = []
    for data in imagedata:
        array_grayscale.append(data[2])
    
    plt.hist(array_grayscale, bins=255)
    plt.savefig(histograypath) #save path
    plt.clf()
    
def create_histohasil():
    array_hasil = []   
    for data in hasildata:
        array_hasil.append(data[2]) 

    plt.hist(array_hasil, bins=255)
    plt.savefig(histohasilpath) #save path
    plt.clf()
    
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
    
    create_histogray()
    
    grayhisto = Image.open(histograypath).resize(ukuranhisto)
    dictgrayhisto["image"] = ImageTk.PhotoImage(grayhisto)
    labelgrayhisto.configure(image=dictgrayhisto["image"])
    

def adjust_brightness():
    datafotobrightness = newfotohasil.load()
    value = simpledialog.askinteger(title= "Brightness Value", prompt= "Value")
    hasildata.clear()
    
    if (value == 0):
        dictfotohasil["image"] = ImageTk.PhotoImage(newfotograyscale)
    elif value:
        for data in imagedata:
            x,y,grayscale = data
            newgray = grayscale + value
            hasildata.append([x,y,newgray])
            
            datafotobrightness[x,y] = (newgray, newgray, newgray)
    
    create_histogray()
        
    dictfotohasil["image"] = ImageTk.PhotoImage(newfotohasil)    
    labelfotohasil.configure(image=dictfotohasil["image"])
    
def negation():
    datafotonegation = newfotohasil.load()
    
    for data in imagedata:
        x,y,grayscale = data
        negasi = 255 - grayscale
        hasildata.append([x,y,negasi])        
        
        datafotonegation[x,y] = (negasi, negasi, negasi)
    
    create_histogray()
    
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
    
    newgrayhisto = Image.new("RGB", ukuranhisto)
    dictgrayhisto["image"] = ImageTk.PhotoImage(newgrayhisto)
    labelgrayhisto.configure(image = dictgrayhisto["image"])

""" CLOSE PROTOCOL """  
def closeprotcol():

    if os.path.exists(histograypath) == True: 
        os.remove(histograypath)
        plt.close('all')
        window.destroy()
    else:
        plt.close('all') #harus diisi soalnya powershellnya jadi ga jalan karna matplotlibnya masih jalan di background (harus di close)
        window.destroy()

"""  Start Tkinter Window  """
window = Tk()
window.geometry('+300+25') #window position
window.resizable(0,0)
window.title("Pointwise Grayscale")

"""  Deklarasi Variabel  """
ukuran = (300,450)
ukuranhisto = (450,450)
imagedata = []
hasildata = []
dictfotoinput, dictfotograyscale, dictfotohasil, dictgrayhisto, dicthasilhisto = dict(), dict(), dict(), dict(), dict()

"""  Deklarasi Frame  """
framefotoinput = Frame(window)
framefotograyscale = Frame(window)
framefotohasil = Frame(window)
framehistogray = Frame(window)
framehistohasil = Frame(window)

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

newgrayhisto = Image.new("RGB", ukuranhisto)
dictgrayhisto['image'] = ImageTk.PhotoImage(newgrayhisto)
labelgrayhisto = Label(framehistogray, image=dictgrayhisto['image'])

newhasilhisto = Image.new("RGB", ukuranhisto)
dicthasilhisto['image'] = ImageTk.PhotoImage(newhasilhisto)
labelhasilhisto = Label(framehistohasil, image=dictgrayhisto['image'])

labelfotoinput.pack()
labelfotograyscale.pack()
labelfotohasil.pack()
labelgrayhisto.pack()

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
framefotohasil.grid(row=2, column=2, rowspan=10, sticky=EW)
framehistogray.grid(row=1, column=3, sticky=EW)
framehistohasil.grid(row=2, column=3, sticky=EW)

buttoninput.grid(row = 2, column = 1, sticky=EW)
buttongrayscale.grid(row = 3, column = 1, sticky=EW)
buttonbrightness.grid(row = 4, column = 1, sticky=EW)
buttonnegation.grid(row = 5, column = 1, sticky=EW)
buttonrestart.grid(row = 6, column = 1, sticky=EW)

""" AKTIVASI PROTOCOL"""
window.protocol("WM_DELETE_WINDOW", closeprotcol)
window.mainloop()