import tkinter as tk
from tkinter import *
import morseToEnglish
import englishToMorse
from tkinter import ttk

root = tk.Tk() 
root.title("morseCode Program")

#returns string
def getString():
	word = e1.get()
	if textchoice.get() == "convert to English":
		morseWord = morseToEnglish.morseToEnglish(word)
	if textchoice.get() == "convert to morse code":
		morseWord = englishToMorse.englishToMorse(word)
	
	tk.Label(root, text = " \t \t \t \t ").place(relx = .6, rely = .5, relheight = .07)
	tk.Label(root, text = morseWord, font = ("Helvetica", 15)).place(relx = .6, rely = .5, relheight = .07)


#Create initial size of program 
root.geometry("500x375")

#Title 
label = tk.Label(root, text='morseCode program by Christian Kubelle', font = '16').place(relx = 0.2, rely = 0.05, relwidth = .6, relheight = 0.07)

#What would you like to do: convert to English or convert to morse code
label = tk.Label(root, text='Would you like to:', font = '16').place(relx = 0.01, rely = 0.18, relwidth = .3, relheight = 0.07)

#Combobox
choices = ["convert to morse code", "convert to English"]
textchoice = StringVar()
box = ttk.Combobox(root, values = choices ,textvariable = textchoice).place(relx = .6, rely = .18, relheight = .07)

#Input
tk.Label(root, text="Enter a word or sentence in English: ", font = '32').place(relx = .041, rely = .35, relwidth = .5 , relheight = .07)
e1 = tk.Entry(root)
e1.place(relx = .6, rely = .35, relwidth = .29, relheight = .07)	

#Output
tk.Label(root, text = "This translate to: ", font = '32').place(relx = 0.01, rely = 0.5,  relwidth = .3, relheight = 0.07)




tk.Button(root, text = 'Quit', command=root.quit, font = '32').place(relx = 0, rely = .9, relwidth = .2, relheight = .1)
tk.Button(root, text = 'Translate', command=getString, font = '32').place(relx = 0.8, rely = .9, relwidth = .2, relheight = .1)


root.mainloop()