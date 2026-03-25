#1 Square and cube
'''
def square():
    a=int(input("Enter a number:"))
    i=a**2
    return i
print(square())

def cube():
    a=int(input("Enter a number:"))
    i=a**3
    return i
print(cube())
'''
#2 Split digits
'''
def splitdigits():
    a=int(input("Enter a number:"))
    b=0
    while a>0:
        c=a%10
        b=b*10+c
        a=a//10
    print(b)
splitdigits()
'''

#3 Armstrong number
'''
def armstrong():
    a=int(input("Enter a number:"))
    count=0
    x=a
    y=a
    while a>0:
        count+=1
        a=a//10
    d=0
    while x>0:
        c=x%10
        d=d+c**count
        x=x//10
    if d==y:
        return "Armstrong number"
    return "Not armstrong"
print(armstrong())
'''
