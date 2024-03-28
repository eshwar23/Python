'''
Program 3           [ICSE - 2006]
NOTES
Note 1 : in place of switch , match keyword is used in python and no break statement is used
Note 2 : _ (underscore) is used in place of default
Note 3 : rem: import math and random
Note 4 : How to use some math functions: math.log(num) , abs(num) , math.sqrt(num) , random.random()
----------------------------------------------------------------------------------------------------
Write a program that outputs the results of the following evaluations based on the number entered
by the user.
(1) Natural logarithm of the number
(2) Absolute value of the number
(3) Square root of the number
(4) Random number between 0 and 1.
'''
import math
import random
print("1-Find Natural Logarithm of a number")
print("2-Find Absolute value of the number")
print("3-Find the square root of the number")
print("4-Find Random number between 0 and 1")
ch=input("Enter Choice 1 to 4")
match ch:
    case "1":
        num=input("Enter a positive value whose log needs to be found")
        num=int(num)
        print("The log of value ",num , "is", math.log(num))
    case "2":
        num=input("Enter value whose absolute value needs to be found")
        num=int(num)
        print("The absolute value of ",num , "is", abs(num))
    case "3":
        num=input("Enter a positive value whose square root needs to be found")
        num=int(num)
        print("The square root of ",num , "is", math.sqrt(num))
    case "4":
       print("Random number between 0 and 1 is ",random.random())
    case _:
        print("Entered wrong choice")
    
        