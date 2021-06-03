from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bg="skyblue")
window.title("Exception Handling")
window.geometry("300x400")
window.resizable(0, 0)

amountlabel = Label(window, text="Please enter amount in your account:", bg="skyblue")
amountlabel.place(x=15, y=30)
amountfield = Entry(window)
amountfield.place(x=15, y=60)


def checkqualification():
    try:
        money = float(amountfield.get())
        if money < 3000:
            messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
            amountfield.delete(0, END)
        else:
            messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
            amountfield.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please put in an amount in numbers.")
        amountfield.delete(0, END)


enterbutton = Button(window, text="Check qualification", bg="#a4d1cc", command=checkqualification)
enterbutton.place(x=15, y=120)


def clearfunc():
    amountfield.delete(0, END)


clearbutton = Button(window, text="Clear", bg="#a4d1cc", command=clearfunc)
clearbutton.place(x=15, y=180)


def exitfunc():
    window.destroy()


exitbutton = Button(window, text="Exit", bg="#a4d1cc", command=exitfunc)
exitbutton.place(x=230, y=180)

window.mainloop()
