'''
Program 4
A school library charges fine from its users according to the given table .
Assuming that the book is returned late
Write the program to calculate the fine charged by the library. Use slab system.
No. of Days returned late   Fine charged
Less than 5 days            Rs 1/day
5 to 10 days                Rs 3/day
11 to 15 days               Rs 5/day
16 to 20 days               Rs 7/day
More than 20 days           Rs 10/day
'''
lateDays=input("Enter the number of days book was returned late")
lateDays=int(lateDays)
if lateDays < 5:
    fine=lateDays * 1
elif lateDays >=5 and lateDays<=10:
    fine=(4*1)+(lateDays-4)*3
elif lateDays >=11 and lateDays<=15:
    fine=(4*1)+(6*3)+(lateDays-10)*5
elif lateDays >=16 and lateDays<=20:
    fine=(4*1)+(6*3)+(5*5)+(lateDays-15)*7
else:
    fine=(4*1)+(6*3)+(5*5)+(5*7)+(lateDays-20)*10
print("Total number of days book was returned late:", lateDays)
print("Total fine is Rs ",fine)




