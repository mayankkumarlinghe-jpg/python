# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = 'Hello, world!'

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {'name': 'Alice', 'age': 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None

#Write a program to check whether a number is positive.
num = int(input("Enter Number"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is 0")
"""Design an algorithm using nested if-else and elif statements to determine the grade of
a student based on their score. The grading scale is: A for 90-100, B for 80-89, C for 70-79, D for 60-69,
and F for below 60.
"""
marks = int(input("Enter the marks of student")
if marks > 0:
            if marks => 90 and marks <=100:
                print("Grade A")
            elif marks = >80 and marks <= 89:
                print("Grade B")
            elif marks => 70 and marks <= 79:
                print("Grade C")
            elif marks => 60 and <= 69:
                print("Grade D")
            elif marks < 60:
                print("Grade F")
else:
    print("Enter valid amrks")

#Loops in Python 
#for loop implemetation using for multiplication program:

for i in range(1,11):
    print(f"9 X {i} = {9*i}")

i=1
while i<11:
    print(f"9 X {i} = {9*i}")
    i+=1
list =[1,2,3,4,5,6,7,8]
result=[]
for item in list:
    if item % 2 ==0:
        pass
    else:
        result.append(item*2)
print(result)

#usage of break and continue
""" the break statement when executed in a loop it terminates the loop from there only and gets the program out of loop 
but sometimes we have to just skip an iteration then we use continue in that case
"""
for i in range(1,20):
    if i%2== 0:
        continue
    if i ==19:
        break
    print(i)
#few uestions on basis of loops 
for j in range(1,4):
        print("*"*j)
for i in range(1,11):
    if i%2==0:
        print("#",end="")
    if i%3==0:
        print("@",end="")
    
    if i%7==0:
        print("~",end="")
    else :
        print(i)
#Nested Loops in the Python
for i in range(1,11):
    for j in range(i,11):
        print("$",end="")
    print(" ")
""" Output 
$ 
$$ 
$$$ 
$$$$ 
$$$$$ 
$$$$$$ 
$$$$$$$ 
$$$$$$$$ 
$$$$$$$$$ """
for i in range(1,11):
    for j in range(1,i):
        print("$",end="")
    print(" ")
"""Output
$$$$$$$$$$ 
$$$$$$$$$ 
$$$$$$$$ 
$$$$$$$ 
$$$$$$ 
$$$$$ 
$$$$ 
$$$ 
$$ 
$ """
list= ["Mango","Apple","grapes","Mongo"]
for fruit in list:
    for word in fruit:
        if word == "M":
            print(fruit)



color =["Red","Green","Blue"]
fruit=["Mango","Apple","grapes","Mongo"]

for x in color:
    for y in fruit:
        print(x,y)
    print()



# for loop with if else statement it execute only when loop doesn't terminate abruptly

fav =['Py','C','java','Ruby']

for lang in fav:
    if 'java' == lang:
        print("Java found")
        break
    else:
        print("Java not Found")

#while loop condition becomes false and loop runs normally then else block will be executed
import random
count =0
while count!=10:
    die= random.randint(1,6)
    if die!=6:
        count+=1
    else:
        print(count)
x=30
y=50
z=10
if x>y or x>z:
    print("x is larger")
else:
    print("x is the smallest")
    
if x>y and x>z:
    print("x is largest")
else:
    print("x is the smallest")

if not(x>y or x>z):
    print("x is not largest")
else:
    print("x is large")

l1=[1,2,3,4,5]
l2=[1,2,4,5]

if l1==l2:
    print(True)
else:
    print(False)
    # returns false


l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

if l1==l2:
    print(True)
else:
    print(False)
# return True

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

if l1 is l2:
    print(True)
else:
    print(False)

#returns false

