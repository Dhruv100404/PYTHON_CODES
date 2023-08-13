from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Miles to Kilometres Converter")
In = Entry()

In.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
kilo = Label(text="Km")
kilo.grid(column=2, row=1)
button = Button(text="calculate")
button.grid(column=1, row=2)

window.mainloop()
