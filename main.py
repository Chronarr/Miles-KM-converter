import tkinter


def convert():
    if input_km.get() == "":
        result = float(input_miles.get()) * 1.609344
        input_km.insert(0, result.__round__(2))
        button_calculate.config(text="Clear", command=clear)
    elif input_miles.get() == "":
        result = float(input_km.get()) * 0.62137119
        input_miles.insert(0, result.__round__(2))
        button_calculate.config(text="Clear", command=clear)
    else:
        clear()


def clear():
    input_miles.delete(0, "end")
    input_km.delete(0, "end")
    button_calculate.config(text="Calculate", command=convert)


window = tkinter.Tk()
window.title("Km / miles converter")
window.minsize(300,150)
window.config(pady=40,padx=40)

top_label = tkinter.Label(text="Enter either Kilometers or miles and click calculate:")
top_label.grid(column=1,row=0)
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)
miles_label = tkinter.Label(text="m")
miles_label.grid(column=2,row=2)

input_km = tkinter.Entry(width=40)
input_km.grid(column=1, row=1)
input_miles = tkinter.Entry(width=40)
input_miles.grid(column=1,row=2)

button_calculate = tkinter.Button(text="Calculate", command=convert)
button_calculate.grid(column=1, row=3)

tkinter.mainloop()
