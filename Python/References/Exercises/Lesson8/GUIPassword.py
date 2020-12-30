from tkinter import *
import tkinter.messagebox as msgBox
window=Tk()
window.geometry("500x100")
window.title("Please Enter Your Password & Click CHECK...")
window.configure(bg = "plum")

frame = Frame(window)
frame.configure(bg = "plum")
input = Entry(frame, show = "*")

def showInfo():
    msgBox.showinfo("Password check...", "Your password is " + input.get() + ".")

enterButton = Button(frame, text="CHECK", padx = "10", pady = "10", fg="black", bg = "dark blue", command=showInfo)
enterButton.pack(side=RIGHT, padx=10, pady=10)
input.pack(side=LEFT)
frame.pack(padx=20, pady=20)

window.mainloop()