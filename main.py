from email.mime import image
from tkinter import *
from tkinter.ttk import Progressbar
import sys

root = Tk()
root.resizable(0,0)

height = 430
width = 530
x = (root.winfo_screenwidth()//2 - (width//2))
y = (root.winfo_screenheight()//2 - (height//2))
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1)
root.config(background='#b800c4')

exit_btn = Button(root, text= 'X', command=lambda : exit_window(), font= ("yu gothic ui", 13, "bold"), fg="black", bg='#b800c4', bd=0, activebackground='#b800c4')
exit_btn.place(x=500, y=1)

welcome_label = Label(root, text="Welcome to my app", font= ("yu gothic ui", 30, "bold"), bg= '#b800c4')
welcome_label.place(x=90, y= 15)

image = PhotoImage(file='./img/logo_1.png')

def exit_window():
    sys.exit(root.destroy())



root.mainloop()