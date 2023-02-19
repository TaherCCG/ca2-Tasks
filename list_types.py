friends_name=["Muhammad Ali","Bruce Lee","Khabib Nurmagomedov"]     # list of friends

print(friends_name[0])                                              # Print 1st friend in list
print(friends_name[2])                                              # Print last friend in list

print("length of the friends list",len(friends_name))               # Print length of friends list

friends_ages=["74","32","35"]                                       # Friends age

x=0                                                                 # sets x as 0 ( the number we will start the count from) 
while x < len(friends_name):                                        # while x is lower then the length of friends list
    print (friends_name[x],friends_ages[x])                         # print friends name and age at number x
    x=x+1                                                           # add 1 to x 

