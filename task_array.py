#1 Large and sum number with array
'''
a=[]
print("Enter 20 numbers:")
for i in range(20):
    a.append(int(input()))
large=a[0]
small=a[0]
total=0
for i in a:
    if i>large:
        large=i
    if i<small:
        small=i
    total+=i
print("The largest number is:",large)
print("The smallest number is:",small)
print("The sum is",total)
'''

#2 Marks,average,remarks
'''
n=int(input("Enter the number of students:"))
roll_number=[]
name=[]
eng_mark=[]
sci_mark=[]
math_mark=[]

for i in range(n):
    roll_number.append(int(input("Enter the roll number:")))
    name.append(str(input("Enter the name:")))
    eng_mark.append(int(input("Enter the mark of English:")))
    sci_mark.append(int(input("Enter the mark of Science:")))
    math_mark.append(int(input("Enter the mark of Maths:")))
print("Students Remarks")
for i in range(n):
    total=eng_mark[i]+math_mark[i]+sci_mark[i]
    average=total/3
    if average>=85:
        remark="Excellent"
    elif average>=75:
        remark="Distinction"
    elif average>=60:
        remark="First class"
    elif average>=50:
        remark="Poor"
    else:
        remark="Fail"
    print("Roll number",roll_number[i])
    print("Name",name[i])
    print("Average Mark",average)
    print("Remarks",remark)
'''

#3 Search an element in array
'''
a=[]
print("Enter 10 numbers:")
for i in range(10):
    a.append(int(input()))
f=int(input("Enter the number to search for:"))
if f==a[i]:
    print("The element is present in the list and the index position is:",a.index(f))
else:
    print("The element is not present in the list")
'''
#4 Max and min element in array
'''
a=[]
n=int(input("How many numbers you want to enter?"))
print("Enter the",n,"numbers:")
for i in range(n):
    a.append(int(input()))
max=a[0]
min=a[0]
for i in a:
    if i>max:
        max=i
    elif i<min:
        min=i
print("The maximum number is:",max)
print("The minimum number is:",min)
'''

#5 Ascending order
'''
a=[]
n=int(input("How many numbers you want to enter?"))
print("Enter the",n,"numbers:")
for i in range(n):
    a.append(int(input()))
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("The ascending order is:",a)
'''

#6 Descending order
'''
a=[]
n=int(input("How many numbers you want to enter?"))
print("Enter the",n,"numbers:")
for i in range(n):
    a.append(int(input()))
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print("The descending order is:",a)
'''
#7 Addition of one digit and two digit number
'''
a=[]
n=int(input("How many numbers you want to enter?"))
print("Enter the",n,"numbers:")
sum1=0
sum2=0
a1=[]
a2=[]
for i in range(n):
    a.append(int(input()))
for i in a:
    if i<10:
        sum1+=i
        a1.append(i)
    elif i>=10 and i<100:
        sum2+=i
        a2.append(i)
print("The one digit numbers are:",a1,"The sum of one digit number is:",sum1)
print("The two digits numbers are:",a2,"The sum of two digit number is:",sum2)
'''
#8 Duplicate element in the Array

a=[]
n=int(input("How many elements you want to enter?"))
print("Enter the",n,"elements:")
dup=[]
for i in range(n):
    a.append(input())
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            dup.append(a[i])
print("The duplicate element is",dup)





