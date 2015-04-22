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

# Notes
"""
91 Col per line
"""
messagebox.showinfo("fake","11111111111111111111111111111111111111111111111111111111111fass")
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
                                     "tracks and think. What should you do now?\n\n" +
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

################ Andy's Functions #####################
def cut():
    messagebox.showinfo("Cut the Ropes", "How terrible of them to try and kill you." 
                        " Luckily you had a headstart, so after you cross the bridge you"
                        " cut the ropes leaving them on the other building.")
                        
    messagebox.showinfo("Cut the Ropes",
                        " It'll be awhile before they can find you now. Onward"
                        " you go, searching for your only way home. Time goes on"
                        " and you can't tell if it's been days or weeks since"
                        " you've been there.")

    messagebox.showinfo("Cut the Ropes",
                        " After a while you start to think that perhaps they had been lying."
                        " Maybe there was no helicopter."
                        " Maybe they were delusional. Maybe there wasn't a way to get home."
                        " After crossing to another"
                        " building you come across a masked figure, standing"
                        " there as if waiting for you.")

    messagebox.showinfo("Cut the Ropes",
                        " And right behind them lies the ever elusive helicopter,"
                        " ready to take you home."
                        " However, dread fills you instead. You were so"
                        " close to getting home if it weren't for them."
                        " They motion for you to jump off the building and get it over with.")
    

    
    choice = simpledialog.askinteger("Cut The Ropes", "What now?\n\n" +
                                     "1: Give up?\n" +
                                     "2: Fight for your chance to go home?")
    if (choice == 1):
        messagebox.showinfo("Give up", "You're absolutely exhausted. You've been walking"
                            " for who knows how long, and the food and wter you've had"
                            " has been limited. You kow you face no chance of winning a"
                            " fight against the masked. So slowly, you inch your way towards"
                            " the edge of the roof.")

        messagebox.showinfo("Give up",
                            " You take one last look at the helicopter and then to the"
                            " masked man. You can't tell if it's because you are going"
                            " delusional, but the masked man bows its head a bit, as if"
                            " showing disappointment in the decision you've made."
                            " And that is your last thought as you fall off the"
                            " building's edge, and plunge into the darkness.")

        messagebox.showinfo("Give up", "YOU ARE DEAD\n"
                            "You have chosen the easy way out.\n\n"
                            "THE END.")
        

    elif (choice == 2):
        messagebox.showinfo("Fight", " You've made it this far, there's no way you're"
                            " going to give up now. You brandish your weapon and get"
                            " into a fighting stance waiting for the masked one to make"
                            " a move. When he does however, it surprises you, for it"
                            " doesn't look like it intends to fight, but rather indicates"
                            " for you to go on the helicopter.")

        messagebox.showinfo("Fight",
                            " He looks oddly pleased and continues to gesture you towards"
                            " the aircraft. Cautiously you make your way to the helicopter."
                            " Even when you get on, he makes no indictive move to attack you."
                            " Once you're safely on a different masked man starts the"
                            " helicopter and into the air you go. You're on your way home."
                            " Relief and fatigue hit you all at once, and you fall into a"
                            " deep slumber.")

        messagebox.showinfo("Fight",
                            " When you awake you find yourself in an empty, unfamiliar room."
                            " But this time you know. You are nowhere unkown, you are"
                            " nowhere where ysomeone is trying to take your life. You look"
                            " out the window to see familiar surroundings and people are out"
                            " and about. You are home. You are safe.")

        
    else:
        cut()

cut()

################ Main #####################
intro()

root.destroy()
