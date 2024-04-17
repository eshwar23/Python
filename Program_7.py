'''
Program 7
A local electricity board charges money from the customers based on the following table
Number of units consumed    Charge
Less than or equal to 100   Rs 3/unit
101 to 250                  Rs 5/unit
251 to 600                  Rs 10/unit 
More than 600 units         Rs 20/unit

Note: Slab system to be implemented
WAP to input the number of units the customer consumed and print the electricity bill 
'''
nou=input("Enter the number of units")
nou=int(nou)
if nou<=100:
    ch=nou*3
elif nou>=101 and nou<=250:
    ch=(nou-100)*5 + (100*3)
elif nou>=251 and nou<=600:
    ch=(nou-250)*10 + (100*3) + (150*5)
else:
    ch=(nou-600)*20 + (350*10) + (150*5) + (100*3)
print ("The number of units consumed is ",nou)
print ("The total charge is Rs",ch)
