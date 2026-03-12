#Loop increment
'''
for i in range(1,11,1):
    print(i)'''

#Loop decrement
'''
for i in range(10,0,-1):
    print(i)'''

#loop string
'''
a="Ezio"

for i in a:
    print(i)'''

#Addition using Loop
'''
a=0
for i in range(1,6):
    a+=i
    print(a)
print(a)'''

#Factorial using Loop
'''
a=1
for i in range(1,20):
    a*=i
print(a)'''

#Factorial from runtime input
'''
a=int(input("Enter a number"))
b=1
for i in range(1,a+1):
    b*=i
print(b)'''

#Finding divisor
'''
a=int(input("Enter a number"))
for i in range(1,a+1):
    if a%i==0:
     print("The divisor of the given number is:",i)'''

#sum of divisor
'''
a=int(input("Enter a number"))
add=0
for i in range(1,a+1):
    if a%i==0:
        add+=i
print("The Sum of divisor is:",add)'''

#Prime number or not
'''
a=int(input("Enter a number"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
if count==2:
    print(a,"is prime number")
else:
    print(a,"not a prime number")'''

#star pattern
'''
for i in range(1,5):
    for j in range(i):
        print("*",end="  ")
    print()'''
# number pattern
'''
for i in range(1,10):
    for j in range(i):
        print(i,end=" ")
    print()'''
'''

for i in range(9,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()'''

#printing alphabet
'''
a=65
for i in range(1,8):
    for j in range(i):
        print(chr(a),end=" ")
        a+=1
        if a>90:
            a=65
    print()'''
#printing number in reverse order
'''
a=20
for i in range(1,10):
    for j in range(i):
        print(a,end=" ")
        a-=1
        if a<0:
            a=20
    print()'''
    
