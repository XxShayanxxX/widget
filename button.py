
from tkinter import  *

window = Tk()

window.title("Shayan :D")
window.geometry("700x400")

label = Label(text = "Hello World", fg = "white", bg = "black", width = 100)
label.pack()


entry = Entry(fg = "black", bg ="grey" , width= 50 ).pack()

def display():
    name = entry.get()
    msg = "welcome to tkinter "
    greeting = "hello" + name + "\n"
    textbox.insert(END, msg + greeting) 


    
button = Button(text = "Click Me", fg = "white", bg = "black" , command = display).pack()


textbox = Text()
textbox.pack()

window.mainloop()



   



window.mainloop()