import tkinter as tk
import datetime as dt
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✓"
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    global checks
    checks = ""
    check_marks.config(text=checks)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps > 8:
        reset_timer()
        start_timer()
    elif reps % 8 == 0:  # every 8th rep
        count_down(LONG_BREAK_MIN * 60)  # long break
        title_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:  # every even rep (except 8th)
        count_down(SHORT_BREAK_MIN * 60)  # short break
        title_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:  # every odd rep
        count_down(WORK_MIN * 60)  # work timer
        title_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    time_remaining = dt.timedelta(0, count)  # calculate time remaining
    time_remaining_str = str(time_remaining)[2:]  # chops off the hours
    canvas.itemconfigure(timer_text, text=time_remaining_str)  # updates the time text
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # after 1 sec, run function with count -1
    else:
        global checks
        checks = math.floor(reps / 2) * CHECK
        check_marks.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
