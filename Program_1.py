'''
Program 1
Write a program to input a positive number and check if the number is a four digit number
or not. If the number is of four digits then print the sum of its first and last digit ,
and if the number is not of four digits then print the number is a buzz number or not .
Sample input1: 5321
Sample Output1: the sum of first and last digit is 6
Sample input2: 497
Sample output2: it is a buzz number

    '''

num=input("Enter a positive number")
#at this stage of the program 'num' is a kind of string
#finds the length of the string 'num' using len()
nod=len(num)
#converts the num to integer kind
num=int(num)
if nod==4:
    ld=num%10
    fd=num//1000
    sum=ld+fd
    print ("The number is of four digits ")
    print ("The sum of first and last digit is ",sum)
else:
    if num%7==0 or num%10==7:
        print("The number is not of four digits")
        print("The number is a Buzz number")
    else:
        print("The number is not of four digits")
        print("The number is NOT A BUZZ number")


