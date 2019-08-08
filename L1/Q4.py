from math import *
year=int(input("What is the year?\n"))
if year%400 == 0:
    print( "Yes, it is  a leap year")
elif ((year%4 ==0)and (year%100 !=0)):
    print( "Yes, it is  a leap year")
else:
    print( "No, it is not a leap year")
    


