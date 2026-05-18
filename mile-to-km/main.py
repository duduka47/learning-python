from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_output = Label(text=0)
km_output.grid(column=1, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

def convert():
   miles = float(miles_input.get())
   km = miles * 1.609
   km_output.config(text=km)

calculate_btn = Button(text="Calculate", command=convert)
calculate_btn.grid(column=1, row=2)

window.mainloop()