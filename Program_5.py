'''
Program 5
A Jsr travelling agency charges money for a cab as per the following given chart
based on the distance traveled by the passenger.
Distance traveled in Km            Charges
Less than or equal to 10 km        Rs 15/km
11 km to 20 km                     Rs 12/km
21 to 50 km                        Rs 8/km
More than 50 Km                    Rs 6/km

Note : Implement slab system to calculate the charge 
WAP to input the distance traveled by the passenger and calculate the amount to be paid.
'''
dt=input("Enter the distance traveled by the passenger")
dt=int(dt)
if dt<=10:
    charge=15*dt
elif dt>10 and dt<=20:
    charge=(10*15) + (dt-10)*12
elif dt>=21 and dt<=50:
    charge=(10*15) + (10*12)+(dt-20)*8
else:
    charge=(10*15) + (10*12)+(30*8)+(dt-50)*6
print("Distance travelled ",dt,"\ncharge",charge)# \n is for new line
