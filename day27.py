import tkinter

window = tkinter.Tk()
window.minsize(width=1000, height=1000)
window.title("My first GUI program")

label = tkinter.Label(text="i am  a label")
label.pack(side="left")


def button1():
    print("I got clicked")
    label.config(text="Button got clicked")


button = tkinter.Button(text="Click me", command=button1)
button.pack()

In = tkinter.Entry(width=100)
In.pack()
print(In.get())

window.mainloop()
