#Haaris' code. After Lecture 2 practice
#30th Jan, 2019

'''
The Variables

pw = password
ent = whatever the user inputs as the password
com = whatever the user inputs as a command

x = random used to shut programme if too many attempts
confirmExit = used to confirm if the user wants to exit or not
key1 = used to confirm if the turtle should be run
proc = used to confirm if user wants to try dicks
can2 = used to confirm cancel in dick size
dabDeath = idk anymore
dabHP = ...
'''

#MUST COMMENT ON HOW EVERYTHING WORKS
#IMPROVE THIS PASSWORD LOCK... SO THAT HINT ONLY POPS UP WHEN NEEDED
#IMPROVE DICKS. CUT IT SHORT WITH YOUR NEW KNOWLEDGE OF 'FOR' COMMANDS

dabDeath = 0
dabHP = 4
x = 0
pw = "password"
ent = input("Enter the password: ")

while (ent != pw): 

    if (ent == "hint"):
        print("Password is password")
        print()

    else: # after 1 failed attempt, it reminds the user that they can get a hint
        print("Incorrect")
        x += 1
        if (x == 1):
            print()
            print("(For a hint, type 'hint')")
        print()

    if (x == 5): # shut down after 5 tries
        print()
        print("Too many false tries, terminating...")
        input()
        exit()

    ent = input("Enter your password: ")

if (ent == pw):
    print()
    print("--------------------")
    print()
    print("Correct, welcome to the Hub")
    print()

print("Now we can proceed. Type 'help' for a list of commands")
print()

while(True):
    com = input(">>> ")

    if (com == "help") or (com == "Help") or (com == "HELP"):
        print()
        print("These are some of the avalable commands;")
        print()
        print("- change password")
        print("- coin flip")
        #print("- dab")
        #print("- dicks")
        #print("- die")
        print("- erg")
        print("- exit")
        print("- hashim")
        print("- heal")
        print("- help")
        print("- mega coin flip")
        print("- notes")
        print("- pah")
        #print("- random") #HAS YET TO BE PROGRAMMED
        print("- turtle")
        print("- secret")
        print("- smiley")
        #print("- yes")
        print()

    elif (com == "hashim"):
        print()
        print("This is all my avalable info on Hashim;")
        print()
        print("Nickname: Hash")
        print("Category: Fooligan")
        print("Adopted?: Possibly")
        print()

    elif (com == "secret"):
        print()
        print("*****SECRET AND EXPERIMENTAL*****")
        print()
        print("These are some secret commands you can try. At your own risk, of course.")
        print()
        print("- dab")
        print("- die")
        print("- dicks")
        print("- yes")
        print()

    elif (com == "erg"):
        print()
        print("There's not much to this. This word was a random keyboard mash that I used as a placeholder while programming the 'help' command. Found it funny, so I let it live here. Forever.")
        print()

    elif (com == "pah"):
        print()
        print(":o")
        print()

    elif (com == "die"):
        print()
        print("no. you die")
        print()
        print("(Press enter to die)")
        input()
        exit()

    elif (com == "exit"):
        print()
        print("Are you sure?")

        confirmExit = input("Type 'y' to confirm: ")
        if (confirmExit == "y"):
            exit()
        else:
            print("Cancelled")
            print()

    elif (com == "turtle"):
        print()
        print("I'll import my turtle code soon... Maybe even multiple versions, such as 'turtle 1' and 'turtle 2'")
        print()

    elif (com == "change password"):
        print()
        print("...actually, I am unable to do this at the moment. I do not know how to get Python to permanantly store the new value")
        print()
        print("When I learn how to do that, then I'll be able to do cool things, like allow the user to set a custom welcome screen, change the background hub to their liking, etc.")
        #pw = input("enter new password: ")
        print()

    elif (com == "dicks"):
        print()
        print("dicks is dangerous... This is code I wrote that has too many bugs. Simple stuff, such as closing the window while a dick is being generated can easily crash this program")
        print()
        print("Are you certain you want to proceed?")
        
        proc = input("Type 'y' to confirm: ")
        if (proc == "y"):
            
            print()
            print("***BETA***")
            print()
            print("Choose your size")
            print()
            print("- small (50)")
            print("- medium (100)")
            print("- big (150)")
            print("- unreasonable (200)")
            print()
            print("- custom (?)")
            print()

            key1 = 0
            while (key1 == 0):
                dickSize = input("Size: ")

                if (dickSize == "small"):
                    y = 50
                    key1 = 1

                elif (dickSize == "medium"):
                    y = 100
                    key1 = 1

                elif (dickSize == "big"):
                    y = 150
                    key1 = 1

                elif (dickSize == "unreasonable"):
                    y = 200
                    key1 = 1

                elif (dickSize == "custom"):
                    y = float(input("Choose your value: "))
                    key1 = 1

                elif (dickSize == "cancel"):
                    print()
                    print("ok")
                    print()
                    key1 = 2

                else:
                    print()
                    print("You didn't pick. Cancel?")
                    can2 = input("Type 'y' to confirm: ")
                    if (can2 == "y"):
                        print("Cancelled")
                        key1 = 2
                    else:
                        print("Failed to confirm")
                    print()

            if (key1 == 1):
                import turtle

                x = 90 # angle for turtle to turn at

                #y = size of dick
                shape = "arrow" #input("Input the desired shape of your turtle: ") # asking user to choose shape of turtle
                bg = "black" #input("Input the desired colour of your background: ") # letting user choose background
                c = "white" #input("Input the desired colour of your square: ")# colour of square and turtle

                turtle.bgcolor(bg) # background colour
                turtle.color(c) # colour of turtle
                turtle.shape(shape) # the shape of the turtle

                turtle.forward(y)
                turtle.right(x)
                turtle.forward(y)
                turtle.right(x)
                turtle.forward(y)
                turtle.right(x)
                turtle.forward(y)

                turtle.left(x)
                turtle.forward(y)
                turtle.left(x)
                turtle.forward(y)
                turtle.left(x)
                turtle.forward(y)
                turtle.left(x)

                turtle.forward(y)
                turtle.left(x)
                turtle.forward(y / 2)
                turtle.right(x)

                turtle.forward(y * 2)
                turtle.right(x)
                turtle.forward(y)
                turtle.right(x)
                turtle.forward(y * 2)

                turtle.right(x * 2)
                turtle.forward(y * 2)
                turtle.right(x)
                turtle.forward(y / 4)

                turtle.left(x * 1.5)
                turtle.forward(y)
                turtle.left(x)
                turtle.forward(y)

                turtle.left(x * 1.5)
                turtle.forward(y /2 )

                turtle.right(x * 2)
                turtle.forward(y /2 )
                turtle.right(x * 1.5)
                turtle.forward(y)

                turtle.right(x * 1.5)
                turtle.forward(y/8)
                turtle.right(x * 2)
                turtle.forward(y/8)

        #jizz
        #also, repetition
                turtle.right(x / 2)
                turtle.forward(y / 8)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.right(x)
                turtle.forward(y / 4)
                turtle.left(x)
                turtle.forward(y / 4)

                turtle.done()

        else:
            print("Cancelled. Wise Choice")
            print()

    elif (com == "dab"):
        dabDeath += 1
        dabHP -= 1

        if (dabDeath < 3):
            print()
            print("no")
            print("HP now at ", dabHP, "hearts")
            print()
            
        if (dabDeath == 3):
            print()
            print("Write that one more time... I dare you")
            print()

        if (dabDeath >= 4):
            print("die")
            exit()

    elif (com == "heal"):
        print()
        print("HP fully restored")
        print()
        dabHP = 4
        dabDeath = 0

    elif (com == "coin flip"):
        print()
        import random

        wow = 0
        
        num = random.randint(1, 6000)

        if (num > 3000):
            print("Heads")
            
        elif (num < 3000):
            print("Tails")
            
        else:
            print("Landed on Edge")
            wow = 1

        if (wow >= 1):
            print()
            print("Hello. This message was set to display only if your coin landed on its edge. This was a 1 in 6000 chance")
            print()
            print("Congratulations. You've won at life")

        print()
        

    elif (com == "mega coin flip"):

        print()
        c = input("Press Enter to Flip a coin 100 times. Or type 'n' to cancel: ")
        print()

        if (c == "n"):
            print("Cancelled")
            print()

        else:

            import random

            x = 0
            h = 0
            wow = 0
            t = 0
            while (x < 100):
                num = random.randint(1, 6000)
                if (num > 3000):
                    print("Heads", end = " ")
                    h += 1
                elif (num < 3000):
                    print("Tails", end = " ")
                    t += 1
                else:
                    print("***Landed on Edge***", end = " ")
                    wow += 1
                x += 1

            print()
            print()
            print("Number of Heads: ", h)
            print("Number of Tails: ", t)

            if (wow >= 1):
                print("Number of Times Coin Landed on Edge: ", wow)
                print()
                print("This message was set to display only if your coin landed on its edge; a 1 in 6000 chance")
                print()
                print("Congratulations. You've won at life")

            print()

    elif (com == "yes") or (com == "YES"):
        print()
        print("What do you mean 'yes'? Write a command")
        print()

    elif (com == "smiley"):
        print()

        for i in range(20):
            for j in range (80):    
                
                if ((i in range (3, 7)) and (j in range (10, 21) or j in range (59, 70))): # to print the eyes
                    print(" ", end = "")

                elif ((i in range (10, 12)) and (j in range (22, 33) or j in range (47, 58))): # to print top part of the mouth
                    print(" ", end = "")

                elif ((i in range (12, 17)) and (j in range (22, 58))): # to print bottom part of the mouth
                    print(" ", end = "")
                    
                else:   #printing the normal lines
                    print("|", end = "")
                        
            print()

        print()

    elif (com == "notes"):
        print()
        print("2nd Feburary, 2018;")
        print()
        print("'smiley' was a tough one to program. I almost gave up halfway through. But somehow, I've done it, and I can now say that my understanding of the 'for' loop, along with how to use it, is at an acceptable level")
        print()
        print("Now it may soon be time to make a variable smiley. One where you can pick and choose how big you want the smile. Or perhaps you could choose a different face altogether")
        print()
    
    else:
        print("unrecognized command")
        print()

input() # No point having this here, as escaping while(True) is impossible
