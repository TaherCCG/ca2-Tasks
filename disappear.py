usrInput=input("Please enter a message :")                                  # Ask user to enter a message
usrDisp=input("Please enter the letter you want to make disappear :")       # Ask user what characters they want to remove from message
for x in usrDisp:                                                           # set x for characters that the user wants removed
    usrInput=usrInput.replace(x, " ")                                       # replace x with " " to the message
print (usrInput)                                                            # print user message

