from tkinter import *


def convert_miles_to_kilometers():
    miles = float(entry_miles.get())
    kilometers = miles * 1.60934
    label_result.config(text=f"{kilometers:.2f} km")


# Create main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

# Create and position widgets
entry_miles = Entry(width=10)
label_miles = Label(text="Miles")
label_equals = Label(text="is equal to")
label_result = Label(text="0 km")
button_convert = Button(text="Convert", command=convert_miles_to_kilometers)

entry_miles.grid(row=0, column=1, pady=5, padx=5)
label_miles.grid(row=0, column=2, pady=5, padx=5)
label_equals.grid(row=1, column=0, pady=5, padx=5)
label_result.grid(row=1, column=1, padx=5, pady=5)
button_convert.grid(row=2, column=1, padx=5, pady=5)

mainloop()