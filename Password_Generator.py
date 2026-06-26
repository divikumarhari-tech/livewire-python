import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z ']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','=','+','_','[',']','{','}','|',':',';','<','>','.','?']
noOfLetters=int(input("How many letters would you like in your password?\n"))
noOfSymbols=int(input("How many symbols would you like?\n"))
numOfNumbers=int(input("How many numbers would you like?\n"))
passwordList=""

for char in range(1,noOfLetters+1):
    passwordList+=random.choice(letters)


for char in range(1,noOfSymbols+1):
    passwordList+=random.choice(symbols)

for char in range(1,numOfNumbers+1):
    passwordList+=random.choice(numbers)

print(f"Your password is: {passwordList}")
