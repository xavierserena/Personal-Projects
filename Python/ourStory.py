inLove = False
interested = False

def metJulia():
    global interested
    interested = True
    print("Introduction *nods and waves*")
    print("X: 'Awesome, she's studying mechanical engineering... and she's cute")
    print("J: 'This must be the guy with the funniest puns, can't wait to hear")
    print("some time later...")
    print("J: Hey look look look! These are the properties of a determinant")
    print("X: 'Wow, she's amazing")

def askOut():
    print("X: When does the new Spiderman movie come out?")
    print("J: I believe it already came out *verifies with phone*")
    print("   Yes, came out on June 28th in Japan at 11:59.99 pm")
    print("X: Do you have plans for tomorrow? Would you like to go see it?")
    print("J: Sure")
    print("X: *screaming with excitement inside*")
    return "success"

def preDate():
    inLove = True
    print("X: 'She's gorgeous, don't mess it up!'")
    print("   'We're both wearing shorts, it's meant to be")
    print("Movie")
    print(" Both share laughs, perspectives and critique movie and")
    print(" analyze the engineering of the robots and costume")
    print("Sushi at the park")
    print(" X calls J a coworker")
    print(" J:  'Hmmm'")
    print(" X:  'Shoot'")
    print("Fireworks are about to start")
    print(" J: *Staring at what's visible of the amazing firework show*")
    print(" X: *Staring at something more amazing*")

def hollywoodBowl():
    print("X learns about music from J")
    print("X and J follow the music playfully, each uncertain of the message")
    print(" or at least X is...")
    print("X and J seat closer and closer...")
    print("*Indiana Jones begins playing, instilling adventurous spirit*")
    print("J moves her hand over, X follows")
    print("X: 'Is this it? Can I hold her hand?'")
    print("   'This uncertainty feels greater than Heisenberg's")
    print("    *caresses J's finger*")
    print("J: *Holds X's hand*")
    print("Fireworks light up the sky as X and J's hearts fill with excitement")

def cadDate():
    print("X shares idea for picture frame with J")
    print("Engineer and diesigner J corrects on dimensions and designs")
    print("Synergy develops as they exchange ideas and take turns adding features")
    print("X hugs J as she CADs")
    print("Can't figure out how to split a freaking model. Looks at video 3 times")
    print("Both laugh over a happy mistake")
    print("Into the Spider Verse")
    print(" X and J hold each other closely, with arms wrapped around one another")
    print(" J's head on X's chest, hands touching")
    print(" Warmth, tranquility and bliss fill the room")
    print("The rest arrive")
    print(" X and J throw each other to the floor, laptops flies away")
    print(" Casually watching movie... phew!")

love = 0
smiles = 0
laughs = 0
juliaBeingRight = 0
xavierBeingRight = 0
juliaPuns = 0
xavierPuns = 0

metJulia()
if interested:
    if askOut() == "success":
        preDate()
    for days in range(20):
        love += 1
        smiles += 2
        laughs += 2
        juliaBeingRight += 200
        xavierBeingRight += 1
        juliaPuns += 1
        xavierPuns += 10
        if days == 13:
            hollywoodBowl()
        elif days == 14:
            cadDate()
        elif days == 19:
            print('Break')
            break
print("Still in love")


