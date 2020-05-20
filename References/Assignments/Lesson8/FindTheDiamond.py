#Your assignment is to build a Find The Diamond game, where the 
# diamond is randomly hidden in one of ten boxes and the objective 
# of the game is to find the diamond by clicking on the box where 
# you think it is hidden. You have three guesses to find the diamond.

from tkinter import *
import tkinter.messagebox as msgBox
import random as rnd
import sys
window=Tk()
window.title("Find The Diamond")
window.geometry("1230x490")
window.configure(bg="plum")
guesses = 0
def random():
    global rndBox
    rndBox = rnd.randint(1, 11)
def guess():
    global guesses
    if guesses != 3:
        guesses+=1
    elif guesses == 3:
        guesses = 1

#Create the widgets
btn1=Button(window, width=10, height=3)
btn2=Button(window, width=10, height=3)
btn3=Button(window, width=10, height=3)
btn4=Button(window, width=10, height=3)
btn5=Button(window, width=10, height=3)
btn6=Button(window, width=10, height=3)
btn7=Button(window, width=10, height=3)
btn8=Button(window, width=10, height=3)
btn9=Button(window, width=10, height=3)
btn10=Button(window, width=10, height=3)
htd=Button(window, width=10, height=3)
label1=Label(window, width=2, bg="plum", justify=LEFT)

#Specify the gird layout
btn1.grid(row=0, column=0, padx=25, pady=30)
btn2.grid(row=0, column=1, padx=20, pady=30)
btn3.grid(row=0, column=2, padx=20, pady=30)
btn4.grid(row=0, column=3, padx=20, pady=30)
btn5.grid(row=0, column=4, padx=20, pady=30)
btn6.grid(row=1, column=0, padx=10, pady=10)
btn7.grid(row=1, column=1, padx=10, pady=10)
btn8.grid(row=1, column=2, padx=10, pady=10)
btn9.grid(row=1, column=3, padx=10, pady=10)
btn10.grid(row=1, column=4, padx=10, pady=10)
htd.grid(row=2, column=0, columnspan=2, sticky=W, padx=30, pady=20)
label1.grid(row=2, column=2, columnspan=3, sticky=W, padx=30, pady=10)

#Configure the buttons
btn1.configure(text="1", bg="yellow", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn2.configure(text="2", bg="blue", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn3.configure(text="3", bg="red", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn4.configure(text="4", bg="green", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn5.configure(text="5", bg="purple", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn6.configure(text="6", bg="brown", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn7.configure(text="7", bg="pink", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn8.configure(text="8", bg="dark blue", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn9.configure(text="9", bg="dark red", fg="white", padx=55, pady=35, border=3, state=DISABLED)
btn10.configure(text="10", bg="orange", fg="white", padx=55, pady=35, border=3, state=DISABLED)
htd.configure(text="Hide The Diamond", bg="dark green", fg="white", padx=75, pady=35, border=3, state=NORMAL)
label1.configure(text="Click the Hide Diamond button to start the game. \nThen, click on the box where you think the diamond is \nhidden. you have three guesses to find it.", bg="plum", fg="black", padx=200, pady=35)

def handler1():
    checkGuess(1)
def handler2():
    checkGuess(2)
def handler3():
    checkGuess(3)
def handler4():
    checkGuess(4)
def handler5():
    checkGuess(5)
def handler6():
    checkGuess(6)
def handler7():
    checkGuess(7)
def handler8():
    checkGuess(8)
def handler9():
    checkGuess(9)
def handler10():
    checkGuess(10)

def diamond():
    btn1.configure(state=NORMAL, command=handler1)
    btn2.configure(state=NORMAL, command=handler2)
    btn3.configure(state=NORMAL, command=handler3)
    btn4.configure(state=NORMAL, command=handler4)
    btn5.configure(state=NORMAL, command=handler5)
    btn6.configure(state=NORMAL, command=handler6)
    btn7.configure(state=NORMAL, command=handler7)
    btn8.configure(state=NORMAL, command=handler8)
    btn9.configure(state=NORMAL, command=handler9)
    btn10.configure(state=NORMAL, command=handler10)
    htd.configure(state=DISABLED)
    random()
    
def checkGuess(self):
    if self==rndBox:
        msgBox.showinfo("Find The Diamond", "Congratulations, you won!")
        msgBox.askquestion("Question", "Do you want to play again?")
        if YES:
            starter()
        else:
            GameExit()
    else:
        guess()
        msgBox.showinfo("Alert", "Sorry, guess was wrong!")
        if guesses==3:
            msgBox.showinfo("Alert", "You are out of Guesses! \n The Diamond was hidden in box %d" % rndBox)
            msgBox.askquestion("Question", "Do you want to play again?")
            if YES:
                starter()
            else:
                GameExit()
        else:
            msgBox.showinfo("Alert", "Your gusses are %d" % guesses)
            diamond()
def GameExit():
    # code to exit
    window = Tk()
    window.destroy
    
def starter():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)
    btn10.configure(state=DISABLED)
    htd.configure(state=NORMAL)

htd.configure(command=diamond)
window.mainloop()