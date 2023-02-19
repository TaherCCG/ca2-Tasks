"""
Letters
"""

inStr=input("Enter a message :")                        # Ask user to input message
print ("your original message is :" + str(inStr))       # Print message

outStr=""                                               # sets blank string     
for x in range(len(inStr)):                             # check number of characters (x) in length of message
    if not x %2:                                        # if its not dividend of 2 then    
        outStr=outStr + inStr[x].upper()                # make the character to  uppercase    
    else:                                               # else
        outStr=outStr + inStr[x].lower()                # make the character to lowercase    
print ("Message 1 is :" + str(outStr))                  # prints the new message


"""
Words
"""
wordStr=input("Enter a message :").split()              # ask user to input message and splits/separate the message         
wordOut=" ".join(                                       # Join the words with whitespace (space)
    [x.upper() if i%2                                   # if word is divdent of 2 then make it uppercase
     else x.lower()                                     # else make it lowercase    
     for i, x in enumerate(wordStr)])                   # for count, value (word) in emumerate message
print ("Message 2 is :" + str(wordOut))                 # Print new message

"""
Return an enumerate object.
  iterable
    an object supporting iteration
The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
"""


