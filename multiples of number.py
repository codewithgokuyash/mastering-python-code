print("Enter five numbers below")
num1=float(input("First number  : "))
num2=float(input("Second  number  : "))
num3=float(input("Third number  : "))
num4=float(input("Fourth number  : "))
num5=float(input("Fifth number  : "))
divisor=float(input("Enter divisor number : "))
count=0
print("Multiples of ",divisor ,"are :")
remainder =num1%divisor
if remainder==0:
     print(num1,sep=" ")
     count+=1
remainder=num2%divisor
if remainder==0:
    print(num2,sep=" ")
    count+=1
remainder=num3%divisor
if remainder==0:
   print(num3,sep=" ")
   count+=1
remainder=num4%divisor
if remainder==0:
   print(num4,sep=" ")
   count+=1
remainder=num5%divisor
if remainder==0:
   print(num5,sep=" ")
   count+=1
print()
print(count,"multiples of ",divisor,"found")
        #output
Enter five numbers below
First number  : 10
Second  number  : 20
Third number  : 30
Fourth number  : 40
Fifth number  : 50
Enter divisor number : 5
Multiples of  5.0 are :
10.0
20.0
30.0
40.0
50.0

5 multiples of  5.0 found
