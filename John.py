nameList=[]                                                     # define empty list
name=False                                                      # name= false
while name != True:                                             # while name is false
    userName= input ("Enter a Name :").lower().strip()          # ask user for name
    if userName== "john":                                       # if user name is john  
        name=True                                               # then name=True  (Break Loop)   
    else:                                                       # else    
        nameList.append(userName)                               # add name to list (loop continues)    
print ("Incorrect names entered:",nameList)                     # Print list of incorrect names

