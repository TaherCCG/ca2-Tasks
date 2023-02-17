nums=[]                                  # define empty list

while True:                              # loop until true 
    num=int (input("Input a number :"))  # ask user input number 
    if num == -1:                        # if -1 is stop then break
        break                            # break
    nums.append(num)                     # appends list

print ("Numbers:",nums)                  # Print list

sums=sum(nums)                           # sums the numbers in list to get total
avg=sums/len(nums)                       # devides the total by the number of list (nums)   

print ("total number: ",sums)            # Print Total
print("Average is :",avg)                # Print Average