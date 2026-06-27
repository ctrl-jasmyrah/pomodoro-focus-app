from tkinter import *
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


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

# rep=1,3,5,6
work_sec = WORK_MIN * 60
# rep=2,4,6
short_break_sec = SHORT_BREAK_MIN * 60
# rep=8
long_break_sec = LONG_BREAK_MIN * 60
window.config(padx=100, pady=100, bg=YELLOW)
reps=1
timer= None
def reset_timer():
    global timer
    if timer:
        window.after_cancel(timer)
    times.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    times.grid(column=1, row=0)
    tick.config(text="",font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
    tick.grid(column=1, row=3)

    canvas.itemconfig(timer_text, text="00:00")
    canvas.grid(column=1, row=1)
    # global reps
    # reps=1


def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")



    if count>0:
        timer=window.after(1000, count_down, count-1)
    else:
        start_time()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
            tick.config(text=mark)



canvas=Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)



tick=Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

times=Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
times.grid(column=1, row=0)

tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(110,115, image=tomato_img)
timer_text=canvas.create_text(115,135, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

text="Timer"
fg=GREEN
def start_time():
    global reps
    global text
    global fg
    if reps==1 or reps==3 or reps==5 or reps==7:
        count_down(work_sec)
        reps+=1
        text="Work"
        fg=GREEN
    elif reps==2 or reps==4 or reps==6:
        count_down(short_break_sec)
        reps+=1
        text="Break"
        fg=PINK
    elif reps==8:
        count_down(long_break_sec)
        reps+=1
        fg=RED
        text="Break"
    times.config(text=f"{text}", font=(FONT_NAME, 30, "bold"), fg=fg, bg=YELLOW)
    times.grid(column=1, row=0)


start=Button(text="Start", highlightthickness=0, command=start_time)
start.grid(row=2, column=0)

reset=Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)




window.title("Pomodoro Technique")
window.mainloop()
