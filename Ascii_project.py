from tkinter import *
# -*- coding: utf-8 -*-
root = Tk()
root.title("ASCII")
root.configure(background = 'azure')
root.geometry("400x500")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label= Label(root, text = "Name in ASCII : ", bg = "light blue", fg="black")
EN = Label(root, text = "Encrypted Name : ", bg = "light green",fg="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord (letter)) + "  "
        EN["text"] += str(chr(encrypted))
        ascii = int(ord(letter))
        encrypted = ascii -1
 
btn= Button(root, text="Show name in Ascii", command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5,rely=0.6, anchor = CENTER)
EN.place(relx=0.5,rely=0.7, anchor = CENTER)



root.mainloop()
