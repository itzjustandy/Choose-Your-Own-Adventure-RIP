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


################ Andy's Functions #####################
def look():
    messagebox.showinfo("Don't Look", "Just as you were about to look, a voice tells"
                        " you to stop and not to look at the back of the mask."
                        " Surprised, you find unmasked people holding weapons of a"
                        " variety standing behind you.")

    choice = simpledialog.askinteger("Don't Look", "Now what?\n\n" +
                                     "1: Run away?\n" +
                                     "2: Stay?")
    if (choice == 1):
        messagebox.showinfo("Run Away", "After the encounter you just had, you decide"
                            " not to risk it. You begin running away to the next building."
                            " As you're crossing the bridge, in your panic you begin to"
                            " trip and stumble. You lose your footing and descend down to"
                            " the ground hundreds of feet below you. No going home for you.")

        messagebox.showinfo("Run Away", "YOU ARE DEAD\n"
                            " Your idiocracy caused your death.\n\n"
                            "THE END.")

    elif (choice == 2):
        Stay()
    else:
        look()

def Stay():
    messagebox.showinfo("Stay", "You stay, curious to know what they have to say."
                            " They explain to you everything they know about the masked"
                            " people and the world that you're in, even how to escape it."
                            " On one of the buildings there is a helicopter that promises"
                            " to take you back home, however only one person can go each"
                            " day and each night. After every night, the helicopters"
                            " position changes.")

    choice = simpledialog.askinteger("Stay", "Should you...?\n\n" +
                                     "1: Team up?\n" +
                                     "2: Refuse?")
    if (choice == 1):
        TeamUp()
    elif (choice == 2):
        Refuse()
    else:
        Stay()

def TeamUp():
    messagebox.showinfo("Team up", "You team up with them. After all, there's"
                        " safety in numbers, right? You searching for the"
                        " helicopter, crossing building after building. Everyone"
                        " is desperate to go home. People are becoming grumpy and"
                        " angry. A fight erupts amongst you all. You've had it with"
                        " them and want to leave, but at the same time are afraid"
                        " to do so.")
    choice = simpledialog.askinteger("Team Up", "Will you...?\n\n" +
                                     "1: Stay?\n" +
                                     "2: Leave?")
    if (choice == 1):
        messagebox.showinfo("Stay", "You try to make it worth but the fights have"
                            " been getting worse and worse as time goes by."
                            " One fight gets bad enough that everyone is pushing"
                            " and shoving. One particular shove sends you spiraling"
                            " down to the ground, hundreds of feet below you. The last"
                            " thing you hear are you friends screaming for you."
                            " Then everything goes blank.")

        messagebox.showinfo("Stay", "YOU ARE DEAD\n"
                            " Your kindness ends your life.\n\n"
                            "THE END.")
    elif (choice == 2):
        messagebox.showinfo("Leave", "You don't want to be around when everything"
                            " really goes south, so when everyone is asleep you"
                            " gather up your stuff and leave. It's practically pitch"
                            " black outside and you don't want to risk giving your"
                            " position away to anyone by flashing a light. You"
                            " carelessly make the decision to cross a bridge"
                            " despite your loss of sight. Unsurprisingly, you end"
                            " up tripping and falling to your death.")

        messagebox.showinfo("Leave", "YOU ARE DEAD\n"
                            " You are indeed the epitome of stupidity.\n\n"
                            "THE END.")
    else:
        TeamUp()

def Refuse():
    messagebox.showinfo("Refuse", "You decide not to team up. You want to get home as"
                        " soon as you can and these people will just slow you down."
                        " You bid them goodbye and leave to search for the helicopter"
                        " yourself. However, the others seem to think differently."
                        " They demand you join. They feel safer this way."
                        " The more you refuse, the more intense the argument gets when"
                        " one of them suddenly attacks you.")

    choice = simpledialog.askinteger("Refuse", "Will you...?\n\n" +
                                     "1: Try to fight them all off?\n" +
                                     "2: Cross the bridge and cut the ropes?")

    if (choice == 1):
        messagebox.showinfo("Fight them all", "Well that was a huge mistake."
                            " They most definetly have the upper hand in this situation."
                            " They easily overpower and kill you."
                            " One less enemy for them to worry about now.")
    elif (choice == 2):
        cut()
    
    else:
        Refuse()

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
look()



root.destroy()
