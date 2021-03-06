#/bin/python3
import turtle
import tkinter as tk
from time import sleep
from sys import exit

isPog = "waiting"

while isPog == "waiting":
    question = tk.Tk()
    question.title("ADHP")
    question.config(bg="black")
    question.geometry("300x300")
    questionlbl = tk.Label(
        question,
        bg="black",
        fg="green",
        text="Is david the turtle pog?",
        font=("Courier", 15))

    def proceed():
        global isPog
        isPog = True
        question.destroy()

    def notpog():
        global isPog
        isPog = False
        exit()

    def pogYes():
        questionlbl.config(text=":)", font=("Courier", 50))
        answerYes.config(text="Proceed", command=proceed)
        answerNo.pack_forget()
        answerYes.pack_forget()
        answerYes.pack(side="bottom")

    def pogNo():
        questionlbl.config(text=">:(", font=("Courier", 50))
        answerNo.config(text="Exit", command=notpog)
        answerYes.pack_forget()
        answerNo.pack_forget()
        answerNo.pack(side="bottom")

    answerYes = tk.Button(question, text="Yes", command=pogYes)
    answerNo = tk.Button(question, text="No", command=pogNo)
    questionlbl.pack(side="top")
    answerYes.pack(side="left")
    answerNo.pack(side="right")
    question.mainloop()

if isPog:
    sleep(0.1)
elif isPog == False:
    exit()

numberofpog = 0
numberofpoggers = 0

root = tk.Tk()
root.configure(bg="black")
root.geometry("650x570")
root.title("Project Sigma")

frame = tk.Frame(root, bg="black")
frame.pack()

bottomframe = tk.Frame(root, bg="black")
bottomframe.pack(side="bottom")

labelone = tk.Label(
    frame,
    bg="black",
    fg="green",
    text=
    "Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later."
)
labelone.pack(side="top")
labelone.config(font=("Courier", 15))

labeltwo = tk.Label(
    bottomframe,
    bg="black",
    fg="green",
    text="Press the \"Programs\" button to open the program menu")
labeltwo.config(font=("Courier", 15))
labeltwo.pack(side="top")
labelthree = tk.Label(
    bottomframe,
    bg="black",
    fg="green",
    text="Poggers x" + str(numberofpoggers),
    font=("Courier", 15))


def pog():
    global numberofpog
    numberofpog += 1
    print("pog")
    labeltwo.config(text="Pog x" + str(numberofpog))


def poggers():
    global numberofpoggers
    numberofpoggers += 1
    print("poggers")
    labelthree.config(text="Poggers x" + str(numberofpoggers))


def justpog():
    buttonofpog.config(text="button of pog", command=pog)


def gers():
    buttonofpog.config(text="button of poggers", command=poggers)


buttonofpog = tk.Button(frame, text="button of pog", command=pog)
justpogbutton = tk.Button(frame, text="just pog", command=justpog)
gersbutton = tk.Button(frame, text="-gers", command=gers)

canvasboi = tk.Canvas(frame, bg="black", width=400, height=400, relief="flat")
screenboi = turtle.TurtleScreen(canvasboi)
screenboi.bgcolor("black")

david = turtle.RawTurtle(screenboi)


def pogprinter():
    trianglerun.pack_forget()
    dmsbutton.pack_forget()
    pogprinterbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Back", command=programsmenu)
    labelone.config(
        text=
        "press button to pog.\npress other buttons to change to poggers or back"
    )
    labeltwo.config(text="Pog x" + str(numberofpog))
    labelthree.pack(side="top")
    prgrmsbutton.pack(side="bottom")
    buttonofpog.pack(side="top")
    justpogbutton.pack(side="left")
    gersbutton.pack(side="right")


pogprinterbutton = tk.Button(
    bottomframe, text="PogPrinter", command=pogprinter)


def darkmodesquare():
    trianglerun.pack_forget()
    pogprinterbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(command=programsmenu, text="Back")
    prgrmsbutton.pack(side="bottom")
    dmsbutton.pack_forget()
    labelone.config(text="Here, have a square.")
    labeltwo.config(text="drawing...")
    david.color("white", "gray")
    david.pensize(10)
    canvasboi.pack(side="bottom")
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    labeltwo.config(text="like it? yeah you do.")


dmsbutton = tk.Button(
    bottomframe, text="Dark Mode Square", command=darkmodesquare)


def triangle():
    trianglestring = """    /\\
    /  \\
    /    \\
    /      \\
    /        \\
    /          \\
    /            \\
    /              \\
    /                \\
    /                  \\
    /                    \\
    /                      \\
    /________________________\\
    triangle go brr"""
    labelone.config(text=trianglestring)
    labeltwo.config(text="Press back to return to program menu")
    trianglerun.pack_forget()
    pogprinterbutton.pack_forget()
    dmsbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(command=programsmenu)
    prgrmsbutton.pack(side="bottom")


trianglerun = tk.Button(bottomframe, text="Triangle", command=triangle)


def programsmenu():
    buttonofpog.pack_forget()
    justpogbutton.pack_forget()
    gersbutton.pack_forget()
    labelthree.pack_forget()
    quitbtn.pack_forget()
    labelone.config(
        text=
        "Program List:\nTriangle: draws a triangle with ASCII\nDark Mode Square: draws a white square using turtle\nPogPrinter: prints your pogs into the console\n(will be removed when no console) and counts them\nPress Back to go to the main menu"
    )
    labeltwo.config(text="Run a program:")
    canvasboi.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Back", command=mainmenu)
    prgrmsbutton.pack(side="left")
    trianglerun.pack(side="right")
    dmsbutton.pack(side="bottom")
    pogprinterbutton.pack(side="bottom")
    david.clear()

quitbtn = tk.Button(bottomframe, text="Exit", command=exit)

def mainmenu():
    labelone.config(
        text=
        "Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later."
    )
    labeltwo.config(text="Press the \"Programs\" button to open the program menu")
    trianglerun.pack_forget()
    dmsbutton.pack_forget()
    pogprinterbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Programs", command=programsmenu)
    prgrmsbutton.pack(side="right")
    quitbtn.pack(side="left")


prgrmsbutton = tk.Button(bottomframe, text="Programs", command=programsmenu)

mainmenu()

root.mainloop()
