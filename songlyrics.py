# import modules
from tkinter import *
import lyricsgenius


# user defined function
def get_lyrics():
    token = "fvE2QNpH7waL1QOw5EDnbBO2jztn6NRSGEvgKoYWzpK8qSNUc3-cB6TS3pPNFaNr"
    genius = lyricsgenius.Genius(token)
    song = genius.search_song(f"{e.get()}",f"{v.get()}")

    res = song.lyrics
    result.set(res)


# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name : ",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="Enter Singer name : ",
      bg="light grey").grid(row=1, sticky=W)

Label(master, text="Result :",
      bg="light grey").grid(row=3, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
      bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
v= Entry(master,width=50)

e.grid(row=0, column=1)
v.grid(row=1,column=1)

# creating a button using the widget
b = Button(master, text="Show",
           command=get_lyrics, bg="Blue")

b.grid(row=0, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5, )


mainloop()
