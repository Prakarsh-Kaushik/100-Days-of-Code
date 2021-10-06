from tkinter import *

def mile_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.60934
    kilometer_result.config(text=km)


window = Tk()
window.title("Miles to Kilometer Convertor")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculator", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()