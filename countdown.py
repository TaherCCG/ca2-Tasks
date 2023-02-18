"""
Loop 1: Count from 20 to 1
"""

x=20                                        # Sets loop start at 20
while x>0:                                  # while x is above 0
    print(x)                                # print x
    x-=1                                    # x = x - 1    

"""
Loop 2: Count from 2 to 20 even numbers
"""
y=2                                         # Sets loop start at 2
while y<21:                                 # while y is below 21    
    print(y)                                # print y
    y+=2                                    # y = y + 2

"""
Loop 3: Count from 1 to 20 prints number of '*' in each line with increasment
"""
z=1                                         # sets loop at 1
while z<21:                                 # while loop is below 21    
    print(z*"*")                            # print '*' * z
    z+=1                                    # z = z + 1            


"""
GCD Greatest common divisor of two positve integers
"""
a=int(input("Input your 1st Number :"))         # Get input from user as number a
b=int(input("Input your 2nd Number :"))         # get input from user as number b

def gcd(a,b):                                   # define GCD function
    if a % b == 0:                              # if a is disior b is 0 
        return b                                # then return b
    for c in range(int(b/2),0,-1):              # if a is not divisable by b it enters a for loop.     
        if a % c == 0 and b % c ==0:            # c checks if a and b are common divisors, 
            gcd=c                               # and if it is the c is set as var of gcd
            break                               # break out of loop
    return gcd                                  # returns the function of gcd a and b

print ("GCD of",a,"and",b,"=",gcd(a,b))         # Prints the GCD

"""
The greatest common divisor (GCD) of two or more numbers is the greatest common factor number 
that divides them, exactly. It is also called the highest common factor (HCF). For example, 
the greatest common factor of 15 and 10 is 5, since both the numbers can be divided by 5. 15/5 = 3. 10/5 = 2.
"""