import tkinter


def button_clicked():
    new_text = my_input.get()
    if new_text != "":
        my_label["text"] = new_text


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Newer Text")
# my_label.pack()  # pack is too opaque, it puts things together for you
# my_label.place(x=100, y=200)  # place is too specific, requires exact coordinates
my_label.grid(column=0, row=0)  # cannot use both grid and pack in same program
my_label.config(padx=50, pady=50)

# Button
my_button = tkinter.Button(text="Click me!", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()  # creates a while loop that keeps the window running and awaiting instruction

