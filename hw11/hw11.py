class Adventurer:
#==========================================
# Purpose: To initialize the instance variables of the class
# Input Parameter(s):self which is a pointer, and line which is a string that represents the information of the employee
# Return Value(s): none
#==========================================
    def __init__(self, name, level, strength, speed, power):
        self.name=name
        self.level=level
        self.strength=strength
        self.speed=speed
        self.power=power
        self.HP=level*6
        self.hidden=False
    def __repr__(self):
        return self.name+' ' + '- ' + 'HP: ' + str(self.HP)
    
#==========================================
# Purpose: make the adventurer object attack another adventurer object. 
# Input Parameter(s):self which is a pointer, target which represents the other adventurer object that the intial adventurer object is going to attack
# Return Value(s): none
#==========================================

    def attack(self,target):
        if target.hidden==True:
            print(self.name + ' '+ "can't see" + ' ' + target.name )
        else:
            damage=self.strength+4
            target.HP=target.HP-(damage)
            print(self.name+' attacks '+target.name+' for '+str(damage)+' damage')
    def __lt__(self,other):
        if self.HP<other.HP:
            return True
        else:
            return False
class Fighter(Adventurer):
    def __init__(self,name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP=level*12
#==========================================
# Purpose: make the adventurer object attack another adventurer object. 
# Input Parameter(s):self which is a pointer, target which represents the other adventurer object that the intial adventurer object is going to attack
# Return Value(s): none
#==========================================

    def attack(self,target):
        if target.hidden==True:
            print(self.name + ' '+ "can't see" + ' ' + target.name )
        else:
            damage=2*self.strength+6
            target.HP=target.HP-(damage)
            print(self.name+' attacks '+target.name+' for '+str(damage)+' damage')

            
class Thief(Adventurer):
    def __init__(self,name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP=level*8
        self.hidden=True
        
#==========================================
# Purpose: make the adventurer object attack another adventurer object.
# Input Parameter(s):self which is a pointer, target which represents the other adventurer object that the intial adventurer object is going to attack
# Return Value(s): none
#==========================================

    def attack(self,target):
        if self.hidden==False:
            Adventurer.attack(self,target)
        elif target.hidden==True and self.speed<target.speed:
            print(self.name + " can't see " + target.name)
        else:
            self.hidden=False
            target.hidden=False
            damage=(self.speed+self.level)*5
            target.HP=target.HP-(damage)
            print(self.name +" sneak attacks " + target.name+ " for "+ str(damage) + ' damage')

class Wizard(Adventurer):
    def __init__(self,name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left=power
        
#==========================================
# Purpose: make the adventurer object attack another adventurer object.
# Input Parameter(s):self which is a pointer, target which represents the other adventurer object that the intial adventurer object is going to attack
# Return Value(s): none
#==========================================

    def attack(self,target):
        if self.fireballs_left==0:
            Adventurer.attack(self,target)
        else:
            self.fireballs_left-=1
            target.hidden=False
            damage=self.level*3
            target.HP=target.HP-(damage)
            print(self.name + ' casts fireball on ' + target.name + ' for ' + str(damage) + ' damage')

#==========================================
# Purpose: To out two adventurer object in a duel against each other until one of them has won
# Input Parameter(s):adv1 and adv2 both of which are adventurer objects
# Return Value(s): return Tue if adv1 won or false is adv2 won or they both lost
#==========================================
            
def duel(adv1, adv2):

    if adv1.HP<=0 and adv2.HP>0:
        print(adv1)
        print(adv2)
        print(adv2.name + ' wins!')
        return False
    if adv2.HP<=0 and adv1.HP>0:
        print(adv1)
        print(adv2)
        print(adv1.name + ' wins!')
        return True
    if adv1.HP<=0 and adv2.HP<=0:
        print(adv1)
        print(adv2)
        print("Everyone loses!")
        return False
    else:
        print(adv1)
        print(adv2)
        adv1.attack(adv2)
        
        if adv2.HP>0:
            adv2.attack(adv1)
        return duel(adv1,adv2)
    
#==========================================
# Purpose: To creat a tournmanet in which multiple adventurer objects battle each other until one of them wins
# Input Parameter(s): a list of adventurer objects
# Return Value(s): none if the adventurer list is empty or return the first adventurer in the list if the adventurer list only has one adventurer onject remaining. return the winner adventurer
#==========================================
        
def tournament(adv_list):
    if adv_list==[]:
        return None
    if len(adv_list)==1:
        return adv_list[0]
    else:
        adv_list.sort()
        duel(adv_list[-2],adv_list[-1])
        if adv_list[-2].HP<=0:
            adv_list.remove(adv_list[-2])
            adv_list.sort()
            return tournament(adv_list)
        if adv_list[-1].HP<=0:
            adv_list.remove(adv_list[-1])
            adv_list.sort()
            return tournament(adv_list)
            

    
    
               
            
        
        
        
    
    
        
