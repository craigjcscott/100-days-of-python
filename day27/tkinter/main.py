import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")  # needed to make label show up on screen







window.mainloop()  # creates a while loop that keeps the window running and awaiting instruction
