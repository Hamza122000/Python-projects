  # problem 1:
#==========================================
# Purpose: (this function uses einstein  equation of speical relativty to find the contracted distance between two objects  ?)
# Input Parameter(s): ( there are two parameters: dist, speed) = distance is the original distance, and speed is the speed
# at which we are travelling relative to the two objects 
# Return Value(s): (the contracted distance between two objectd gets returned)
#==========================================

def length_contract(dist, speed):
    c_sqaured=(3*10**8)**2
    dist=dist*(1-((speed**2)/(c_sqaured)))**0.5
    return dist

# problem 2:
#==========================================
# Purpose: (This function calculates bessels average speed in his run through the 12 parsec region of space?)
# Input Parameter(s): (speed) speed is the speed that bessel is traveling at in the region of space
# Return Value(s): ( it returns two things: time required to traverse the segment as seen by a stationary observer, and then as seen by bessel)
#==========================================

def bessel_run(speed):
    twelve_parsec = (3.086 * 10**16)*12
    year = 31557600
    x=length_contract(twelve_parsec,speed)
    print(twelve_parsec/speed/year)
    return (x/speed/year)


# problem 3.fucntion.1:
#==========================================
# Purpose: (this function prints the phrase "who needs loops" 5 times  ?)
# Input Parameter(s): ( there are no input parameters 
# at which we are travelling relative to the two objects 
# Return Value(s): (This function does not return any values)
#==========================================

def print_loop():
    print('Who needs loops?')
    print('Who needs loops?')
    print('Who needs loops?')
    print('Who needs loops?')
    print('Who needs loops?')
#problem 3.fucntion.2:    
#==========================================
# Purpose: (this function calls the fucntion 'print_loop' 5 times)
# Input Parameter(s): ( there are no input parameters 
# at which we are travelling relative to the two objects 
# Return Value(s): (This function does not return any values)
#==========================================

def print_loop_2():
    print_loop()
    print_loop()
    print_loop()
    print_loop()
    print_loop()
#problem 3.fucntion.2:    
#==========================================
# Purpose: (this function calls the fucntion 'print_loop-2' 4 times)
# Input Parameter(s): ( there are no input parameters 
# at which we are travelling relative to the two objects 
# Return Value(s): (This function does not return any values)
#==========================================

def print_100():
    print_loop_2()
    print_loop_2()
    print_loop_2()
    print_loop_2()

    
