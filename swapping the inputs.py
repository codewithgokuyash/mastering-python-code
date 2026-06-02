x=int(input("Enter any number 1: "))
y=int(input("Enter any number 2: "))
z=int(input("Enter any number 3: "))
print("Original number :", x,y,z)
x,y,z=y,z,x
print("After swapping ;",x,y,z) 
                #output
Enter any number 1: 1000
Enter any number 2: 2000
Enter any number 3: 10
Original number : 1000 2000 10
After swapping ; 2000 10 1000
