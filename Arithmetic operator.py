num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
op=input("Enter operator [+-*/%] :")
result=0
if op=='+':
    result=num1+num2
elif op=='-':
   result=num1-num2
elif op=='*':
   result=num1*num2
elif op=='/':
   result=num1/num2
elif op=='%':
   result=num1%num2
else:
   print("Invalid operator ")
print(num1,op,num2,'=',result)
    #output
Enter first number : 10001
Enter second number : 2002
Enter operator [+-*/%] :#
Invalid operator 
10001.0 # 2002.0 = 0

   #output
Enter first number : 10001
Enter second number : 20002
Enter operator [+-*/%] :+
10001.0 + 20002.0 = 30003.0

    #output
Enter first number : 10001
Enter second number : 20002
Enter operator [+-*/%] :*
10001.0 * 20002.0 = 200040002.0
