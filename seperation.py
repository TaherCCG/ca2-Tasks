sep=input("Enter a message :")                  # Ask user to enter a message

for x in sep:                                   # check number of characters in message
    if x ==" ":                                 # if any are spaces
        print()                                 # then print() nothing, (adds line)   
    else:                                       # else
        print(x, end="")                        # print x till the end of characters 
print()                                         # Print nothing (adds line)

