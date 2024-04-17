'''
Program  8
Write a program to input marks of five different subjects (eng , hindi, science, comp  and maths )
and  print  the grade as per the given criteria. The maximum marks of each subject is 100.
(Using if else if statement)
Percentage Marks          Grade
From 75 to 100            Passed with star
From 60 to less than 75   First Division
From 40 to less than 60   Second Division
Less than 40              Failed

Note: use mnemonic code variable names 
'''
# First way to input multiple values using the split() function
eng,hin,sc,comp,math=input("Enter the marks of 5 subjects,english,hindi,science,computer and maths").split()
# Second way to input
'''
eng=input("Enter English marks")
hin=input("Enter Hindi marks")
sc=input("Enter science marks")
comp=input("Enter computer marks")
math=input("Enter maths marks")
'''
eng=int(eng)
hin=int(hin)
sc=int(sc)
comp=int(comp)
math=int(math)
sum=eng+hin+sc+comp+math
per=sum/5
if per>=75 and per<=100:
    grade="Passed with star"
elif per>=60 and per<=75:
    grade="First Division"
elif per>=40 and per <=60:
    grade="Second Division"
else:
    grade="Failed"
print("Total is ",sum, "percentage is ",per,"and your grade is ",grade)
