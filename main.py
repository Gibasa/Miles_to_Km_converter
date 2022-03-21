from tkinter import *


def button_clicked():
    miles = float(input.get())
    km = miles*1.609
    result.config(text=f"{km}")


window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=3, row=0)

km = Label(text="Km")
km.grid(column=3, row=1)

button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=3)

result = Label(text="0")
result.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()