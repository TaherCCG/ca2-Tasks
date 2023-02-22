<div align="center">

  #    Class Activity 2

### Table Of Contents

</br>

| Task Description   | Program Name        |                                 GitHub Link                   |
|--------------------|---------------------|---------------------------------------------------------------|
|[Task 1](#task-1)   | even.py             | https://github.com/TaherCCG/ca2-Tasks/blob/main/even.py       |
|[Task 2](#task-2)   | names.py            | https://github.com/TaherCCG/ca2-Tasks/blob/main/names.py      |
|[Task 3](#task-3)   | while.py            | https://github.com/TaherCCG/ca2-Tasks/blob/main/while.py      |
|[Task 4](#task-4)   | timestable.py       | https://github.com/TaherCCG/ca2-Tasks/blob/main/timesTable.py |
|[Task 5](#task-5)   | leapyear.py         | https://github.com/TaherCCG/ca2-Tasks/blob/main/leapyear.py   |
|[Task 6](#task-6)   | countdown.py        | https://github.com/TaherCCG/ca2-Tasks/blob/main/countdown.py  |
|[Task 7](#task-7)   | alternative.py      | https://github.com/TaherCCG/ca2-Tasks/blob/main/alternative.py|
|[Task 8](#task-8)   | separation.py       | https://github.com/TaherCCG/ca2-Tasks/blob/main/seperation.py |
|[Task 9](#task-9)   | disappear.py        | https://github.com/TaherCCG/ca2-Tasks/blob/main/disappear.py  |
|[Task 10](#task-10) | list_types.py       | https://github.com/TaherCCG/ca2-Tasks/blob/main/list_types.py |
|[Task 11](#task-11) | loop1000.py         | https://github.com/TaherCCG/ca2-Tasks/blob/main/loop1000.py   |
|[Task 12](#task-12) | john.py             | https://github.com/TaherCCG/ca2-Tasks/blob/main/John.py       |



</div>


***
***



### Task 1
*Steps:*
-  Create a new file called even.py.
-  Write a program that asks the user to enter a number.
-  Make use of the while loop repetition structure so the program prints out
all the even numbers from 1 up to (and possibly including) the number
given by the user.
-  Compile, save, and run your file.
<div align="right">

[back to Top](#table-of-contents)

</div>
Here is a simple flow chart of this program:

```mermaid
graph TD;
    InputNumber-->CheckInputNumber;
    CheckInputNumber-->lessThanInputNumber-->printIfEven;
    printIfEven-->+2;
    +2-->CheckInputNumber;
    CheckInputNumber-->End_If=InputNumber;
```
---
### Task 2
*Steps:*
-  Create a program called names.py to do the following:
-  Require the user to enter the names of all pupils in a class. The user
should be able to type “Stop” to indicate that the names of all the
students have been entered.
-  Print out the total number of names the users entered after the
loop has been exited.
-  Compile, save, and run your file.
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 3
*Follow these steps:*
-  Create a new file called while.py.
-  Write a program that always asks the user to enter a number.
-  When the user enters -1, the program should stop requesting the user to
enter a number.
-  The program must then calculate the average of the numbers entered,
excluding the -1.
-  Make use of the while loop repetition structure to implement the
program.
-  Compile, save, and run your file.
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 4 
*Follow these steps:*
-  Create a program file called timestable.py. 
-  This program needs to make use of for loops in order to display the times tables for any number. 
-  For example, say the user enters 6 - the program must print out the 6 times table from start (1) to end (12), something like this: The 6 times table is: 6 x 1 = 6 6 x 2 = 12 … 6 x 12 = 72 
-  Compile, save, and run your file.  
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 5
*Follow these steps:* 
A simple rule to determine if a year is a leap year is to test if it is a multiple of 4. 
-  Create a program file called leapyear.py.
-  In this file, write a program to input a year and a number of years.
-  Then use for loops to determine and display which of those years were or will be leap years. What year do you want to start with? 1994 How many years do you want to check? 8 1994 isn’t a leap year 1995 isn’t a leap year 1996 is a leap year 1997 isn’t a leap year 1998 isn’t a leap year 1999 isn’t a leap year 2000 is a leap year 2001 isn’t a leap year.
-  Compile, save and run your file.  
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 6
*Follow these steps:*
-  Create a new Python file in this folder called countdown.py.
-  The activities in this task are all different and are designed to test your knowledge of loops, including a little while-loop revision.
-  Create a while loop that will display count down from 20 to 0.
-  Next, create a loop (any) that will display all the even numbers between 1 and 20.
-  Now, create a loop that will produce the following output: * ** *** **** *****
-  Finally, write the code to compute the greatest common divisor (GCD, or highest common factor) of two positive integers.
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 7
 *Follow these steps:* 
-  Create a program called alternative.py that reads in a string and makes each alternate character an uppercase character and each other alternate character a lowercase character (e.g, the string “Hello World” would become “HeLlO WoRlD”)
-  Now, try starting with the same string but making each alternative word lower and upper case (e.g. the string “I am learning to code” would become “i AM learning TO code”). Using the split and join functions will help you here.  
<div align="right">

[back to Top](#table-of-contents)

</div>

--- 
### Task 8 
 *Follow these steps:* 
-  Write a program called separation.py that inputs a sentence and then displays each word of the sentence on a separate lines.
 <div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 9
 *Follow these steps:* 
-  Write a Python program called disappear.py that strips a set of characters from a string. 
-  Ask the user to input a string and then ask the user which characters they would like to make disappear. 
-  For example: 
-  The quick brown fox jumps over the lazy dog. 
-  After stripping a,e,i,o,u: 
-  Th qck brwn fx jmps vr th lzy dg.
<div align="right">

[back to Top](#table-of-contents)

</div>

--- 
### Task 10
 *Follow these steps:* 
-  Create a new Python file in this folder called list_types.py. 
-  Imagine you want to store the names of three of your friends in a list of strings. Create a list variable called friends_names, and write the syntax to store the full names of three of your friends. 
-  Now, write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list. 
-  Now, define a list called friends_ages that stores the age of each of your friends in a corresponding manner, i.e., the first entry of this list is the age of the friend named first in the other list.  
<div align="right">

[back to Top](#table-of-contents)

</div>

---
### Task 11
 *Follow these steps:* 
-  Create a new Python file in this folder called loop1000.py. 
-  You are asked to print out all the numbers from 1 to 1000. Write 2 lines of code in your file to print out all numbers from 1 to 1000. 
-  Once you've got this to work, add logic inside your loop to only print out the numbers from 1 to 1000 that are even (i.e. divisible by 2). Remember the modulo command — i.e., %. 10%5 will give you the remainder of 10 divided by 5. 10 divided by 5 equals 2 with a remainder of 0. Hence, this statement returns 0. Any even number is a number that can be divided by 2 with no remainder.  
<div align="right">

[back to Top](#table-of-contents)

</div>

--- 
### Task 12 
 *Follow these steps:* 
-  Write a Python program called john.py that takes in a user’s input as a string. 
-  While the string is not “John”, add every string entered to a list until “John” is entered. This program basically stores all incorrectly entered strings in a list where “John” is the only correct string. 
-  Print out the list of incorrect names. 
-  Example program run (what should show up in the Python Console when you run it): Enter your name : <user enters="" tim=""> Enter your name : <user enters="" mark=""> Enter your name: <user enters="" john=""> Incorrect names: [‘Tim’, ‘Mark’] 
-  HINT: When testing your While loop, you can make use of .upper() or .lower() to eliminate case sensitivity.</user></user></user>
<div align="right">

[back to Top](#table-of-contents)

</div>

---
