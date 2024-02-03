from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root=Tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('logo simpli.ico')
root['bg']='yellow'

root.title('Language Translator Sample')
Label(root, text="Language Translator",font="Arial 20 bold").pack()

root.mainloop()
