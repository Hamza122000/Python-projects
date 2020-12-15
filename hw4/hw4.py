# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    letter1='a'
    letter2='a'
    letter3='a'
    letter4='a'
    while letter1 <= 'z':
        letter2='a'
        while letter2 <= 'z':
            letter3='a'
            while letter3 <= 'z':
                letter4='a'
                while letter4<='z':
                    password = letter1+letter2+letter3+letter4
                    if decrypt(data,password):
                        return password
                    letter4=chr(ord(letter4)+1)
                letter3=chr(ord(letter3)+1)
            letter2=chr(ord(letter2)+1)    
        letter1=chr(ord(letter1)+1)


# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def prime(number):
    if number == 1:
        return False
    end =  int(number**(1/2.0))
    primeFound = True
    if end+1 < 2 :
        return False
    for i in range(2, end+1):
        if number % i == 0: 
            primeFound = False
    return primeFound
           



def count_primes(low,high):
    if low > high :
        return 0
    count = 0
    for num in range(low,high+1):
        if prime(num):
            count = count + 1
            print(num,' is a prime number')
    return count

# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================
def population(small,middle,big):
    count = 0
    while small >= 10 and big >= 10 and middle >= 10:
        if count < 100 :
            stemp = small + (0.1*small - 0.0002*small*middle)  
            mtemp = middle + (-0.05*middle + 0.0001*small*middle - 0.00025*middle*big)
            btemp = big + (-0.1*big + 0.0002*middle*big)
            small = stemp
            big = btemp
            middle = mtemp
            count =  count + 1
            print('week', count,'small=',int(small),'middle=', int(middle), 'Big=',int(big))
    return count
    
#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


