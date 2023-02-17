year=int(input("What year do you want to start with? :"))           # Ask user to input year
numOfYears=int(input("How many years do you want to check? :"))     # Ask user for how many years to check
x=0                                                                 # set x as 0
for x in range(numOfYears):                                         # loop for number of years to check
    if (                                                        
        (year%400==0) or                                            # checks if the centuries are leap years    
        (year%100!=0) and                                           # or if the centuries are not leap years    
        (year%4==0)                                                 # check if years are leap years
    ):
        print ("Given Year is a Leap Year :",year)                  # prints the leap years
    else:
        print("Given year is not a leap year :",year)               # else prints the none leap years            
    year=year+1                                                     # adds 1 to the year until the number of years to check by user

"""
There is a leap year every year whose number is perfectly divisible by four - except for years which are 
both divisible by 100 and not divisible by 400. The second part of the rule effects century years. 
For example; the century years 1600 and 2000 are leap years, but the century years 1700, 1800, and 1900 are not
"""




