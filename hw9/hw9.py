
#==========================================
# Purpose: opens a file name and returs a list containing all the first words in the file 
# Input Parameter(s): a file name
# Return Value(s): list containing all the first words in the file 
#==========================================
def first_words(fname):
    fp=open(fname)
    lis=[]
    for i in fp:
        r=i.split(' ')[0]
        lis.append(r)
    fp.close()
    return lis
#==========================================
# Purpose: takes a file name a returns a dictionairy with every single word as a key paired up with a list containing all the words that follow up the word in the file
# Input Parameter(s):the name of the file
# Return Value(s): a dictionary cotaining a word as a key paied witha list with a list containing every single word that comes after the key
#==========================================


def next_words(fname):
    fp=open(fname)
    ls=[]
    mydict={}
    for line in fp:
        line = line.strip('\n')
        line=line.split(' ')
        for word in line:
            ls.append(word)
    for i in range(len(ls)):
        if ls[i] not in mydict and ls[i] != '.' :
            lst = []
            if i < len(ls) - 1:
                lst.append(ls[i + 1])
                mydict[ls[i]] = lst
            else:
                mydict[ls[i]] = '.'
        elif ls[i] in mydict and ls[i] != '.' :
            if i < len(ls) -  1:
                mydict[ls[i]].append(ls[i + 1])
            else:
                mydict[ls[i]] = '.'
    fp.close()
    return (mydict)
#==========================================
# Purpose: prints 10 lines the first word must be random word from the words that come first in the file and followed by a random word in the list that follows the word in the dictionary
# Input Parameter(s): file name
# Return Value(s): a line where the word is chosen radomely from the results of first_words and the followed by a word in the list in the dictionary that follows the word. and keep using recursion until noting is left to get printed
#==========================================


import random
def fanfic(fname):
    dictionary=next_words(fname)
    for i in range(0,11):
        first_word=first_words(fname)
        random_word=random.choice(first_word)
        line =  ""
        while random_word != "." :
            line +=  random_word + " " 
            random_word = random.choice(dictionary[random_word])
        print(line + ".")


#==========================================
# Purpose: find he size of the txt files in a directory combined
# Input Parameter(s): directory which represents a nested dictionary of a directory
# Return Value(s): all the size of the txt files combined
#==========================================

def total_txt_size(directory):
    count=0
    for key in directory:
        if type (directory[key])==dict:
            count+=total_txt_size(directory[key])
        else:
            if 'txt' in key:
                count+=directory[key]
    return count

                    
                    
                    

































    

    
