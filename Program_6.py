'''
Program 6
The income tax (given in percentage %) to be paid by a person is based on the following given slab system.
Annual gross income              Tax %
Less than or equal to 100,000    No tax to be paid
100,001 to 150,000               Rs 3000 + 10% of Income exceeding Rs 100,000
150,001 to 300,000               Rs 6000 + 15% of Income exceeding Rs 150,001
More than 300,000                Rs 10,000 + 25% of Income exceeding Rs 300,000

WAP to input the annual gross income and calculate the amount to be paid as tax.
'''
agi=input("Enter the annual gross income")
agi=int(agi)
if agi<=100000:
    tax=0
elif agi>=100001 and agi<=150000:
    tax=3000+(10/100)*(agi-100000)
elif agi>=150001 and agi<=30000:
    tax=6000+(15/100)*(agi-150001)
else:
    tax=10000+(25/100)*300000
print("Annual gross income",agi,"\ntax=",tax)