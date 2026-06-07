def palindrome():
        a=input(str("Enter a string:"))
        b=""
        for i in a:
            b=i+b
        print(b)
        if b==a:
            print("Palindrome")
        else:
            print("Not palindrome")
palindrome()
palindrome()

def vowel(a):
    i=['a','e','i','o','u']
    for j in i:
        if j==a:
            return "Vowel"
        else:
            return "Consonant"
print(vowel("a"))
print(vowel("k"))


def vovwel():
    i=['a','i','o','e','u']
    a=input(str("Enter:"))
    for j in i:
        if j==a:
            return "Vowel"
        else:
            return "Consonant"
print(vovwel())
print(vovwel())

def fibonacci():
    n=(int(input("Enter a  number:")))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n - 1) + (n - 2)
print(fibonacci())
    

    
# Take two numbers from user input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The sum is:",(x+y))


a=int(input("ENter a num:"))
assert a==10
print(a)

def div():
    a=int(input("Num1:"))
    b=int(input("Num2"))
    if b==0:
        raise ZeroDivisionError("Cant divide")
    return a/b
print(div())

def remove_duplicates(arr):
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(remove_duplicates(arr))


def move_zero(a):
    z=[]
    n=[]
    for i in a:
        if i == 0:
            # z.append(i)
            z=z+[i]
        else:
            # n.append(i) 
            n=n+[i]
    for f in range(len(n)):
        for h in range (f+1,len(n)):
            if n[f]>n[h]:
                temp = n[f]
                n[f] = n[h]
                n[h] = temp
    return n+z

a=[8,0,1,7,2,3,0,4]
print(move_zero(a))  

def multi_max_2(a):

    for i in range (len(a)):
           for j in range (i+1,(len(a))):
            if a[i]>a[j]:
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
    return a[-1]*a[-2]

a=[0,2,8,4,3]
print("The multi is:",multi_max_2(a))

def display_duplicate(a):
    d=[]
    for i in range (len(a)):
        for j in range (i+1,(len(a))):
            if a[i]==a[j] and a[i] not in d:
                d+=a[i]
    return d
a=[1,2,2,3,4,4,2,1,4]
# a=list(map(int,input("Enter numbers").split()))
print(display_duplicatedup(a))

def sec_large(a):
    for i in range (len(a)):
        for j in range(i+1,(len(a))):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a[-2]
a=[1,4,2,6,7]
print(sec_large(a))

def add_1_all(a):

    for i in range(len(a)):
        if a[i] == 9:
            a[i] = 0

        else:
            a[i] = a[i] + 1
    return a
a = [9,9,9]
print(add_1_all(a))



def comp(a,b):
    if len(a)!=len(b):
        return False

    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if a[i]>a[j]:
                temp = a[i]
                a[i]=a[j]
                a[j]=temp

    for i in range (len(b)):
        for j in range(i+1,len(b)):
            if b[i]>b[j]:
                temp = b[i]
                b[i]=b[j]
                b[j]=temp
     
    for i in range (len(a)):
        if a[i]!=b[i]:
            return False
    return True

a=[1,2,4,7,3]
b=[1,5,2,4,3]
print(comp(a,b))

def frequency(a):
    d={}
    for i in range (len(a)):
        count=0
        for j in range (len(a)):
            if a[i]==a[j]:
                count+=1
        if count>1 and a[i] not in d:
            d[a[i]]=count
    return d
a=[1,2,3,1,3,3,4,4,5,5,5]
print(frequency(a))


def missing_number(a,n):

    total1=0
    for i in range(1,n+1):
        total1+=i
    total2=0
    for i in a:
        total2+=i
    return total1-total2
a=[1,2,4,5]
print(missing_number(a,5))

def intersection(a,b):
    d=[]
    e=[]
    for i in range (len(a)):
        for j in range (len(b)):
            if a[i]==b[j] and j not in e:
                d+=[a[i]]
                e+=[j]
                break #stops after finding common element
    return d
a=[1,2,4,5,7]
b=[1,2,5,7,8,9]
print(intersection(a,b))

def swap_array(a):

    first=a[0]
    for i in range (len(a)-1):
        a[i]=a[i+1]
    a[len(a)-1]=first

    return a
a=[1,2,3,4,5]
print(swap_array(a))

def left_rotate_by_2(a):
    first=a[0]
    second=a[1]
    for i in range(len(a)-2):
        a[i]=a[i+2]
    
    a[len(a)-2]=first
    a[len(a)-1]=second
    return a
a=[1,2,3,4,5]
print(left_rotate_by_2(a))

def arr_true(a):
    a_copy=a.copy()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

    if a==a_copy:
        return True
    return False

a=[5,2,3,6,1]
print(arr_true(a))

def remove_duplicate(a):
    result = []
    for i in range(len(a)):
        if a[i] not in result:
            result = result + [a[i]]
    return result
a = [1, 1, 2, 3, 4, 4, 5, 6, 6]
print(remove_duplicate(a))

def inter_display_unique_elements(a,b):
    result=[]

    for i in range (len(a)):
        for j in range (len(b)):
            if a[i]==b[j]:
                break
        else:
                result.append(a[i])
    for i in range (len(b)):
        for j in range (len(a)):
            if b[i]==a[j]:
                break
        else:
                result.append(b[i])
    return result

a=[1,2,3,4]
b=[6,8,9]
print(inter_display_unique_elements(a,b))

def odd_even_count(a):
    count1=0
    count2=0
    for i in a:
        if i%2==0:
            count1+=1
        else:
            count2+=1
    return count1,count2
a=[2,3,4,5,6]
print(odd_even_count(a))


def left_rotate(a,k):
    n=len(a)
    k=k%n
    temp=[]
    for i in range(k):
        temp.append(a[i])

    for i in range(n-k):
        a[i]=a[i+k]

    for i in range(k):
        a[n-k+i]=temp[i]

    return a
a=[1,2,3,4,5]
k=1
print(left_rotate(a,k))

        
def vowels(a):
    count=0
    result=""
    for char in a:
        if 'A'<= char <='Z':
            char = chr(ord(char)+32)
        if char=='a' or char=='e' or char =='i' or char=='o' or char =='u':
            count+=1
            result+=char
    return count,result
a="Hello Dude"
print(vowels(a))

def missing_number(a,n):
    total1=0
    total2=0
    for i in a:
        total1+=i
    for i in range (1,n+1):
        total2+=i

    return total1,total2,n
a=[1,2,3,5]
n=5
print(missing_number(a,n))

def solution(a):
    b=""
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b
a="world" 
print(solution(a))

def narcissistic(a):
    power=0
    x=a
    temp = a
    while a>0:
        power+=1
        a=a//10
    ans=0
    while x>0:
        c=x%10
        ans=ans+c**power
        x//10
        
    if ans==temp:
        return True
    return False
a=153
print(narcissistic(a))


def square(n):
    root=0
    while n>0:
        a=n%10
        root+=a*a
        n//10
    return root
print(square(123))
