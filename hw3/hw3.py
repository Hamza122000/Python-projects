#Problem 1:
#==========================================
# Purpose: (The function prints the sound the dog makes based on the dogs weight?)
# Input Parameter(s): (1 input parameter which is weight that represents the dogs weight)
# Return Value(s): (The function returns the sound the dog makes?)
#==========================================
def sound(weight):
    weight=int(weight+0.5)
    if weight<13:
        return'Yip'
    elif weight>=13 and weight<=30:
        return'Ruff'
    elif weight>=31 and weight<=70:
        return'Bark'
    else:
        return 'Boof'
#problem 2:
#==========================================
# Purpose: (The function chooses the user to choose between 3 options and if the user chooses an option besides those 3 it asks the user to choose again?)
# Input Parameter(s): (there are 3 input parameters the text of the game and the 3 options, option1, option2, and option3, text represents the story given and option1,option2,option3 represent the options the user can choose from)
# Return Value(s): (the option the user chose)
#==========================================

def choice(text, option1, option2, option3):
    print(text)
    print('1.', option1)
    print('2.', option2)
    print('3.', option3)
    i=0
    while i<1:
        x=input('Choose 1,2,or,3:')
        if x=='1':
            return x
            i=+1
        elif x=='2':
            return x
            i+=1
        elif x=='3':
            return x
            i+=1
        else:
            print('Invalid option')
 #problem 3:
#==========================================
# Purpose: (the function lets the user play a game where he is presented with multiple options that dictate how the game story will go?)
# Input Parameter(s): (no input variables)
# Return Value(s): (either boolean false or boolean true)
#==========================================
def adventure():
    state=1
    while state != 6:
        if state==1:
            x = choice("you are attempting to break into area 51 and get stopped by guards.",
           "fight the guards",
           "play dead",
           "Scream for help")
            if x=='1':
               print('wrong move, they just shoot you and kill you?')
               return False
            if x=='2':
                print('they though you were dead and left you alone')
                state += 1
            if x=='3':
                print('Aliens hear your scream instead of your comrades and show up at your location ')
                state +=2
        if state ==2:
            x1=choice("you are now wondering the facility after escaping the guards and you encounter an alien.",
           "Capture and Kidnap the Alien",
           "Try to Kill him",
           "run away")
            if x1=='1':
               print('Hurray you succeeded in capturing your first alien ')
               return True
            if x1=='2':
                print('Bad choice, you angered him and now he is trying to kill and eat you')
                state += 2
            if x1=='3':
                print('Also bad choice, He senses your fear and tries to chase you so he can eat you(they feed on fear)')
                state +=2
        if state ==3:
            x2=choice("Your scream for help garnerd alien attention. Now an alien showed up at your location,He kills the guards and now is looking at you.",
           "Try to fight him", "try to escape",
           "hide in secret valt 42. the most secure location in the facility that just happens to be next to you")
            if x2=='1':
               print('You lose and die')
               return False
            if x2=='2':
                print('He chases after you to eat you')
                state += 1
            if x2=='3':
                print('you are now in valt 42 safe from the alien')
                state +=2
        if state ==4:
            x3=choice("You are now running away from an alien when you reach a dead end",
                      "Use the secret weapon you acquired from lab 13 to seal the alien away and then kidnap him ","Hide in vault 42","Hide inside the trash can")
            if x3=='1':
               print('Hurray you captured your first alien')
               return True
            if x3=='2':
                print('You are now safe in vault 42')
                state += 1
            if x3=='3':
                print('he finds and eats you')
                return False
        if state ==5:
             x4=choice("You are now in vault 42 and stuck ",
           "leave the valt through the back exist and make your way outside area51",'go back outside and fight the alien',
           "use the teleportation device to leave the vault and go back home ")
             if x4=='1':
               print('Hurray you made it to safety')
               return True
             if x4=='2':
                print('you just die a horrible death')
                return False
             if x4=='3':
                print('Hurray you are back home, alive')
                return True
        
            
            
            
            
            
        
        


        
                
        
    
     
    

