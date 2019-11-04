import tkinter as tk
import morseToEnglish
root = tk.Tk() 
root.title("morseCode Program")


def getString():
	englishWord = e1.get()
	morseWord = morseToEnglish.main(englishWord)
	tk.Label(root, text = " \t \t \t \t ", font = '32').grid(row=2, column = 1)
	tk.Label(root, text = morseWord, font = '60').grid(row=2, column = 1)
	

label = tk.Label(root, text='morseCode program by Christian Kubelle', font = '32').grid(row=0, sticky=tk.NE)


tk.Label(root, text="Enter a word or sentence in English: ", font = '32').grid(row=1,sticky =tk.W)
tk.Label(root, text = "This translate to: ", font = '32').grid(row=2, column=0,sticky=tk.W)


e1 = tk.Entry(root)
e1.grid(row=1, column=1)	


tk.Button(root, text = 'Quit', command=root.quit, font = '32').grid(row=3, column = 0,sticky = tk.W)
tk.Button(root, text = 'Done', command=getString, font = '32').grid(row=3, column =2,sticky = tk.E)


root.mainloop()