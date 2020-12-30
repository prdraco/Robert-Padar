from tkinter import *
import tkinter.messagebox as msgBox
window=Tk()

#Create the Widgets
img=PhotoImage(file='Python.png')
imgLbl=Label(window, image=img, bg= "red")

Button1=Button(window, width=2)
Button2=Button(window, width=2)
Button3=Button(window, width=2)
Button4=Button(window, width=2)
Button5=Button(window, width=2)
Button6=Button(window, width=2)

# Specify the grid layout:
imgLbl.grid(row=0, column=0, rowspan=2, padx=30, pady=40)

Button1.grid(row=0, column=1, columnspan=6, padx=10, pady=30)
Button2.grid(row=0, column=7, columnspan=6, padx=10, pady=30)
Button3.grid(row=0, column=14, columnspan=6, padx=10, pady=30)
Button4.grid(row=1, column=1, columnspan=6, padx=10, pady=20)
Button5.grid(row=1, column=7, columnspan=6, padx=10, pady=20)
Button6.grid(row=1, column=14, columnspan=6, padx=10, pady=20)

def button1():
    msgBox.showinfo("Your choice...", "You selected Lesson 1")

def button2():
    msgBox.showinfo("Your choice...", "You selected Lesson 2")

def button3():
    msgBox.showinfo("Your choice...", "You selected Lesson 3")

def button4():
    msgBox.showinfo("Your choice...", "You selected Lesson 4")

def button5():
    msgBox.showinfo("Your choice...", "You selected Lesson 5")

def button6():
    msgBox.showinfo("Your choice...", "You selected Lesson 6")

# Static properties:
window.title("Gird Exercise")
window.geometry("700x250")
window.configure(bg="plum")
Button1.configure(text="Lesson 1", bg= "red", fg= "black", \
					padx=50, pady=20, border=3, command= button1)
Button2.configure(text="Lesson 2", bg= "yellow", fg="black", \
					padx=50, pady=20, border=3, command= button2)
Button3.configure(text="Lesson 3", bg= "blue", fg="black", \
					padx=50, pady=20, border=3, command= button3)
Button4.configure(text="Lesson 4", bg= "green", fg="black", \
					padx=50, pady=20, border=3, command= button4)
Button5.configure(text="Lesson 5", bg= "purple", fg="black", \
					padx=50, pady=20, border=3, command= button5)
Button6.configure(text="Lesson 6", bg= "light blue", fg="black", \
					padx=50, pady=20, border=3, command= button6)

window.mainloop()