sum1=sum2=0
num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))
sum1=num1+num2+num3
if num1 !=num2 and num1!=num3:
   sum2+=num1
if num2 !=num1 and num2!=num3:
   sum2+=num2
if num3 !=num1 and num3!=num2:
   sum2+=num3
print("Numbers are",num1,num2,num3)
print("Sum of three given numbers is ",sum1)
print("Sum of non duplicate number is ",sum2)
                #output
Enter number 1 : 10001
Enter number 2 : 10002
Enter number 3 : 10003
Numbers are 10001 10002 10003
Sum of three given numbers is  30006
Sum of non duplicate number is  30006
