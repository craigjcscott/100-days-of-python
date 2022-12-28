import tkinter as tk


def mile2km():
    miles_in = input_miles.get()
    km_out = 1.61 * float(miles_in)
    result_label["text"] = km_out


window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

input_miles = tk.Entry(width=8)
input_miles.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = tk.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

result_label = tk.Label()
result_label.grid(row=1, column=1)

convert_button = tk.Button(text="Convert", command=mile2km)
convert_button.grid(row=2, column=1)

window.mainloop()
