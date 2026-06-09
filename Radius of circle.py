radius=float(input("Enter radius of the cicle : "))
print("1.Calculate Area ")
print("2.Calculate Perimeter ")
choice=int(input("Enter your choice (1 or 2) :"))
if choice==1:
    area=3.14159*radius*radius
    print("Area of circle wit radius ",radius,'is',area)
else:
    perm=2*3.14159*radius
    print("Perimeter of circle with radius ",radius,'is',perm)
    #output
Enter radius of the cicle : 1000
1.Calculate Area 
2.Calculate Perimeter 
Enter your choice (1 or 2) :1
Area of circle wit radius  1000.0 is 3141589.9999999995


#output
Enter radius of the cicle : 1000
1.Calculate Area 
2.Calculate Perimeter 
Enter your choice (1 or 2) :2
Perimeter of circle with radius  1000.0 is 6283.179999999999
