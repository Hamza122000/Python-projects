



class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def get_real(self):
        return self.real
    def get_imag(self):
        return self.imag
    def set_real(self,new_real):
        self.real=new_real
        
    def set_imag(self,new_imag):
        self.imag=new_imag
    
    def __str__(self):
        return str(self.real)+ ' '+ '+'+ ' '+ str(self.imag)+'i'
    def __add__(self,other):
        a=self.real+other.real
        b=self.imag+other.imag
        return Complex(a,b)
    def __mul__(self,other):
        c=self.real*other.real-self.imag*other.imag
        d=self.imag*other.real+self.real*other.imag
        return Complex(c,d)
    def __eq__(self,other):
        if self.real==other.real and self.imag==other.imag:
            return True
        else:
            return False




    
class Employee:
#==========================================
# Purpose: To initialize the instance variables of the class
# Input Parameter(s):self which is a pointer, and line which is a string that represents the information of the employee
# Return Value(s): none
#==========================================
    def __init__(self,line):
        line=line.strip('\n')
        line=line.split(',')
        self.name=line[0]
        self.position=line[1]
        self.salary=float(line[2])
        self.seniority=float(line[3])
        self.value=float(line[4])
    def __str__(self):
        return self.name + ','+ ' '  +(self.position)
    def net_value(self):
        return self.value-self.salary
#==========================================
# Purpose: to take two different employess and compare their net_Values
# Input Parameter(s): self and other which represent the two different employees
# Return Value(s): Returns True is the net_value of the first employee is less, false otherwise
#==========================================
    def __lt__(self,other):
        a=self.net_value()
        b=other.net_value()
        if a<b:
            return True
        else:
            return False

        
class Branch:
#==========================================
# Purpose: To intialize the instance variables of the class
# Input Parameter(s): self which is the pointer and fname which is the name of the file
# Return Value(s): none
#==========================================
    def __init__(self,fname):
        
        fp=open(fname)
        line=fp.readlines()
        self.location=(line[0].split(',')[1])
        self.upkeep=float((line[1].split(',')[1]))
        self.team=[]
        for i in range(3,len(line)):
            self.team.append(Employee(line[i]))
    def __str__(self):
        s=''
        for i in self.team:
            s+=str(i)+'\n'
        return self.location+'\n'+s
    def profit(self):
        s=0
        for i in self.team:
            s+=i.net_value()
        return s-self.upkeep
    def __lt__(self,other):
        if self.profit()<other.profit():
            return True
        else:
            return False
        
    def cut(self,num):
        self.team.sort()
        for i in range(0,num):
            self.team.pop(0)

            
            
class Company:
    def __init__(self,name,branches):
        self.name=name
        self.branches=branches
    def __str__(self):
        line=''
        for i in self.branches:
            line=line+str(i)+'\n'
        return self.name + '\n'+'\n' + line
    def synergize(self):
        self.branches.sort()
        self.branches[0].cut(len(self.branches[0].team)//2)
        
        
        
    
        
        
        
        
    



        
        
        
