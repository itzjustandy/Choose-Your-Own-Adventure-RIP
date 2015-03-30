# Choose.py
# by Andy Nguyen and Stephanie Ignacio
# Description: choose your own adventure game
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    choice = simpledialog.askinteger("Awake", "You find yourself slowly being stirred awake.\n" +
                        "You open your eyes to find yourself lying on the ground of an unknown\n" + 
                        "room. Sitting up, you take a look around the room. From the ceiling\n" +
                        "down to the floor it is made entirely out of concrete and is empty,\n" +
                        "except for two sets of stairs and a window. Try and try as you might you\n" +
                        "you just can't seem to remember how exactly you ended up where you are.\n" +
                        "You push those thoughts aside and stand up, making your way to only\n" +
                        "window in the room. Looking out the window, your eyes widen as you see\n" +
                        "nothing but skyscrapers in the surrounding area. More confused than\n" +
                        "ever, you step away from the window and decide what you should do next.\n\n" +
                        "Should you:\n 1: Go upstairs. \n 2: Go downstairs.")
    if (choice == 1):
        upstairs()
    elif choice == 2:
        downstairs()
    else:
        intro()

################ Student A Functions #####################
def upstairs():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Student B Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Main #####################
intro()

root.destroy()
