from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

def butopenfile():
    
    global openinput
    window.filename = filedialog.askopenfilename(initialdir="/", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    alamatfile = window.filename
    
    if alamatfile:
        openinput = Image.open(alamatfile).resize(ukuran)
        dictfotoinput["image"] = ImageTk.PhotoImage(openinput)
        labelfotoinput.configure(image=dictfotoinput["image"])

def butgrayscale():

    datafotograyscale = newfotograyscale.load()
    datafotobrightness = newfotohasil.load()
    
    for xpos in range(openinput.width):
        for ypos in range(openinput.height):
            rbuf = openinput.getpixel((xpos,ypos))[0]
            gbuf = openinput.getpixel((xpos,ypos))[1]
            bbuf = openinput.getpixel((xpos,ypos))[2]
            imagedata.append([xpos, ypos, rbuf, gbuf, bbuf])

    for data in imagedata:
        x,y,r,g,b = data
        grayscale = ((r+g+b)/3)
        grayscale = int(grayscale)
        datafotograyscale[x,y] = (grayscale,grayscale,grayscale)
        datafotobrightness[x,y] = (grayscale,grayscale,grayscale)
        
    dictfotograyscale["image"] = ImageTk.PhotoImage(newfotograyscale)
    labelfotograyscale.configure(image=dictfotograyscale["image"])
    labelfotograyscale.image = dictfotograyscale["image"]
    
    dictfotohasil["image"] = ImageTk.PhotoImage(newfotohasil)
    labelfotohasil.configure(image=dictfotohasil["image"])
    labelfotohasil.image = dictfotohasil["image"]

def butbrightness():

    windowbrightness = Toplevel()
    datafotobrightness = newfotohasil.load()
    
    def getvalue():
         
        bright = int(entrybrightness.get())
        
        for data in imagedata:
            x,y,r,g,b = data
            grayscale = ((r+g+b)/3)
            grayscale = int(grayscale)
            brightadjust = (grayscale + bright)
            datafotobrightness[x,y] = (brightadjust,brightadjust,brightadjust)
            
        windowbrightness.destroy()
        
    entrybrightness = Entry(windowbrightness)
    okbrightbutton = Button(windowbrightness, text="Enter", command=getvalue)
    entrybrightness.grid(row=1, column=1)
    okbrightbutton.grid(row=1, column=2)
    
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

def printtext():
    print(1)

"""  Start Tkinter Window  """
window = Tk()
window.geometry('+500+190') #window position
window.resizable(0,0)

"""  Deklarasi Variabel  """
ukuran = (150,250)
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
buttoninput = Button(window, text="Open Files", command=butopenfile)
buttongrayscale = Button(window, text="Grayscale", command=butgrayscale)
buttonbrightness = Button(window, text="Brightness Adjusment", command=butbrightness)
buttonnegation = Button(window, text="Negation", command=printtext)
buttonrestart = Button(window, text="Reset", command=restart)

framefotoinput.grid(row=1, column=1, sticky=EW)
framefotograyscale.grid(row=1, column=2, sticky=EW)
framefotohasil.grid(row=1, column=3, sticky=EW)

buttoninput.grid(row = 3, column = 1, sticky=EW)
buttongrayscale.grid(row = 4, column = 1, sticky=EW)
buttonbrightness.grid(row = 5, column = 1, sticky=EW)
buttonnegation.grid(row = 6, column = 1, sticky=EW)
buttonrestart.grid(row = 7, column = 1, sticky=EW)

window.mainloop()