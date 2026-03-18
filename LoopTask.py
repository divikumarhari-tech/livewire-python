#1 Sum of odd and even integers
'''
a=int(input("Enter number:"))
b=0
c=0
for i in range(1,a+1,1):
      if i%2==0:
         b+=i
      else:
          c+=i
print("The sum of even number is:",b)
print("The sum of odd number is:",c)
          
'''
#2 Multiplication table of a number
'''
a=int(input("Enter a number:"))

for i in range(1,11):
      print(i,"*",a,"=",i*a)

 '''

#3 Factorial
'''
a=int(input("Enter a number:"))
b=1
for i in range(1,a+1):
    b*=i
print(b)
'''

#4 Printing alphabets a to z
'''
for i in range(97,123):
    print(chr(i),"-", i)
    
 '''
#5 Printing alphabets Z to A
'''
for i in range(90,64,-1):
    print(chr(i),"-",i)
      
 '''
#6 Print ASCII values
'''
for i in range(1,256):
    print(chr(i),"-",i)

'''

#7 Harshad number
'''
a=int(input("Enter a number:"))
d=a
sum=0
while a>0:
    sum+=a%10
    a//=10
if d%sum==0:
    print("Harshad number")
else:
    print("Not harshad number")

'''
#8 sum of divisors
'''
a=int(input("Enter a number:"))
sum=0
for i in range(1,a+1):
    if a%i==0:
        sum+=i
print(sum)'''

#9 Fibonacci series
'''
a=int(input("Enter the range:"))
n=0
n1=1
print(n)
for i in range(1,a+1):
    n2=n+n1
    n=n1
    n1=n2
    print(n1)
'''
