from tkinter import *
from tkinter.ttk import Progressbar
import sys

root = Tk()
root.resizable(0,0)

height = 430
width = 530
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.wm_attributes('-topmost', True)
root.wm_attributes('-alpha', 0.7)

root.overrideredirect(1)
root.config(background='#C400FF')

exit_btn = Button(root, text= 'X', command=lambda : exit_window(), font= ("yu gothic ui", 13, "bold"), fg="black", bg='#C400FF', bd=0, activebackground='#b800c4')
exit_btn.place(x=500, y=1)

welcome_label = Label(root, text="Welcome to my app", font= ("yu gothic ui", 30, "bold"), bg= '#C400FF')
welcome_label.place(x=90, y= 10)

image = PhotoImage(file='img\\a.png')
bg_label = Label(root, image=image, bg= '#C400FF')
bg_label.place(x=145, y= 65)

progress_label = Label(root, text='Please Wait...', font=("yu gothic ui", 13, "bold"), bg= '#C400FF')
progress_label.place(x= 190, y= 350)

progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x= 15, y= 390)

def exit_window():
    sys.exit(root.destroy())
    
i= 0

def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+ '%')
        progress_label.config(text=txt)
        progress_label.after(500, load)
        progress['value'] = 10 * i
        i += 1

load()


root.mainloop()