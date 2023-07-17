import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    print(count)
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Check marks
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24))
canvas.grid(column=2, row=2)
canvas.place(x=1, y=30)

# Label
my_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=2, row=1)
my_label.place(x=40, y=-30)

# Button
button_1 = Button(text="Start", width=10, highlightthickness=0, command=start_timer)
button_1.grid(column=1, row=3)
button_1.place(x=-80, y=220)

button_2 = Button(text="Reset", width=10, highlightthickness=0, command=reset_timer)
button_2.grid(column=3, row=3)
button_2.place(x=200, y=220)

check_marks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)
check_marks.place(x=60, y=270)

window.mainloop()
