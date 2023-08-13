from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
import time
count = 5
while True:
    time.sleep(1)
    count -=1
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=RED, font=("Arial", 50))
label.grid(column=1, row=0)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
store = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=store)
canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold "))
canvas.grid(column=1, row=1)

s1 = Button(text="start")
s1.grid(column=0, row=2)
s2 = Button(text="reset")
s2.grid(column=2, row=2)


window.mainloop()