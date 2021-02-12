import random
def rand_int(min=0, max=100):
    if isinstance(min, int) == False or isinstance(max,int) == False:
        return "Invalid Parameters"
    if min<0 or max<0 or min>max or min==max:
        return "Invalid integers"

    rand = round( random.random() * max + min )
    return rand
print(rand_int()) 		    # should print a random integer between 0 to 100
print(rand_int(max=50)) 	    # should print a random integer between 0 to 50
print(rand_int(min=50)) 	    # should print a random integer between 50 to 100
print(rand_int(min=50, max=500)) # should print a random integer between 50 and 500
print(rand_int(max='cheese'))
print(rand_int(50,40))