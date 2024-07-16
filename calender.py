from tkinter import *
import calendar


def make_cal():
    scr2 = Tk()
    scr2.title("CALENDAR")
    scr2.configure(background="lightblue")
    scr2.geometry("800x800")
    fetch_year = int(year_input.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(scr2, text=cal_content, font="times", fg="black", bg="gray")
    cal_year.pack(side=TOP)

    scr2.mainloop()







scr = Tk()
scr.geometry("500x500")
scr.title("Calender")
scr.configure(background="gray")

title = Label(scr, text="Calender", font=("times", 70), fg="black", bg="lightgreen")
title.pack(side=TOP)

year = Label(scr, text="What year?", font=("times", 15), fg="blue", bg="pink").place_configure(x=190,y=200)

year_input = Entry(scr, width=20).place(x=190, y=230)
#get_year = int(year_input.get())


show_calender = Button(scr, text="show calender", command=make_cal, width=40, bg="green", fg="red").place(x=120,y=420)
exit = Button(scr, text="Exit", bg="red", fg="black", command=exit)
exit.pack(side=BOTTOM)




scr.mainloop()