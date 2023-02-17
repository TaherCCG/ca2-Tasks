print ("Even Numbers\n")                        # Print Title
usrInput=int(input("Enter a any number:"))      # Ask use for Number

start= usrInput+1 if usrInput&1 else usrInput   # set var to set even numbers

x=0                                             # set var x = 0
while x < start:                                # loop whle x is below start
    print (x+2)                                 # print numbers
    x=x+2                                       # increase x by 2
    
