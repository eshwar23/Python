'''
Program 2         [ICSE-2006]

A cloth showroom has announced the following festival discounts
on the purchase of items, based on the total cost of the items purchased:-

Total cost                      Discount (in percentage)
Less than or equal to Rs 2000   5%
Rs2001 to Rs5000                25%
Rs5001 to Rs10000               35%
AboveRs10000                    50%

Write a program to input the total cost and compute and display the amount to be paid
by the customer after availing the discount.
'''

tc=input("Enter the total cost of the cloth")
tc=int(tc)
if tc<=2000:
    discount=5
elif tc>=2001 and tc<=5000:
    discount=25
elif tc>=5001 and tc<=10000:
    discount=35
else:
    discount=50
amount=tc-(discount/100)*tc
print("Total cost of cloth =" , tc)
print("Amount to be paid after discount=" , amount)

