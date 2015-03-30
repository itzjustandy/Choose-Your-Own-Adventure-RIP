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
    choice = simpledialog.askinteger("Rooftop",
                                     "You climb up and up the staircase, yet the stairs never seem to end.\n" +
                                     "After climbing the stairs for what seemed like an eternity, you finally\n" +
                                     "reach the rooftop. When you get there you scan the entirety of the area\n" +
                                     "only to once again conclude that you are surrounded by skyscrapers, all\n" +
                                     "at leas 20 stories tall. Taking a second glance around, you notice that on\n" +
                                     "each tower, there is a suspension bridge connecting one roof top\n" +
                                     "another. This intrigues, yet scares you at the same time. Why are\n" +
                                     "there suspension bridges? Why is there skyscrapers? How on did\n" + 
                                     "I end up here? Question after question begin to flood your already clouded\n" +
                                     "mind, until you ask yourself a question that makes you stop in your\n" +
                                     "tracks and think. What should you do now?\n\n\" +
                                     "Should you:\n 1: Cross the suspension bridge. \n 2: Stay where you are\n" +
                                     "and wait for help to arrive.")
                                        
    if (choice == 1):
        messagebox.showinfo("Crossing",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "The idea of having to cross the suspension bridge frightens you.\n" +
                            "There is no way you are crossing on to the next building. You sit down\n" +
                            "in the middle of the rooftop, taking shelter underneath one of the\n" +
                            "structures on the roof. You sit there with the hope that maybe somebody,\n" +
                            "anybody will come out to rescue you. Seconds turn to minutes, and minutes\n" +
                            "into hours. Boredom begins to consume you and you soon become sleepy. Deciding\n" +
                            "that a quick nap wouldn't hurt, you close your eyes and begin to drift away.\n" +
                            "However, this is your mistake. The moment you fall asleep, he approaches\n"+
                            "you from behind, knife in hand, striking you straight through the heart.\n" +
                            "Who is he? Well that's for you to never find out, as you descend into an\n" +
                            "eternal slumber sent there by the man himself. THE END")
    else:
        choice1()

################ Student B Functions #####################
def choice2():
    choice = simpledialog.askinteger("Dead End",
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
