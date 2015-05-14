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

################ Stephanies Functions #####################
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
        crossing()

    elif (choice == 2):
        messagebox.showinfo("The End", "The idea of having to cross the suspension bridge frightens you.\n" +
                            "There is no way you are crossing on to the next building. You sit down\n" +
                            "in the middle of the rooftop, taking shelter underneath one of the\n" +
                            "structures on the roof. You sit there with the hope that maybe somebody,\n" +
                            "anybody will come out to rescue you. Seconds turn to minutes, and minutes\n" +
                            "into hours. Boredom begins to consume you and you soon become sleepy. Deciding\n" +
                            "that a quick nap wouldn't hurt, you close your eyes and begin to drift away.\n" +
                            "However, this is your mistake. The moment you fall asleep, he approaches\n"+
                            "you from behind, knife in hand, striking you straight through the heart.\n" +
                            "Who is he? Well that's for you to never find out, as you descend into an\n" +
                            "eternal slumber sent there by the strange man himself. THE END")
    else:
        exit

def downstairs():
     choice = simpledialog.askinteger("No Exit", "You head down the set of stairs hoping to find an exit. The building\n" +
                                      "was absolutely silent, the only thing you could hear was the pitter patter of your own\n" +
                                      "feet, and you were starting to freak out. You wanted to get out of there as soon as\n" +
                                      "you could. Once you reached the bottom of the stairs however, you knew that wasn't going to\n" +
                                      "be possible. Right across from you was your only way out of this building, bounded and boarded up.\n" +
                                      "You pulled and pried, hoping you could remove enough away from the door so you could leave, but to\n" +
                                      "your disappointment, nothing would budge. Fear and confusion slowly starting to bubble up inside\n" +
                                      "of you, you made your way back up the stairs so you could travel up the second set of stairs in the\n" +
                                      "first room you were in.\n\n" +
                                      "Press 1 to continue.")
     if (choice == 1):
         upstairs()
        
  
                           
def crossing():
    choice = simpledialog.askinteger("Crossing", "Once you crossed the bridge and set foot upon the new building, you are\n" +
                            "met with a sight you did not expect. Opposite from where you were, stood what appeared\n" +
                            "to be a man. Excitement had begun to bubble inside of you. You had found another person in\n" +
                            "this odd yet frightening place, and perhaps even somehow go home, or at the very least be willing\n" +
                            "to travel alongside you. Before you could him, what you saw next made a cold sweat roll down your\n" +
                            "back. Covering his entire face, sat a mask, forever stuck in a smile, and in his hands was a standard\n" +
                            "cooking knife, something you can see in anyone’s kitchen. But despite the distance that was between the\n" +
                            "two of you, undeniably, there was blood on that knife, and that just did not sit with you too well.\n" +
                            "Before he could see you, you ducked behind a concrete structure that sat on the rooftop. Your heart rate\n" +
                            "sped up, your palms now sticky with sweat. You had to make a choice and you knew you had to do it\n" +
                            "quickly. There was a chance the blood was just from some animal he recently cooked and the mask maybe\n" +
                            "just a strange sort of fashion statement he was trying to make. Of course the chances of that being it\n" +
                            "were unfortunately low. So now you had two options to choose from.\n\n" +
                            "Should you:\n 1: Confront the masked man. \n 2: Hide out and wait.")
    if (choice == 1):
        confront()
                                     
    elif (choice == 2):
        hide()                             
       
    else:
        exit
                                     
def hide():
    choice = simpledialog.askinteger("Hiding", "His movements, his looks, everything about this masked man made a chill run down your spine.\n" +
                                     "You didn't want to take a chance with confronting him right away, so you decided to hide behind a structure\n" +
                                     "on the roof, to hide yourself from this man. You knew you couldn't stay there hiding forever, you still had to\n" +
                                     "cross the suspension bridge to make it to the next building. Yet, at the same time, you didn't want to make yourself\n" +
                                     "known to him just yet.\n\n" +
                                     "Should you:\n 1: Stay hidden and observe him a bit more. \n 2: Take a chance and try to cross the bridge.")
    if (choice == 1):
        messagebox.showinfo("The End", "Perhaps if you stay hidden and observed him, you could find out if he really was dangerous or not. After all, just\n" +
                            "because someone looks hostile doesn't mean they actually are, right? Telling yourself that, you crouch down even lower to the ground\n" +
                            "and position yourself so that you could still see the masked man. As you lay low, watching the masked one closely, you didn't notice\n" +
                            "as another figure approached you from behind. Before you could turn around, you felt something stab into your back, but oddly enough \n" +
                            "you did not feel any pain. All you felt was numbness swallow your entire body, as darkness washed over you. Before your eyes shut\n" +
                            "completely, you caught a glimpse of the one that ended your life. And the last thing you would ever see would be that wretched mask. THE END")

    elif (choice == 2):
        bridge()

def confront():
    choice = simpledialog.askinteger("Confrontation", "You tried to think on the optimistic side of things and started to think of the various\n" +
                                     "reasons behind all of the suspicious qualities this masked man had. The mask was probably a new trend you never caught\n" +
                                     "on to, his wobbling was because he was tired, and the blood on that knife was probably from self-defense. As you got up\n" +
                                     "from where you sat staying hidden, you kept repeating those thoughts in your head to alleviate your growing\n" +
                                     "nerves the closer you got to him. You were about 10 feet away from him , yet he still didn't seem to notice you\n" +
                                     "standing right behind him. You called out to him successfully gaining his attention, but before you could even open\n" +
                                     "your mouth to speak once again, he launched at you, knife in hand, ready to end your life. Adrenaline pumps through\n" +
                                     "your veins and your body goes into fight-or-flight mode. The only thought in your head is that this man is\n" +
                                     "dangerous and you need to do something NOW. You glance towards the suspension bridge just a few feet away from you, then\n" +
                                     "back to the man chasing after you, ready to kill you. You needed to make a decision soon.\n\n" +
                                     "Should you:\n 1: Make a dash to the bridge. \n 2: Fight back against the masked one.")
    if (choice == 1):
        bridge()
    elif (choice == 2):
        messagebox.showinfo("The End", "With all of this adrenaline pumping through you, you felt like you could do anything, so you\n" +
                            "decided to take a risk and fight against the masked one. Bad idea. You quickly began to tire out. Your\n" +
                            "legs screamed in protest and your breathing was heavily labored. All in all, your body was in a terrible\n" +
                            "state. To make matters worse, the masked figure looked completely fine. No matter how you looked at it, the\n" +
                            "masked man had the advantage here. I mean, after all, not only was he in better shape but he also had a knife.\n" +
                            "Just as you were about to take another step, you miscalculated when to put your foot down, and ended up falling\n" +
                            "to the ground. Wasting not even a second, the masked man took the opportunity to drive his knife through your heart.\n" +
                            "Your last thought before you died, was that you really should have worked out more. THE END")
        
def bridge():
    choice = simpledialog.askinteger("The Bridge", "You didn't want to take any chances with this masked man. He was dangerous and you could tell.\n" +
                                     "Making up your mind, you made a dash to the bridge. Halfway there, the man noticed you running and started to make\n" +
                                     "chase, but you paid no mind to that and focused on making it across that bridge safely. You set foot on the bridge\n" +
                                     "and it immediately began wobbling dangerously back and forth. You looked down and you could see the street, hundereds\n" +
                                     "of feet below. You were terrified. You didn't want to end up falling to your death. The sound of footsteps nearing you\n" +
                                     "made you snap out of your fear ridden trance and you quickly, but carefully began making your way across the suspension bridge.\n" +
                                     "When you finally step foot onto the new building, you nearly kissed the rooftop in pure joy, but that was when you remembered\n" +
                                     "about the man who was supposed to be chasing after you. You quickly turned only to end up confused. There, standing on the\n" +
                                     "building you were previously on, was the masked man. He had not bother to make even an attempt to cross the bridge, instead\n" +
                                     "choosing to stand at its entrance instead. After staring at you for several moments, he turned around and left. While you\n" +
                                     "were very confused by the masked ones actions, you couldn't help but let out a cheer full of relief and joy. You had survived\n" +
                                     "an attack from a strange man wearing a mask trying to take you down with a kitchen knife. Not just anyone could to say that.\n" +
                                     "After you came down from your little high of joy, you took a look around the roof. It looked just like the last one and seem to\n" +
                                     "be void of any people. Letting out a thankful sigh, you look towards the door on the roof and the suspension bridge connecting\n" +
                                     "to the next building.\n\n" +
                                     "Should you:\n 1: Go inside and explore this building. \n 2: Move on to the next building.")
    if (choice == 1):
        explore()

    elif (choice == 2):
        move()

def explore():
    choice = simpledialog.askinteger("Then There Were Four", "You explore the inside of the building and find 3 people who have had the\n" +
                                     "same experience with the masked figures as you had. They begin to tell you more about this world and\n" +
                                     "offer you to travel with them.\n\n" +
                                     "Should you:\n 1:Team up with them. \n 2: Don't team up.")
    if (choice == 1):
        team()
        
    elif (choice == 2):
        messagebox.showinfo("The End", "Despite how much information they gave you, you don't fully trust them so you decide to keep going on\n" +
                            "your own. You start walking but they still insist you stay. They don't want another enemy to deal with. You continue\n" +
                            "arguing to the point it gets physical. Forgetting your location all of you get into a scuffle, causing you all to fall of\n" +
                            "the building, leading to your multiple deaths.")

def team():
    choice = simpledialog.askinteger("A New Team", "You decide to team up with them since they seem to know so much about this world. They then tell\n" +
                                     "you the one way to leave this world. They hand you a flier giving details of a helicopter that leaves everyday that\n" +
                                     "will take you back home. One of the team members come back only to be controlled by a mask.\n\n" +
                                     "Should you: \n 1:Kill them. \n 2: Don't kill them.")
    if (choice == 1):
        messagebox.showinfo("The End", "The other two hesitate not wanting to kill their friend, so you decide that you have to do it instead.\n" +
                            "Instead of receiving a 'thank you for saving our lives!' you get an angry knife to the heart for killing their friend.")
    elif (choice == 2):
        messagebox.showinfo("The End", "You don't have the heart to kill them. They were such a kind person to you as well as a friend to the others.\n" +
                            "Your hesistation along with the others gets everyone killed.")

                    

    


def move():
    choice = simpledialog.askinteger("The Garden", "As you were crossing the next bridge, you looked ahead to the next building and saw something green sitting on top\n" +
                                     "of the roof. Curious, you tried to make haste and cross the bridge as fast as you could. What you saw was certainly a surprise. There, right\n" +
                                     "front of you, was a beautiful, well kept garden, with a functioning fountain sitting in the middle of it all. You did a quick glance\n" +
                                     "around to make sure no one else was there to try and kill you. With the coast clear, you made your way around the garden. The flowers\n" +
                                     "smelled wonderfully sweet, and the entire garden was pleasantly warm. You walked around the fountain spouting out water when your foot\n" +
                                     "knocked against something. You looked to see a wooden crate. You looked around its side to see the word 'SUPPLIES' written on a sign.\n" +
                                     "You crouched down and lifted the lid to see a variety of non-perishable food and clean drinking water. You were absolutely estatic. Your\n" +
                                     "stomach had been feeling a bit empty, and your throat very dry. As you reached for one of the bottles of water, you paused. What if this\n" +
                                     "was a trap. What if everything was poisoned? You were able to set that idea aside quickly as you realized everything was perfectly sealed.\n" +
                                     "You ate only one bag of the preserved foods you had and drank only one bottle of water. You didn't know when the next time you would find\n" +
                                     "another crate full of food and drinks, so you needed to save as much as you could. After finishing up your food and water, you started\n" +
                                     "to feel a bit sleepy. After all, running for your life across a bridge that was at least 20 stories high could really tire a person\n" +
                                     "out. You laid down on the grass letting your body rest for a bit. The longer you laid down, the more you didn't want to get up. The grass\n" +
                                     "felt amazingly soft against your back and you wanted to take a nap right there and then so badly. At the same time, you didn't know how\n" +
                                     "how safe that was. Who knows how many other masked people were running around trying to find and kill you.\n\n" +
                                     "Should you:\n 1: Stay and take a quick nap. \n 2: Keep on moving.")
    if (choice == 1):
        messagebox.showinfo("The End", "You decide that you deserve a nice long nap after everything you had to go\n" +
                            "through. With your mind made up, you snuggle further into the grass and make yourself a\n" +
                            "bit more comfortable. Within seconds, you fall into a deep and peaceful sleep. This nap\n" +
                            "is just what you need to cure your aching, tired body. However, taking that nap was your\n" +
                            "mistake, for as you lay on the ground peacefully snoring away, a knife plunged straight\n" +
                            "into your heart, turning your quick little catnap, into an eternal slumber. THE END")
    elif (choice == 2):
            ongoing()

def ongoing():
    choice = simpledialog.askinteger("Take It Or Leave It", "You decide against the nap, it's safer that way. Your energy\n" +
                                     "was already replenished enough from just lying down, so you get up, and keep moving.\n" +
                                     "You cross building after building, never encountering anything new or different. While\n" +
                                     "you are grateful you didn't run into anymore knife wielding maniacs wearing masks, you can't\n" +
                                     "help but find yourself becoming exceedingly bored. You've been walking for hours and all\n" +
                                     "you want to do is go home. The universe finally taking pity on you, answers your prayers,\n" +
                                     "in an unlikely form. You stepped off the bridge to a new rooftop, something you've been\n" +
                                     "doing repeatedly since earlier. As you take in the sight before you, however, instead of\n" +
                                     "looking across an empty rooftop, you see a small table standing in the middle,\n" +
                                     "only tall enough to reach your hips. You cautiously make your way to the table. Who knows\n" +
                                     "what's on it. As you get closer you realize what it is. Sitting atop the table, was a gun\n" +
                                     "lying next to a magazine full of bullets. It looked almost as if it was waiting there\n" +
                                     "for you to pick up and take with you. You've never held a gun before, let alone shoot one,\n" +
                                     "but the thought of the masked one made you think. What if you had a run in with him again?\n" +
                                     "Or worse, what if there were more? Sure, you hadn't seen anymore masked figures, but you\n" +
                                     "could never be too sure.\n\n" +
                                     "Should you:\n 1: Take it. \n 2: Leave it.")
    if (choice == 1):
        takeit()

    elif (choice == 2):
        leaveit()

def takeit():
    choice = simpledialog.askinteger("A Second Encounter", "You decide it's best to take the gun. After all, it's better to be safe\n" +
                                     "than sorry, right? With the fully loaded gun in your posession, you make your way to the next\n" +
                                     "building. You couldn't have gotten that gun at a better time, because as soon as you set foot on\n" +
                                     "the roof, you are a immediately attacked by a masked figure. You feel your stomach drop as you look\n" +
                                     "at the person standing in front of you. Instead of the man who attacked you last time, it was a female\n" +
                                     "holding an axe, at the ready to take care of you. If someone new was attacking you, then that could only\n" +
                                     "mean one thing; there is more than one of the masked men. You quickly throw those thoughts aside as you\n" +
                                     "prepare to defend yourself. The woman doesn't hesitate to swing her axe at you, and you don't hesitate to\n" +
                                     "run away from this deranged woman. You would have attempted to dodge and fight her head on, but we all know\n" +
                                     "that you are not in good enough shape for that. So instead, you choose to run. As you are running, that's\n" +
                                     "when you remember you have something to fight back with as well; you have a gun. You pull it out, and start\n" +
                                     "to fiddle with the safety locks, trying to turn them off, but of course you have no idea what to do never using a gun\n" +
                                     "before. Finally, you get the guns safety unlocked and put enough distance between you and the masked one to get ready\n" +
                                     "and shoot her. As you take aim, that's when you start to think. Where should you shoot her? Should you aim for\n" +
                                     "her head? Her heart? You've never killed anyone before and you don't really feel like starting now. Maybe\n" +
                                     "if you shoot her leg it'll be enough to slow her done and give you a good amount of time to run away.\n\n" +
                                     "Should you:\n 1: Shoot her heart. \n 2: Shoot her leg")
    if (choice == 1):
        heart()

    elif (choice == 2):
        messagebox.showinfo("The End", "You don't think you could live with the idea of taking someone else's life, so you shoot\n" +
                            "the masked woman in the leg instead. Surprisingly, you get her right in the thigh. You were too\n" +
                            "busy mentally celebrating the fact that you were actually able to do something right in a fight, you\n" +
                            "didn't notice how she barely faltered from the gun wound. It slowed her down, for maybe a second, before\n" +
                            "she took off, running after you, axe in hand. You realize that the gun had no effect on her too\n" +
                            "late, because before you can even react and ready your gun once again, the last thing you saw was the red\n" +
                            "blade of the axe falling down towards you. Then everything went black. THE END")


def leaveit():
    choice = simpledialog.askinteger("The Jump", "Well that was a terrible idea. You really should have taken that gun with you.\n" +
                                     "It seems that the universe loves playing cruel jokes on you, because as soon as you step onto\n" +
                                     "the new building, you are immediately attacked by a masked figure. You feel your stomach sink as\n" +
                                     "you notice that this isn't the same man who attacked you earlier. The mask is the same, but the person\n" +
                                     "is entirely new. He's taller and lankier than the last one, and this time he holds only a metal baseball\n" +
                                     "bat. This is bad; if you ran into two crazy, mask-wearing, weapon wielding maniacs, who knows how many others\n" +
                                     "are out there. As you keep on running, you slowly find out that the masked woman is driving you towards the\n" +
                                     "edge of the building. You think that she is trying to make you jump off the building and end your own life.\n" +
                                     "Desperate for a way out, you contemplate whether or not you should pretend to jump. If you do that, she might just\n" +
                                     "leave you alone. On the other hand, she might not be trying to get you to jump, she's simply just chasing you around.\n\n" +
                                     "Should you:\n 1: Pretend to jump. \n 2: Continue dodging.")
    if (choice == 1):
        pretend()

    elif (choice == 2):
        messagebox.showinfo("The End", "It's no use, you eventually begin to tire out while the masked figure doesn't even look\n" +
                            "out of breath. You are killed")
def pretend():
    choice = simpledialog.askinteger("The Jump", "Right before you jump off the ledge, you surprise the figure and attack them\n" +
                                     "instead, Using their own knife, you stab them in the heart.\n\n" +
                                     "Should you:\n 1: Look behind their mask. \n 2: Don't look behind the mask.")
    if (choice == 1)
        messagebox.shwoinfo("The End", "Big mistake. As soon as you look at the back of the mask your head starts reeling\n" +
                            "and you begin to lose control of yourself. Your mind, your body, your entire being now belongs\n" +
                            "to the mask. You are one of them.")
    elif (choice == 2):
        dontlook()

def heart():
    choice = simpledialog.askinteger("The Mask", "Kill or be killed, right? After you shoot them dead you begin to\n" +
                                     "question what is underneath the mask and take it off the person. You take it off \n" +
                                     "and find nothing special.\n\n"+
                                     "Should you:\n 1: Look behind the mask. \n 2: Don't look behind the mask.")
    if (choice == 1):
        messagebox.showinfo("The End", "Big mistake. As soon as you look at the back of the mask your head starts reeling\n" +
                            "and you begin to lose control of yourself. Your mind, your body, your entire being now belongs\n" +
                            "to the mask. You are one of them.")

    elif (choice == 2):
        dontlook()


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

################ Main #####################
intro()

root.destroy()
